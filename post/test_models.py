""" Post Model test cases """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from home.models import Category
from theme.models import Theme
from .models import Post


class TestPostModels(TestCase):
    """ Test Post app's models """

    def setUp(self):
        """Set up required instance """
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
            title='TestPost',
            author=self.user,
            category=self.category)
        self.theme.save()

    def test_post_string_method(self):
        """ Test string method """
        theme = get_object_or_404(Theme, slug='testpost')
        post_obj = Post.objects.create(
            title='Test1',
            theme=theme,
            post_body='Test post model only',
            excerpt='create for test post')
        self.assertEqual(str(post_obj), 'Test1 of TestPost')
