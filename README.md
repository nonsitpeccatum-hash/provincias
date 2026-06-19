# Bot de Enrutamiento — Red Gay España

Bot de Telegram que pregunta zona geográfica y rango de edad a cada usuario
nuevo, y le entrega automáticamente los enlaces de:
1. Su grupo de zona/provincia
2. Su grupo de rango de edad
3. Los grupos generales/temáticos (para todos)

Un usuario solo puede completar el registro **una vez**. Si vuelve a escribir
`/start`, el bot le repite el mismo resultado de su primer registro — sin
opción a cambiar de zona o edad.

## Estructura

```
telegram-router-bot/
├── bot.py              # Lógica del bot (handlers, conversación)
├── database.py         # Conexión y queries a PostgreSQL
├── data.py             # Zonas, edades y grupos generales (editar aquí)
├── requirements.txt
├── Procfile
└── .env.example
```

## 1. Crear el bot en Telegram

1. Habla con [@BotFather](https://t.me/BotFather)
2. `/newbot` → elige nombre y username
3. Guarda el **token** que te da (algo como `123456:ABC-DEF...`)

## 2. Subir el código a GitHub

```bash
cd telegram-router-bot
git init
git add .
git commit -m "Bot de enrutamiento por zona y edad"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/telegram-router-bot.git
git push -u origin main
```

## 3. Desplegar en Railway

1. Entra a [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**
2. Selecciona el repositorio que acabas de subir
3. Añade el plugin de base de datos: **New** → **Database** → **Add PostgreSQL**
4. En el servicio del bot (no en el de Postgres), ve a **Variables** y añade:
   - `BOT_TOKEN` = el token de @BotFather
   - `DATABASE_URL` = referencia la variable de Postgres así: `${{Postgres.DATABASE_URL}}`
     (Railway te autocompleta esto si escribes `${{` en el campo de valor)
5. Railway detectará el `Procfile` y arrancará el proceso `worker: python bot.py`
6. Revisa los **Logs** del servicio: deberías ver:
   ```
   Pool de PostgreSQL creado correctamente.
   Tabla 'usuarios' verificada/creada.
   Bot listo. Pool de base de datos inicializado.
   Iniciando polling...
   ```

## 4. Probar el bot

1. Búscalo en Telegram por su username
2. `/start` → debe mostrar los 19 botones de zona
3. Elige una zona → debe mostrar los 5 botones de edad
4. Elige una edad → debe enviar el mensaje final con los 3 bloques de enlaces
5. Vuelve a mandar `/start` → debe repetir el mismo resultado, sin dejarte elegir de nuevo

## Comando de administración

`/status` — muestra cuántos usuarios se han registrado en total. Útil para
verificar que el bot está funcionando y para llevar métricas básicas sin
entrar a la base de datos directamente.

## Editar zonas, edades o grupos generales

Todo el contenido editable está en `data.py`. Si necesitas:
- Cambiar un enlace → edita el valor `"enlace"` correspondiente
- Añadir una zona nueva → añade una entrada nueva al diccionario `ZONAS`
  con una `callback_data` (clave) única, por ejemplo `"zona_nueva_zona"`
- **Importante**: no cambies las claves (`callback_data`) de zonas/edades ya
  publicadas si el bot lleva tiempo activo — los botones que la gente ya
  recibió en chats antiguos dejarían de funcionar. Es seguro añadir nuevas
  claves, pero evita renombrar las existentes.

Después de editar `data.py`, haz `git push` y Railway redespliega automáticamente.
