from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=160)


class Subcategory(models.Model):
    name = models.CharField(max_length=160)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
