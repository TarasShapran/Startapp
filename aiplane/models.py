from django.db import models
from django.core import validators as v


# Create your models here.
class AirPlaneModel(models.Model):
    class Meta:
        db_table = 'airplane'

    name = models.CharField(max_length=20,
                            validators=[v.RegexValidator('^[a-zA-Z]{3,20}$', 'name must be 3-20 characters')])
    speed = models.IntegerField(validators=[v.MinValueValidator(100)])
    engine = models.IntegerField()
