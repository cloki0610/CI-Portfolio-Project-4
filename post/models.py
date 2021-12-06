""" Post Data Model """
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from theme.models import Theme


class Post(models.Model):
    """ To manage the post written by creators """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE,
                              related_name="theme_posts")
    publish_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_body = models.TextField(blank=True)

    class Meta:
        """ Data should order by update date """
        ordering = ['-updated_on']

    def __str__(self):
        return f"{self.title} of {self.theme}"


@receiver(pre_save, sender=Post)
def post_pre_save(sender, instance, *args, **kwargs):
    """ auto add slug to the slug column """
    if not instance.slug:
        instance.slug = slugify(instance.title)
