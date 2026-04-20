# Aroma Sublime

Aplicacion web local para gestionar inventario de perfumes con Django + SQLite. Pensada para catalogo visual de perfumes de imitacion con fotos comparativas y una interfaz elegante, llamativa e interactiva.

## Requisitos

- Python 3.10+
- pip

## Instalacion

1. Crear y activar entorno virtual.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Crear superusuario (opcional):

```bash
python manage.py createsuperuser
```

5. Levantar servidor:

```bash
python manage.py runserver
```

## Estructura clave

- app: perfumes
- modelos: Perfume con imagen y stock
- plantillas: base, index, detalle, formulario
- control rapido de stock desde catalogo
- marca visual: Aroma Sublime

## Configuracion media

- `MEDIA_URL = "media/"`
- `MEDIA_ROOT = BASE_DIR / "media"`
- URLs de media activas en desarrollo desde `config/urls.py`
