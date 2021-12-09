""" Create form model to display report form """
from django import forms
from django_summernote.widgets import SummernoteWidget
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
