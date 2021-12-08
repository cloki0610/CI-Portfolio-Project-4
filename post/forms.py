""" Create form model to leave comment on the theme overview page """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    """ Form model to add or update post """
    post_body = forms.CharField(widget=SummernoteWidget(
                                    attrs={
                                        'summernote': {
                                            'width': '100%',
                                            'height': '400px',
                                            'align-item': 'center'
                                        }
                                    }
                                    )
                                )

    class Meta:
        """ Form model to submit comment """
        model = Post
        fields = ('title', 'excerpt', 'post_body')
