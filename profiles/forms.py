""" Create form model to display a form """
from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import UserProfile


class UserProfilesForm(forms.ModelForm):
    """ Form model to let user modify his own profile """
    bio = forms.CharField(widget=SummernoteWidget(attrs={
                                        'summernote': {
                                            'width': '100%',
                                            'height': '400px',
                                            'align-item': 'center',
                                            'placeholder': 'Write Bio here'
                                        }
                                    }
                                ), label="Bio", required=False
                          )

    class Meta:
        """ Handle the column in form"""
        model = UserProfile
        fields = ('user_icon', 'name', 'location', 'bio')
        labels = {
            'user_icon': 'User Icon',
            'name': 'Display Name',
            'location': 'User Location',
            'bio': 'Bio'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('user_icon', css_class="mb-3"),
            Field('name', css_class="mb-3"),
            Field('location', css_class="mb-3"),
            Field('bio', css_class="mb-3")
        )
