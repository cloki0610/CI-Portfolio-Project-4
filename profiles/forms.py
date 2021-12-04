""" Create form model to display a form """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import UserProfile


class UserProfilesForm(forms.ModelForm):
    """ Form model to let user modify his own profile """
    bio = forms.CharField(widget=SummernoteWidget())

    class Meta:
        """ Handle the column in form"""
        model = UserProfile
        fields = ('user_icon', 'name', 'location', 'bio')
