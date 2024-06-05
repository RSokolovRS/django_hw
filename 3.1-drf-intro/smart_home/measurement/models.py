import uuid

from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Место расположения')
    description = models.CharField(max_length=255, verbose_name='Описание датчика')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.FloatField(verbose_name='Температура')
    date_time = models.DateTimeField(verbose_name='Дата и Время')
    name = models.OneToOneField(Sensor, on_delete=models.CASCADE, related_name='sensor')



