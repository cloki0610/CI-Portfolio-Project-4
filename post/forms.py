""" Create form model to leave comment on the theme overview page """
from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
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
        labels = {
            'title': 'Post Title',
            'excerpt': 'Post Excerpt',
            'post_body': 'Contents'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class="mb-3"),
            Field('excerpt', css_class="mb-3"),
            Field('post_body', css_class="mb-3")
        )
