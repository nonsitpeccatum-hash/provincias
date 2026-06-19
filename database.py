# -*- coding: utf-8 -*-
"""
Capa de acceso a PostgreSQL.
Usa asyncpg con un pool de conexiones (compatible con el loop async de PTB).
"""

import os
import logging
import asyncpg

logger = logging.getLogger(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

_pool: asyncpg.Pool | None = None


async def init_pool() -> None:
    """Crea el pool de conexiones y asegura que la tabla exista."""
    global _pool
    if not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL no está definida. En Railway, añade el add-on de "
            "PostgreSQL y conecta la variable al servicio del bot."
        )

    _pool = await asyncpg.create_pool(dsn=DATABASE_URL, min_size=1, max_size=5)
    logger.info("Pool de PostgreSQL creado correctamente.")

    async with _pool.acquire() as conn:
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                telegram_id BIGINT PRIMARY KEY,
                username TEXT,
                zona TEXT NOT NULL,
                rango_edad TEXT NOT NULL,
                fecha_registro TIMESTAMP DEFAULT NOW()
            );
            """
        )
    logger.info("Tabla 'usuarios' verificada/creada.")


async def close_pool() -> None:
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None


async def obtener_registro(telegram_id: int) -> asyncpg.Record | None:
    """Devuelve la fila del usuario si ya está registrado, o None."""
    async with _pool.acquire() as conn:
        return await conn.fetchrow(
            "SELECT telegram_id, username, zona, rango_edad, fecha_registro "
            "FROM usuarios WHERE telegram_id = $1;",
            telegram_id,
        )


async def crear_registro(
    telegram_id: int, username: str | None, zona_key: str, edad_key: str
) -> bool:
    """
    Inserta el registro del usuario. Devuelve True si se insertó,
    False si ya existía (gracias a la PK, es atómico: no hay carrera posible
    entre 'comprobar si existe' e 'insertar').
    """
    async with _pool.acquire() as conn:
        result = await conn.execute(
            """
            INSERT INTO usuarios (telegram_id, username, zona, rango_edad)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (telegram_id) DO NOTHING;
            """,
            telegram_id,
            username,
            zona_key,
            edad_key,
        )
        # asyncpg devuelve algo como "INSERT 0 1" si insertó, "INSERT 0 0" si no.
        return result.endswith(" 1")


async def contar_usuarios() -> int:
    async with _pool.acquire() as conn:
        row = await conn.fetchrow("SELECT COUNT(*) AS total FROM usuarios;")
        return row["total"]
