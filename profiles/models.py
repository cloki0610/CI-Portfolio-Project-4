""" UserProfile Data model """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import cloudinary


class UserProfile(models.Model):
    """
    A extend model for store user information
    """
    ROLES = ((0, "member"), (1, "creator"), (2, "admin"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, default='')
    membership = models.IntegerField(choices=ROLES, default=0)
    registered_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50, blank=True, default='')
    bio = models.TextField(blank=True, default='')
    user_icon = CloudinaryField('image', default='placeholder')

    class Meta:
        """ Data should order by register date """
        ordering = ['registered_on']
        verbose_name = "Profile"

    def __str__(self):
        return self.name or self.user.username


@receiver(pre_delete, sender=UserProfile)
def icon_delete(sender, instance, **kwargs):
    """ try to remove the image in cloudinary when user record deleted """
    cloudinary.uploader.destroy(instance.user_icon.public_id)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Create profile when new user signup """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
