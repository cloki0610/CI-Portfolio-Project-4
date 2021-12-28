""" Theme Models testsuit """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from home.models import Category
from .models import Theme, Comment


class TestThemeModels(TestCase):
    """ Test Theme app's models """

    def setUp(self):
        """Set up test user and category instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='12test12',
                    email='test@example.com')
        self.user.save()
        self.category = Category.objects.create(
            name='Fiction',
            introduction='testonly'
        )
        self.category.save()
        self.comment_theme = Theme.objects.create(
            title='Test2',
            author=self.user,
            category=self.category)
        self.comment_theme.save()

    def test_theme_string_method(self):
        """ Test string method """
        category = get_object_or_404(Category, slug='fiction')
        user = User.objects.get(username="test")
        theme_obj = Theme.objects.create(
            title='Test1',
            author=user,
            category=category)
        self.assertEqual(str(theme_obj), 'Test1')

    def test_comment_string_method(self):
        """ Test string method """
        user = User.objects.get(username="test")
        theme = get_object_or_404(Theme, slug='test2')
        comment_obj = Comment.objects.create(
            theme=theme,
            user=user,
            comment_body='Test Comment')
        self.assertEqual(str(comment_obj), 'Comment on Test2')

    def test_default_slug(self):
        """ Test default slug """
        category = get_object_or_404(Category, slug='fiction')
        user = User.objects.get(username="test")
        theme_obj = Theme.objects.create(
            title='Test Theme Title',
            author=user,
            category=category
            )
        self.assertEqual(theme_obj.slug, 'test-theme-title')
