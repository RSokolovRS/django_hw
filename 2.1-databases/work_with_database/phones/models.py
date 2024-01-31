from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=255, verbose_name='Модель')
    slug = AutoSlugField(max_length=255, populate_from='name', editable=True, always_update=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='image')
    release_date = models.DateField(auto_now_add=False)
    lte_exists = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name}, {self.price}'

