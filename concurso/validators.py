from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_positive_number(value):
    if value <= 0:
        raise ValidationError("El número debe ser positivo.")
    

def validate_future_date(value):
    if value <= timezone.now().date():
        raise ValidationError("La fecha debe ser posterior a la fecha actual.")