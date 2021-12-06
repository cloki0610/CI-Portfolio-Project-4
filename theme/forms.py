""" Create form model to leave comment on the theme overview page """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Form model to submit comment """
    comment_body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        """ Handle the column in form """
        model = Comment
        fields = ('comment_body',)
