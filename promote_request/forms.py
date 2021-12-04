""" Create form model to display request form to become creator """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import PromoteRequest


class PromoteRequestForm(forms.ModelForm):
    """ Form model to let user submit a request form """
    reason = forms.CharField(widget=SummernoteWidget())

    class Meta:
        """ Handle the column in form """
        model = PromoteRequest
        fields = ('category', 'reason')
