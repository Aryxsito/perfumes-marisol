from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Perfume


@receiver(post_migrate)
def load_initial_catalog(sender, app_config, **kwargs):
    if app_config.name != "perfumes":
        return

    if Perfume.objects.exists():
        pass

    fixture_path = Path(settings.BASE_DIR) / "perfumes" / "fixtures" / "initial_data.json"
    if fixture_path.exists() and not Perfume.objects.exists():
        call_command("loaddata", str(fixture_path))

    User = get_user_model()
    username = settings.ADMIN_USERNAME if hasattr(settings, "ADMIN_USERNAME") else None
    username = username or "Marisol"
    email = getattr(settings, "ADMIN_EMAIL", None) or "aromasublime1971@gmail.com"
    password = getattr(settings, "ADMIN_PASSWORD", None) or "Marisol2026!"

    user = User.objects.filter(username=username).first()
    if user is None:
        User.objects.create_superuser(username=username, email=email, password=password)
        return

    changed = False
    if not user.is_staff:
        user.is_staff = True
        changed = True
    if not user.is_superuser:
        user.is_superuser = True
        changed = True
    if email and user.email != email:
        user.email = email
        changed = True
    if changed:
        user.set_password(password)
        user.save()
