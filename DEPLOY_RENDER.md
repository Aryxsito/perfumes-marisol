# 🚀 Guía de Despliegue en Render (Gratuito)

## Paso 1: Preparar Git Localmente
```bash
git init
git add .
git commit -m "Initial commit - Perfumes Marisol"
```

## Paso 2: Crear un Repositorio en GitHub
1. Ve a https://github.com/new
2. Crea un repositorio llamado `perfumes-marisol`
3. Copia los comandos que GitHub te proporciona para conectar tu repositorio local

## Paso 3: Conectar con Render
1. Ve a https://render.com
2. Regístrate/inicia sesión con GitHub
3. Haz clic en "New Web Service"
4. Selecciona tu repositorio `perfumes-marisol`
5. Configura así:
   - **Name**: perfumes-marisol
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn config.wsgi:application`

## Paso 4: Variables de Entorno en Render
En el panel de Render, agrega estas variables de entorno:
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `tu-app.onrender.com` (reemplaza con tu dominio real)
- `SECRET_KEY`: Genera una clave segura (https://djecrety.ir/)

## Paso 5: Base de Datos en Producción
Para pasar de SQLite a PostgreSQL (recomendado en Render):
1. Render te proporciona un PostgreSQL gratuito
2. En la sección "Database" de Render, crea una base de datos PostgreSQL
3. Copia la URL de conexión
4. En variables de entorno, agrega: `DATABASE_URL`: [tu-url-postgres]
5. Instala en requirements.txt: `psycopg2-binary`

## Notas Importantes
- El plan gratuito de Render es muy bueno pero se "duerme" si no hay actividad
- Puedes acceder a tu app en: https://perfumes-marisol.onrender.com
- Los archivos subidos (media) en el servidor se pierden cada cierto tiempo (considera usar un almacenamiento externo como Cloudinary)
