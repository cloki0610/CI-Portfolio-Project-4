""" Promote Request Data Model """
from django.db import models
from django.contrib.auth.models import User
from home.models import Category


class PromoteRequest(models.Model):
    """ to manage the request from user who want to becom creator """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_request")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="category_request")
    reason = models.TextField(blank=True)
    submit_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Data should order by submit date """
        ordering = ['-submit_on']

    def __str__(self):
        return f"Promote Request from {self.user}"
