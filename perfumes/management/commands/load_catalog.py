from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand, call_command

from perfumes.models import Perfume


class Command(BaseCommand):
    help = "Carga el catalogo inicial de perfumes si la base esta vacia."

    def handle(self, *args, **options):
        if Perfume.objects.exists():
            self.stdout.write(self.style.SUCCESS("El catalogo ya existe; no se cargaron datos."))
            return

        fixture_path = Path(settings.BASE_DIR) / "perfumes" / "fixtures" / "initial_data.json"
        call_command("loaddata", str(fixture_path))
        self.stdout.write(self.style.SUCCESS("Catalogo inicial cargado correctamente."))
