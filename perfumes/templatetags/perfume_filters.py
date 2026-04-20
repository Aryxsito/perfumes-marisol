from django import template

register = template.Library()


@register.filter
def format_clp(value):
    """
    Formatea un número en pesos chilenos con puntos cada 3 dígitos.
    Ejemplo: 45000 -> 45.000, 1500000 -> 1.500.000
    """
    try:
        value = int(value)
        # Convertir a string y formatear con puntos
        formatted = f"{value:,}".replace(",", ".")
        return formatted
    except (ValueError, TypeError):
        return value
