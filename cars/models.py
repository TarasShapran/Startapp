from django.db import models
from django.core import validators as v

from autopark.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'car'

    brand = models.CharField(max_length=20, validators=[v.MinLengthValidator(3), v.MaxLengthValidator(20)])
    model = models.CharField(max_length=20)
    year = models.DateField()
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
