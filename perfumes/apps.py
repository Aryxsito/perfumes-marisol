from django.apps import AppConfig


class PerfumesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "perfumes"

    def ready(self):
        from . import signals  # noqa: F401
