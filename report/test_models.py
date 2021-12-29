""" Report Models test cases """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from home.models import Category
from theme.models import Theme
from .models import Report


class TestReportModels(TestCase):
    """ Test report models """
    def setUp(self):
        """ Set up required instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='password',
                    email='test@example.com')
        self.user.save()
        self.category = Category.objects.create(
            name='Fiction',
            introduction='testonly'
        )
        self.category.save()
        self.theme = Theme.objects.create(
            title='Test3',
            author=self.user,
            category=self.category)
        self.theme.save()

    def test_report_string_method(self):
        """ Test report model's string method """
        user = User.objects.get(username="test")
        theme = get_object_or_404(Theme, slug='test3')
        report_obj = Report.objects.create(
            user=user,
            theme=theme,
            email='email@test.com',
            report_type=1,
            description='test report model'
        )
        self.assertEqual(str(report_obj), 'Report from test')
