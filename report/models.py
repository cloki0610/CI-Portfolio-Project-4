from django.db import models
from django.contrib.auth.models import User
from theme.models import Theme


REPORT_TYPE = ((0, "Others"), (1, "Sensitive Speech"), (2, "Personal Attack"))


class Report(models.Model):
    """ to manage the report from user """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_report")
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE,
                                 related_name="theme_report")
    email = models.EmailField(max_length=50, blank=True, default='')
    report_type = models.IntegerField(choices=REPORT_TYPE, default=0)
    description = models.TextField(blank=True, default='')
    submit_on = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    class Meta:
        """ Data should order by submit date """
        ordering = ['-submit_on']

    def __str__(self):
        return f"Report from {self.user}"
