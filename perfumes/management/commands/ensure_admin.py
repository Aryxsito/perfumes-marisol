import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Crea un superusuario en la base de datos si no existe."

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv("ADMIN_USERNAME", "Marisol")
        email = os.getenv("ADMIN_EMAIL", "aromasublime1971@gmail.com")
        password = os.getenv("ADMIN_PASSWORD", "Marisol2026!")

        user = User.objects.filter(username=username).first()
        if user is None:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superusuario creado: {username}"))
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
            self.stdout.write(self.style.SUCCESS(f"Superusuario actualizado: {username}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superusuario ya existe: {username}"))
