from django import forms

from .models import Perfume, Acorde


class PerfumeForm(forms.ModelForm):
    acordes = forms.ModelMultipleChoiceField(
        queryset=Acorde.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Acordes principales"
    )
    
    class Meta:
        model = Perfume
        fields = [
            "nombre",
            "inspiracion",
            "caracteristicas",
            "descripcion",
            "precio",
            "stock",
            "imagen",
            "imagen_original",
            "acordes",
        ]
        widgets = {
            "caracteristicas": forms.Textarea(attrs={"rows": 5, "placeholder": "Marca: Al Haramain\nTipo: Eau de Parfum (EDP)\nContenido: 120ml\nGénero: Unisex\nEstilo: Oriental ambarado"}),
            "descripcion": forms.Textarea(attrs={"rows": 4}),
            "precio": forms.NumberInput(attrs={"placeholder": "Ingresa el precio en CLP", "min": "0"}),
        }

