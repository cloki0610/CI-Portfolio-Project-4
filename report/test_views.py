""" Report Models test cases """
from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Category
from theme.models import Theme


class TestReportViews(TestCase):
    """ Test report views """

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
            title='Test1',
            author=self.user,
            category=self.category)
        self.theme.save()

    def test_get_report_form(self):
        """ Test get method to render report.html template """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/report/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/report.html')

    def test_get_report_form_redir(self):
        """ Test get method to render report.html template without login """
        response = self.client.get('/theme/test1/report/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme/test1/report/')

    def test_post_report_form(self):
        """ Test post method by ReportView to send form data """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/report/', {
            'report_type': 0,
            'email': 'test@test.com',
            'description': 'test report form'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/theme_overview.html')

    def test_post_report_form_redir(self):
        """ Test post method by ReportView to send form data without login """
        response = self.client.post('/theme/test1/report/', {
            'report_type': 0,
            'email': 'test@test.com',
            'description': 'test report form'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme/test1/report/')

    def test_post_form_invalid(self):
        """
        Test post method by ReportView to send form data with invalid input
        """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/report/', {
            'report_type': 'invalid input',
            'email': 'test@test.com',
            'description': 'test report form'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/')
