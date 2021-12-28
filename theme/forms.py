""" Create form model to leave comment on the theme overview page """
from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Comment, Theme


class ThemeForm(forms.ModelForm):
    """ Form model to add or update theme details """
    class Meta:
        """ Handle the column in form """
        model = Theme
        fields = ('title', 'category', 'excerpt', 'feature_image')
        labels = {
            'title': 'Title',
            'category': 'Category',
            'excerpt': 'Excerpt',
            'feature_image': 'Feature Image'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='mb-3', placeholder="Title"),
            Field('category', css_class='mb-3'),
            Field('excerpt', css_class='mb-3',
                  placeholder="Write some excerpt(Optional)"),
            Field('feature_image', css_class='mb-3 text-center')
        )


class CommentForm(forms.ModelForm):
    """ Form model to submit comment """
    comment_body = forms.CharField(widget=SummernoteWidget(
                                        attrs={
                                            'summernote': {
                                                'width': '100%',
                                                'height': '400px',
                                                'align-item': 'center',
                                                'placeholder': 'Comment here',
                                                'aria-label': 'Comment'
                                            }
                                        }
                                        ), label="Comment"
                                   )

    class Meta:
        """ Handle the column in form """
        model = Comment
        fields = ('comment_body',)
        labels = {
            'comment_body': 'Comment'
        }
