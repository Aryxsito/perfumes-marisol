from django.contrib import admin

from .models import Perfume, Acorde


@admin.register(Acorde)
class AcordeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "color")
    search_fields = ("nombre",)


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "inspiracion", "get_precio_formatted", "stock", "get_acordes_count")
    search_fields = ("nombre", "inspiracion")
    filter_horizontal = ("acordes",)
    fieldsets = (
        (None, {
            "fields": ("nombre", "inspiracion", "descripcion", "caracteristicas")
        }),
        ("Valoración", {
            "fields": ("precio", "stock"),
            "description": "Solo el administrador puede modificar estos valores"
        }),
        ("Multimedia", {
            "fields": ("imagen", "imagen_original")
        }),
        ("Acordes", {
            "fields": ("acordes",)
        }),
    )
    
    def get_acordes_count(self, obj):
        return obj.acordes.count()
    get_acordes_count.short_description = "Acordes"
    
    def get_precio_formatted(self, obj):
        return f"${obj.precio:,} CLP".replace(",", ".")
    get_precio_formatted.short_description = "Precio"
