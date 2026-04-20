#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from perfumes.models import Acorde

acordes_data = [
    ("cálido especiado", "#D84D2D"),
    ("dulce", "#E84D6D"),
    ("avainillado", "#E8D4A0"),
    ("canela", "#B8724D"),
    ("café", "#704D3D"),
    ("ámbar", "#B8763D"),
    ("atalcado", "#9B9B9B"),
]

for nombre, color in acordes_data:
    acorde, created = Acorde.objects.get_or_create(
        nombre=nombre,
        defaults={"color": color}
    )
    status = "✓ Creado" if created else "✗ Ya existe"
    print(f"{status}: {nombre} ({color})")

print(f"\nTotal de acordes: {Acorde.objects.count()}")
