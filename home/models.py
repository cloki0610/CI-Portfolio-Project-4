""" Category Data model """
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Category(models.Model):
    """ Model for handle different categories """
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200)
    introduction = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categorie"

    def __str__(self):
        return str(self.name)


@receiver(pre_save, sender=Category)
def catrgory_pre_save(sender, instance, *args, **kwargs):
    """ auto add slug to the slug column """
    if not instance.slug:
        instance.slug = slugify(instance.name)
