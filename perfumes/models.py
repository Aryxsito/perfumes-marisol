from django.db import models


class Acorde(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    color = models.CharField(
        max_length=7,
        default="#d4af37",
        help_text="Color hexadecimal para mostrar el acorde (ej: #ff5733)"
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Perfume(models.Model):
    nombre = models.CharField(max_length=120)
    inspiracion = models.CharField(max_length=180)
    caracteristicas = models.TextField(
        blank=True,
        help_text="Ingresa cada característica en una línea nueva (Marca, Tipo, Contenido, etc.)"
    )
    descripcion = models.TextField()
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(
        default=0,
        help_text="Precio en CLP (Pesos Chilenos)"
    )
    imagen = models.ImageField(
        "Foto principal (imitacion)",
        upload_to="perfumes/imitaciones/",
        blank=True,
        null=True,
    )
    imagen_original = models.ImageField(
        "Foto del perfume original",
        upload_to="perfumes/originales/",
        blank=True,
        null=True,
    )
    acordes = models.ManyToManyField(Acorde, blank=True, related_name="perfumes")

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
