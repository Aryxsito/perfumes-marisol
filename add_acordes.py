import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from perfumes.models import Acorde

acordes_nuevos = [
    {"nombre": "dulce", "color": "#ff4a50"},
    {"nombre": "afrutados", "color": "#ff6b5b"},
    {"nombre": "ozónico", "color": "#7dd3c0"},
    {"nombre": "atalcado", "color": "#b3a89f"},
    {"nombre": "avainillado", "color": "#d4c876"},
    {"nombre": "almizclado", "color": "#d4b5d4"},
    {"nombre": "fresco", "color": "#5c9ccc"},
    {"nombre": "ámbar", "color": "#a0581c"},
    {"nombre": "acuático", "color": "#5db3d4"},
    {"nombre": "cítrico", "color": "#c4d65b"},
    {"nombre": "fresco especiado", "color": "#7cb342"},
    {"nombre": "aromático", "color": "#4a7c7e"},
    {"nombre": "cálido especiado", "color": "#aa3d23"},
    {"nombre": "lavanda", "color": "#9b7bb2"},
    {"nombre": "iris", "color": "#a796b5"},
    {"nombre": "violeta", "color": "#6a3a7a"},
    {"nombre": "verde", "color": "#2d5016"},
    {"nombre": "amaderado", "color": "#6b5344"},
    {"nombre": "herbal", "color": "#5a7a5a"},
    {"nombre": "floral blanco", "color": "#f0f0f0"},
    {"nombre": "florales", "color": "#c85a7f"},
    {"nombre": "caramelo", "color": "#8b6f47"},
    {"nombre": "terrosos", "color": "#7a6d5d"},
    {"nombre": "marino", "color": "#1e5a96"},
    {"nombre": "salado", "color": "#c9bfb5"},
    {"nombre": "rosas", "color": "#b8247a"},
    {"nombre": "balsámico", "color": "#8b7355"},
    {"nombre": "aldehídico", "color": "#8f8f8f"},
    {"nombre": "ron", "color": "#8b4513"},
    {"nombre": "lactónico", "color": "#a9a9a9"},
]

for acorde_data in acordes_nuevos:
    acorde, created = Acorde.objects.get_or_create(
        nombre=acorde_data["nombre"],
        defaults={"color": acorde_data["color"]}
    )
    if created:
        print(f"✓ Acorde '{acorde.nombre}' agregado")
    else:
        print(f"- Acorde '{acorde.nombre}' ya existe")

print(f"\nAcordes totales en la base de datos: {Acorde.objects.count()}")
