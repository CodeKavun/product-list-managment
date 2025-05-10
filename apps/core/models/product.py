from django.db import models

from apps.core.models.brand import Brand
from apps.core.models.catalog import Subcategory


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField()
    price = models.FloatField()
    amount = models.IntegerField(default=1)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}: {self.price}UAH, x{self.amount}"
