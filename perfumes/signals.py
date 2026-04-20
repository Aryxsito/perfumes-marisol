from pathlib import Path

from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Perfume


@receiver(post_migrate)
def load_initial_catalog(sender, app_config, **kwargs):
    if app_config.name != "perfumes":
        return

    if Perfume.objects.exists():
        return

    fixture_path = Path(settings.BASE_DIR) / "perfumes" / "fixtures" / "initial_data.json"
    if fixture_path.exists():
        call_command("loaddata", str(fixture_path))
