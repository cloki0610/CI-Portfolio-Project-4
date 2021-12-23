""" Create form model to display request form to become creator """
from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import PromoteRequest


class PromoteRequestForm(forms.ModelForm):
    """ Form model to let user submit a request form """
    reason = forms.CharField(widget=SummernoteWidget(attrs={
                                        'summernote': {
                                            'width': '100%',
                                            'height': '400px',
                                            'align-item': 'center',
                                            'placeholder': 'Write here'
                                        }
                                    }
                                ), label="Explain reason"
                             )

    class Meta:
        """ Handle the column in form """
        model = PromoteRequest
        fields = ('category', 'reason')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('category', css_class="mb-3"),
            Field('reason', css_class="mb-3")
        )
