
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
        "enlace": "https://t.me/+HUTtmU819RMwMTQ0",
    },
    "zona_madrid": {
        "nombre": "Madrid",
        "detalle": "Madrid y alrededores",
        "enlace": "https://t.me/+BVppEG39X7BjMGE0",
    },
    "zona_cyl_sur": {
        "nombre": "Castilla y León SUR",
        "detalle": "Salamanca, Zamora, Segovia, Ávila y Soria",
        "enlace": "https://t.me/+y-csjoNusd40ODU0",
    },
    "zona_burgos": {
        "nombre": "Burgos",
        "detalle": "Burgos y provincia",
        "enlace": "https://t.me/+MB3LBsoWL5hkYmE0",
    },
    "zona_valladolid_palencia": {
        "nombre": "Valladolid y Palencia",
        "detalle": "Valladolid y Palencia",
        "enlace": "https://t.me/+yhp0Qz_ataFjN2Vk",
    },
    "zona_toledo_talavera": {
        "nombre": "Toledo y Talavera",
        "detalle": "Toledo y Talavera",
        "enlace": "https://t.me/+zMIwHHCOvzhiMjM8",
    },
    "zona_clm_este": {
        "nombre": "Castilla-La Mancha Este",
        "detalle": "Ciudad Real, Cuenca, Guadalajara y Albacete",
        "enlace": "https://t.me/+Lm5ejpM-TJRjZGY0",
    },
    "zona_valencia_castellon": {
        "nombre": "Valencia & Castellón",
        "detalle": "Valencia y Castellón",
        "enlace": "https://t.me/+PXCC9tZlHR1kMjNk",
    },
    "zona_alicante_murcia": {
        "nombre": "Alicante & Murcia",
        "detalle": "Alicante y Murcia",
        "enlace": "https://t.me/+1E-_FPs_oMBkNzNk",
    },
    "zona_aragon": {
        "nombre": "Aragón",
        "detalle": "Zaragoza, Huesca y Teruel",
        "enlace": "https://t.me/+qADOZdu-Uk05NjY0",
    },
    "zona_galicia": {
        "nombre": "Galicia",
        "detalle": "A Coruña, Pontevedra, Lugo y Ourense",
        "enlace": "https://t.me/+bRin9DGytf0yN2Vk",
    },
    "zona_andalucia_occidental": {
        "nombre": "Andalucía Occidental",
        "detalle": "Sevilla, Córdoba, Cádiz y Huelva",
        "enlace": "https://t.me/+PXCC9tZlHR1kMjNk",
    },
    "zona_andalucia_oriental": {
        "nombre": "Andalucía Oriental",
        "detalle": "Málaga, Granada, Jaén y Almería",
        "enlace": "https://t.me/+hSyYLLJUqwZlNmI0",
    },
    "zona_canarias": {
        "nombre": "Canarias",
        "detalle": "Tenerife, Gran Canaria, Lanzarote y Fuerteventura",
        "enlace": "https://t.me/+psmJBet2Sk0zMzE0",
    },
    "zona_baleares": {
        "nombre": "Baleares",
        "detalle": "Mallorca, Ibiza, Menorca y Formentera",
        "enlace": "https://t.me/+5VgiyhPlxw9mODc0",
    },
    "zona_asturias_cantabria_leon": {
        "nombre": "Asturias, Cantabria y León",
        "detalle": "Asturias, Cantabria y León",
        "enlace": "https://t.me/+DMnCKbupiDwzNWU8",
    },
    "zona_pv_navarra": {
        "nombre": "País Vasco & Navarra",
        "detalle": "Bilbao, San Sebastián, Vitoria, Pamplona y Logroño",
        "enlace": "https://t.me/+cTAQ_Ou9PCo0NzE0",
    },
    "zona_extremadura": {
        "nombre": "Extremadura",
        "detalle": "Cáceres y Badajoz",
        "enlace": "https://t.me/+0hI4OmR-lpM0OTNk",
    },
    "zona_ceuta_melilla": {
        "nombre": "Ceuta y Melilla",
        "detalle": "Ceuta y Melilla",
        "enlace": "https://t.me/+kOraxuJcMvMxZmE0",
    },
    "zona_hispanoamerica": {
        "nombre": "Hispanoamérica",
        "detalle": "Fuera de España",
        "enlace": "https://t.me/+XzqpQRbqoctjOTFk",
    },
}
 
# ──────────────────────────────────────────────────────────────────────────
# RANGOS DE EDAD
# ──────────────────────────────────────────────────────────────────────────
EDADES = {
    "edad_-15": {
        "nombre": "- de 15",
        "enlace": "https://www.youtube.com/watch?v=m0dhNHYbWT8", 
     },
     "edad_15_18": {
        "nombre": "15 a 18",
        "enlace": "https://www.youtube.com/watch?v=m0dhNHYbWT8",
     },
    "edad_18_30": {
        "nombre": "18 a 30",
        "enlace": "https://t.me/+SIWj5Abr9-IxNjE0",
    },
    "edad_31_40": {
        "nombre": "31 a 40",
        "enlace": "https://t.me/+C3gOzB6vfX0zZDZk",
    },
    "edad_41_50": {
        "nombre": "41 a 50",
        "enlace": "https://t.me/+J8P5rGEYjGU5Yzg0",
    },
    "edad_mas_50": {
        "nombre": "+50",
        "enlace": "https://t.me/+x2JlX0GqPhczYWM0",
    },
}
 
# ──────────────────────────────────────────────────────────────────────────
# GRUPOS GENERALES / TEMÁTICOS (se entregan siempre, a todo el mundo)
# ──────────────────────────────────────────────────────────────────────────
GENERALES = [
    {"nombre": "Hablar sin miedo (grupo blanco)", "enlace": "https://t.me/+LHtWQBUZ5-phNjk0"},
    {"nombre": "Conexiones Reales (grupo blanco)", "enlace": "https://t.me/+96J7nDyReJ4yOTM0"},
 
    {"nombre": "Videochat Gay España", "enlace": "https://t.me/+jElxv1yaIZA1Njg0"},
    {"nombre": "Bears España", "enlace": "https://t.me/+kdXdBhSv84c4MzNk"},
    {"nombre": "Relatos Gay", "enlace": "https://t.me/+v_gLKWyqERJmZTM0"},
    {"nombre": "Retos Gay", "enlace": "https://t.me/+UMy01sLmYU00ZDlk"},
    {"nombre": "BDSM (grupo adulto temático)", "enlace": "https://t.me/+EBAP-5WcmuI4MDQ0"},
    {"nombre": "Intergeneracional (todas las edades)", "enlace": "https://t.me/+g3EQ0E8V-lowODlk"},
    {"nombre": "Decus Mensis (El honor se vota)", "enlace": "https://t.me/+jNMF_TpbfOkzZmQ8"},
    {"nombre": "Grupos Amigos", "enlace": "https://t.me/+-QGfKH5PltMzOGQ0"},
]
 
# Mención especial del grupo BOYS: no es un enlace de acceso directo,
# tiene su propio embudo vía @BienvenidaPeccbot (presentación + foto + aprobación admin).
BOYS_INFO = {
    "texto": (
        "🔒 Y para *BOYS*, ambiente más activo: te presentas con foto en el "
        f"[Grupo de presentación BOYS](https://t.me/+u2goGuMVEeBhODc0) y entras."
    )
}
 
