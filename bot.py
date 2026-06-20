# -*- coding: utf-8 -*-
"""
Bot de enrutamiento por perfil (zona + edad) para Red Gay España.

Flujo:
  /start
    └─ ¿Usuario ya registrado en BD?
         SÍ -> repetir el resultado guardado (zona + edad + generales), FIN
         NO -> mostrar botones de ZONA
                └─ callback zona -> guardar en user_data (memoria, no BD)
                                  -> mostrar botones de EDAD
                                       └─ callback edad -> INSERT en BD (sella el registro)
                                                         -> enviar resultado completo

Si el usuario abandona a mitad del flujo (eligió zona, no edad) y vuelve con /start,
se reinicia desde cero: no hay penalización porque el registro NO se considera
"completado" hasta que se inserta en la base de datos.
"""

import os
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

import database
from data import ZONAS, EDADES, GENERALES, BOYS_INFO

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Prefijos para distinguir el tipo de callback_data en el handler genérico de botones
PREFIJO_ZONA = "zona_"
PREFIJO_EDAD = "edad_"


# ──────────────────────────────────────────────────────────────────────────
# Helpers de construcción de teclados y mensajes
# ──────────────────────────────────────────────────────────────────────────

def teclado_zonas() -> InlineKeyboardMarkup:
    botones = [
        [InlineKeyboardButton(info["nombre"], callback_data=key)]
        for key, info in ZONAS.items()
    ]
    return InlineKeyboardMarkup(botones)


def teclado_edades() -> InlineKeyboardMarkup:
    botones = [
        [InlineKeyboardButton(info["nombre"], callback_data=key)]
        for key, info in EDADES.items()
    ]
    return InlineKeyboardMarkup(botones)


def construir_mensaje_resultado(zona_key: str, edad_key: str) -> str:
    """Construye el texto final con los 3 bloques de enlaces."""
    zona = ZONAS[zona_key]
    edad = EDADES[edad_key]

    lineas = []
    lineas.append("✅ *Listo, ya estás dentro.*\n")

    lineas.append(f"📍 *Tu zona* — {zona['nombre']}")
    lineas.append(f"[Unirme al grupo de mi zona]({zona['enlace']})\n")

    lineas.append(f"🎂 *Tu edad* — {edad['nombre']}")
    lineas.append(f"[Unirme al grupo de mi edad]({edad['enlace']})\n")

    lineas.append("🔥 *Además, estos están abiertos para todos:*")
    for grupo in GENERALES:
        if edad_key in grupo.get("excluir_edades", []):
            continue
        lineas.append(f"• [{grupo['nombre']}]({grupo['enlace']})")
    lineas.append("")

    lineas.append(BOYS_INFO["texto"])

    return "\n".join(lineas)


# ──────────────────────────────────────────────────────────────────────────
# Handlers
# ──────────────────────────────────────────────────────────────────────────

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_id = update.effective_user.id

    registro = await database.obtener_registro(telegram_id)

    if registro is not None:
        # Ya registrado: repetir el resultado original, sin opción a cambiar.
        zona_key = registro["zona"]
        edad_key = registro["rango_edad"]
        texto = (
            "ℹ️ Ya hiciste tu registro antes, no puedes cambiar zona ni edad.\n\n"
        ) + construir_mensaje_resultado(zona_key, edad_key)
        await update.message.reply_text(
            texto, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
        return

    # Usuario nuevo: empezar flujo desde cero.
    context.user_data.clear()
    texto = (
        "👋 ¡Bienvenido/a a *Red Gay España*!\n\n"
        "Para llevarte a tus grupos, dime cuál es la *capital de tu provincia*.\n\n"
        "Elige tu zona abajo. ¿Vives fuera de España? Elige *Hispanoamérica*."
    )
    await update.message.reply_text(
        texto, parse_mode=ParseMode.MARKDOWN, reply_markup=teclado_zonas()
    )


async def callback_zona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    zona_key = query.data
    if zona_key not in ZONAS:
        await query.edit_message_text("⚠️ Zona no válida. Por favor usa /start de nuevo.")
        return

    # Si el usuario ya se registró entretanto (doble clic, mensaje viejo reabierto, etc.)
    telegram_id = update.effective_user.id
    registro = await database.obtener_registro(telegram_id)
    if registro is not None:
        texto = (
            "ℹ️ Ya hiciste tu registro antes.\n\n"
            + construir_mensaje_resultado(registro["zona"], registro["rango_edad"])
        )
        await query.edit_message_text(
            texto, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
        return

    context.user_data["zona_key"] = zona_key
    zona_nombre = ZONAS[zona_key]["nombre"]

    texto = (
        f"📍 Zona: *{zona_nombre}*\n\n"
        "Ahora dime tu rango de edad:"
    )
    await query.edit_message_text(
        texto, parse_mode=ParseMode.MARKDOWN, reply_markup=teclado_edades()
    )


async def callback_edad(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    edad_key = query.data
    if edad_key not in EDADES:
        await query.edit_message_text("⚠️ Opción no válida. Por favor usa /start de nuevo.")
        return

    zona_key = context.user_data.get("zona_key")
    if zona_key is None:
        # El usuario llegó aquí sin haber pasado por la selección de zona
        # (ej. mensaje antiguo, o reinicio del proceso perdió el estado en memoria).
        await query.edit_message_text(
            "⚠️ Parece que tu sesión expiró o el bot se reinició. "
            "Por favor, vuelve a empezar con /start."
        )
        return

    telegram_id = update.effective_user.id
    username = update.effective_user.username

    insertado = await database.crear_registro(telegram_id, username, zona_key, edad_key)

    if not insertado:
        # Carrera: alguien completó el registro justo antes (muy raro, pero posible).
        registro = await database.obtener_registro(telegram_id)
        texto = (
            "ℹ️ Ya hiciste tu registro antes.\n\n"
            + construir_mensaje_resultado(registro["zona"], registro["rango_edad"])
        )
        await query.edit_message_text(
            texto, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
        return

    context.user_data.clear()
    texto = construir_mensaje_resultado(zona_key, edad_key)
    await query.edit_message_text(
        texto, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando de utilidad para Héctor: cuántos usuarios se han registrado."""
    total = await database.contar_usuarios()
    await update.message.reply_text(f"📊 Usuarios registrados: {total}")


async def post_init(application: Application) -> None:
    await database.init_pool()
    logger.info("Bot listo. Pool de base de datos inicializado.")


async def post_shutdown(application: Application) -> None:
    await database.close_pool()


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN no está definido en las variables de entorno.")

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )

    application.add_handler(CommandHandler("start", cmd_start))
    application.add_handler(CommandHandler("status", cmd_status))
    application.add_handler(
        CallbackQueryHandler(callback_zona, pattern=f"^{PREFIJO_ZONA}")
    )
    application.add_handler(
        CallbackQueryHandler(callback_edad, pattern=f"^{PREFIJO_EDAD}")
    )

    logger.info("Iniciando polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
