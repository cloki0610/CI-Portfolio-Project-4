""" Report Models test cases """
from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from home.models import Category


class TestReportViews(TestCase):
    """ Test report views """

    def setUp(self):
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

    def test_get_promote_request_form(self):
        """ Test get method to render report.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/promote_request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promote_request/request.html')

    def test_get_promote_request_form_redir(self):
        """ Test get method redirect to login page """
        response = self.client.get('/promote_request/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/promote_request/')

    def test_post_promote_request_form(self):
        """ Test post method to send form data """
        self.client.login(username='test', password='password')
        category = get_object_or_404(Category, slug='fiction')
        response = self.client.post('/promote_request/', {
            'category': category.pk,
            'reason': 'test promote request form'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_promote_request_form_redir(self):
        """ Test post method without login """
        category = get_object_or_404(Category, slug='fiction')
        response = self.client.post('/promote_request/', {
            'category': category.pk,
            'reason': 'test promote request form'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/promote_request/')

    def test_post_promote_request_form_invalid(self):
        """ Test post method with invalid input """
        self.client.login(username='test', password='password')
        response = self.client.post('/promote_request/', {
            'category': 'invalidinput',
            'reason': 'test promote request form'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profiles/')
