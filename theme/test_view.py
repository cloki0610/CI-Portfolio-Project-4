""" Theme app views testsuit """
from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from home.models import Category
from .models import Theme


class TestThemeView(TestCase):
    """ Test Theme apps views """

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
        self.theme = Theme.objects.create(
            title='Test1',
            author=self.user,
            category=self.category)
        self.theme.save()

    def test_get_theme_overview(self):
        """ test get theme_overview.html without login """
        response = self.client.get('/theme/test1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/theme_overview.html')

    def test_get_theme_overview_no_login(self):
        """ test get theme_overview.html with login """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/theme_overview.html')

    def test_post_theme_overview(self):
        """ test to post a comment """
        user = get_object_or_404(User, username='test')
        theme = get_object_or_404(Theme, slug="test1")
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/', {
            'theme': theme,
            'user': user,
            'comment_body': '<i>Test comments</i>'
        })
        self.assertEqual(response.status_code, 200)

    def test_edit_theme(self):
        """ test to get edit_theme.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/edit_theme/test1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/edit_theme.html')

    def test_edit_theme_redir(self):
        """ test edit_theme view redirect when user not login"""
        response = self.client.get('/theme/edit_theme/test1/')
        self.assertEqual(response.status_code, 302)

    def test_new_theme(self):
        """ test to get new_theme.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/new_theme/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/new_theme.html')

    def test_new_theme_redir(self):
        """ test new_theme view redirect when user not login"""
        response = self.client.get('/theme/edit_theme/test1/')
        self.assertEqual(response.status_code, 302)
