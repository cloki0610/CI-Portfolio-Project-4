""" Category Data model """
from django.db import models


class Category(models.Model):
    """ Model for handle different categories """
    name = models.CharField(max_length=80)
    introduction = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categorie"

    def __str__(self):
        return str(self.name)
