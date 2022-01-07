""" Home app views test cases """
from django.test import TestCase
from django.contrib.auth.models import User
from theme.models import Theme
from .models import Category


class TestHomeView(TestCase):
    """ Test home apps views """
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

    def test_get_index(self):
        """ Test get method to render index.html template """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_index_with_login(self):
        """ Test get method to render index.html template with login """
        self.client.login(username='test', password='password')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_category(self):
        """ Test get method to render category.html template """
        response = self.client.get('/fiction')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/category.html')

    def test_get_category_with_login(self):
        """ Test get method to render category.html template with login """
        response = self.client.get('/fiction')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/category.html')

    def test_get_error_404(self):
        """ Test a invalid link to error 404 page """
        response = self.client.get('/invalidurl')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
