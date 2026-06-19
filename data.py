# -*- coding: utf-8 -*-
"""
Datos estáticos del bot: zonas geográficas, rangos de edad y grupos generales.
Cada entrada tiene un "callback_data" único (id corto) que se usa en los
botones inline, y la info que se muestra/envía al usuario.
"""

# ──────────────────────────────────────────────────────────────────────────
# ZONAS GEOGRÁFICAS (provincias agrupadas)
# callback_data debe ser único y estable (no cambiar una vez publicado el bot,
# o los botones antiguos en chats de usuarios dejarán de funcionar).
# ──────────────────────────────────────────────────────────────────────────
ZONAS = {
    "zona_catalunya": {
        "nombre": "Catalunya",
        "detalle": "Barcelona, Girona, Tarragona y Lleida",
        "enlace": "https://t.me/+jda74FtAt7c1ODlk",
    },
    "zona_madrid": {
        "nombre": "Madrid",
        "detalle": "Madrid y alrededores",
        "enlace": "https://t.me/+pXPOMryT0XMxY2Y8",
    },
    "zona_cyl_sur": {
        "nombre": "Castilla y León SUR",
        "detalle": "Salamanca, Zamora, Segovia, Ávila y Soria",
        "enlace": "https://t.me/+DXz89NmQTXAwOTk8",
    },
    "zona_burgos": {
        "nombre": "Burgos",
        "detalle": "Burgos y provincia",
        "enlace": "https://t.me/+LQCfWLLnuCNmNWFk",
    },
    "zona_valladolid_palencia": {
        "nombre": "Valladolid y Palencia",
        "detalle": "Valladolid y Palencia",
        "enlace": "https://t.me/+nwXVnpiG3TRhZWJk",
    },
    "zona_toledo_talavera": {
        "nombre": "Toledo y Talavera",
        "detalle": "Toledo y Talavera",
        "enlace": "https://t.me/+vvbxmBvk7cljOGI0",
    },
    "zona_clm_este": {
        "nombre": "Castilla-La Mancha Este",
        "detalle": "Ciudad Real, Cuenca, Guadalajara y Albacete",
        "enlace": "https://t.me/+An9eIUgGq5k1YzE0",
    },
    "zona_valencia_castellon": {
        "nombre": "Valencia & Castellón",
        "detalle": "Valencia y Castellón",
        "enlace": "https://t.me/+B0dHrjPSoOVjZmVk",
    },
    "zona_alicante_murcia": {
        "nombre": "Alicante & Murcia",
        "detalle": "Alicante y Murcia",
        "enlace": "https://t.me/+nGdOFom0AgVkM2Q8",
    },
    "zona_aragon": {
        "nombre": "Aragón",
        "detalle": "Zaragoza, Huesca y Teruel",
        "enlace": "https://t.me/+uRldVbB1a_05ZDE0",
    },
    "zona_galicia": {
        "nombre": "Galicia",
        "detalle": "A Coruña, Pontevedra, Lugo y Ourense",
        "enlace": "https://t.me/+60APVQUNCEtlNTY0",
    },
    "zona_andalucia_occidental": {
        "nombre": "Andalucía Occidental",
        "detalle": "Sevilla, Córdoba, Cádiz y Huelva",
        "enlace": "https://t.me/+xY9bn2VMdSRjMmJk",
    },
    "zona_andalucia_oriental": {
        "nombre": "Andalucía Oriental",
        "detalle": "Málaga, Granada, Jaén y Almería",
        "enlace": "https://t.me/+MmbCFccbdNtmNGY0",
    },
    "zona_canarias": {
        "nombre": "Canarias",
        "detalle": "Tenerife, Gran Canaria, Lanzarote y Fuerteventura",
        "enlace": "https://t.me/+4TRX7OPT8AE5MTI0",
    },
    "zona_baleares": {
        "nombre": "Baleares",
        "detalle": "Mallorca, Ibiza, Menorca y Formentera",
        "enlace": "https://t.me/+bGHl31DeG7liMGM8",
    },
    "zona_asturias_cantabria_leon": {
        "nombre": "Asturias, Cantabria y León",
        "detalle": "Asturias, Cantabria y León",
        "enlace": "https://t.me/+5SsdAebcjSg2YThk",
    },
    "zona_pv_navarra": {
        "nombre": "País Vasco & Navarra",
        "detalle": "Bilbao, San Sebastián, Vitoria, Pamplona y Logroño",
        "enlace": "https://t.me/+ufMAv1YU5eg5NTZk",
    },
    "zona_extremadura": {
        "nombre": "Extremadura",
        "detalle": "Cáceres y Badajoz",
        "enlace": "https://t.me/+N2dXMRhcXE9hMDY0",
    },
    "zona_ceuta_melilla": {
        "nombre": "Ceuta y Melilla",
        "detalle": "Ceuta y Melilla",
        "enlace": "https://t.me/+09Pv11SI1dpjY2M8",
    },
    "zona_hispanoamerica": {
        "nombre": "Hispanoamérica",
        "detalle": "Fuera de España",
        "enlace": "https://t.me/+skalCSJKyew0MmRk",
    },
}

# ──────────────────────────────────────────────────────────────────────────
# RANGOS DE EDAD
# ──────────────────────────────────────────────────────────────────────────
EDADES = {
    "edad_18_30": {
        "nombre": "18 a 30",
        "enlace": "https://t.me/+AP3dtljPdHlmM2M0",
    },
    "edad_31_40": {
        "nombre": "31 a 40",
        "enlace": "https://t.me/+PKxrDGqzbQdlNWFk",
    },
    "edad_41_50": {
        "nombre": "41 a 50",
        "enlace": "https://t.me/+HEVwA5soXdM1MjRk",
    },
    "edad_mas_50": {
        "nombre": "+50",
        "enlace": "https://t.me/+hS5vqc-bfhxjZDI0",
    },
}

# ──────────────────────────────────────────────────────────────────────────
# GRUPOS GENERALES / TEMÁTICOS (se entregan siempre, a todo el mundo)
# ──────────────────────────────────────────────────────────────────────────
GENERALES = [
    {"nombre": "Videochat Gay España", "enlace": "https://t.me/+HHds6El5omw3ZTlk"},
    {"nombre": "Bears España", "enlace": "https://t.me/+71GO7eMfVqYyM2E0"},
    {"nombre": "Relatos Gay", "enlace": "https://t.me/+AG-WuXXW3aljNDI0"},
    {"nombre": "Retos Gay", "enlace": "https://t.me/+1Icwqo1fU-RlODQ0"},
    {"nombre": "BDSM (grupo adulto temático)", "enlace": "https://t.me/+UTxzuztF6hY5NmM0"},
    {"nombre": "Grupos Amigos", "enlace": "https://t.me/+X0OWKauWJNphZmM0"},
    {"nombre": "Hablar sin miedo", "enlace": "https://t.me/+ga-9ISwD26g5OWRk"},
    {"nombre": "Conexiones Reales", "enlace": "https://t.me/+TNVU56xsqYM0OGFk"},
    {"nombre": "Intergeneracional (todas las edades)", "enlace": "https://t.me/+yDw1vZDRnlg0NWI0"},
]

# Mención especial del grupo BOYS: no es un enlace de acceso directo,
# tiene su propio embudo vía @BienvenidaPeccbot (presentación + foto + aprobación admin).
BOYS_INFO = {
    "texto": (
        "🔥 *Grupo BOYS* (chat con doble filtro, ambiente más activo)\n"
        "1️⃣ Entra al grupo de presentación y escríbele a @BienvenidaPeccbot con tu "
        "presentación (nombre, #Ciudad, #Edad, #LoQueBuscas) + una foto.\n"
        "2️⃣ Si tu presentación cumple las normas, el bot te da el enlace secreto al grupo real.\n"
        "3️⃣ Los admins te confirman el acceso.\n"
        f"👉 [Grupo de presentación BOYS](https://t.me/+2oaZ75NXWAgwZGI0)"
    )
}
