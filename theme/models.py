""" Theme and Comment Data Model """
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
import cloudinary
from home.models import Category


class Theme(models.Model):
    """ To manage the theme create by creators """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="author_theme")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="category_theme")
    excerpt = models.TextField(blank=True, default='')
    feature_image = CloudinaryField('image',
                                    default='featureimg')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    upvote = models.ManyToManyField(User, related_name='theme_upvote',
                                    blank=True)
    downvote = models.ManyToManyField(User, related_name='theme_downvote',
                                      blank=True)

    class Meta:
        """ Data should order by created date from latest """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} by {self.author.userprofile.name}"


@receiver(pre_delete, sender=Theme)
def feature_image_delete(sender, instance, **kwargs):
    """ try to remove the image in cloudinary when record deleted """
    cloudinary.uploader.destroy(instance.feature_image.public_id)


@receiver(pre_save, sender=Theme)
def theme_pre_save(sender, instance, *args, **kwargs):
    """ auto add slug to the slug column """
    if not instance.slug:
        instance.slug = slugify(instance.title)


class Comment(models.Model):
    """ To manage the comment written by users """
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE,
                              related_name="theme_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_comments")
    comment_body = models.TextField(blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    upvote = models.ManyToManyField(User, related_name='comment_upvote',
                                    blank=True)
    downvote = models.ManyToManyField(User, related_name='comment_downvote',
                                      blank=True)

    class Meta:
        """ The data should order by created date from latest """
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment on {self.theme} by {self.user.userprofile.name}"
