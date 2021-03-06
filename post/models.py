""" Post Data Model """
from django.db import models
from theme.models import Theme


class Post(models.Model):
    """ To manage the post written by creators """
    title = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE,
                              related_name="theme_posts")
    publish_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_body = models.TextField(blank=True)
    excerpt = models.TextField(blank=True, default='', max_length=200)

    class Meta:
        """ Data should order by update date """
        ordering = ['-updated_on']

    def __str__(self):
        return f"{self.title} of {self.theme}"
