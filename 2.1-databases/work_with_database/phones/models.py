from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='image')
    release_date = models.DateField(auto_now_add=True)
    lte_exists = models.BooleanField(default=True)