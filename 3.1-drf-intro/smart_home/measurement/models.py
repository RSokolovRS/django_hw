import uuid

from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название Датчика')
    description = models.CharField(max_length=255, verbose_name='Место расположения')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(verbose_name='Дата и Время')
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE, related_name='sensor')



