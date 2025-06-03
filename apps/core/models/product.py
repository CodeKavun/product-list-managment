from django.db import models

from apps.core.models.brand import Brand
from apps.core.models.catalog import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.FloatField()
    amount = models.IntegerField(default=1)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}: {self.price}UAH, x{self.amount}"
