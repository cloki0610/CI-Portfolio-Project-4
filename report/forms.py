""" Create form model to display report form """
from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Report


class ReportForm(forms.ModelForm):
    """ Form model to let user submit a report form """
    description = forms.CharField(widget=SummernoteWidget(attrs={
                                        'summernote': {
                                            'width': '100%',
                                            'height': '400px',
                                            'align-item': 'center'
                                        }
                                    }
                            ))

    class Meta:
        """ Handle the column in form """
        model = Report
        fields = ('report_type', 'description', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('report_type', css_class="mb-3"),
            Field('description', css_class="mb-3"),
            Field('email', css_class="mb-3",
                  placeholder="Your contact email(Optional)")
        )
