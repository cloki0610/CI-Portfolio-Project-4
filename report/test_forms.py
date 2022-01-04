""" Report Form test cases """
from django.test import TestCase
from .forms import ReportForm


class TestReportForms(TestCase):
    """ Test report form model """

    def test_form_is_valid(self):
        """ Test form model with a valid input """
        form = ReportForm({
            'report_type': 0,
            'email': 'test@test.com',
            'description': 'test report form'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_input(self):
        """ Test form model with an invalid input """
        form = ReportForm({
            'report_type': 'invalidinput',
            'description': 'test report form'
        })
        self.assertFalse(form.is_valid())

    def test_report_type_is_reuqired(self):
        """ Test if report_type is required """
        form = ReportForm({
            'report_type': '',
            'email': 'test@test.com',
            'description': 'test without report_type'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('report_type', form.errors.keys())
        self.assertEqual(form.errors[
            'report_type'][0], 'This field is required.')

    def test_description_is_reuqired(self):
        """ Test if description is required """
        form = ReportForm({
            'report_type': 0,
            'email': 'test@test.com',
            'description': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors[
            'description'][0], 'This field is required.')

    def test_email_is_optional(self):
        """ Test if email is optional """
        form = ReportForm({
            'report_type': 0,
            'description': 'test report form'
        })
        self.assertTrue(form.is_valid())
