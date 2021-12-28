""" Theme Form and Comment Form testsuit """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from home.models import Category
from .models import Theme
from .forms import ThemeForm, CommentForm


class TestThemeForm(TestCase):
    """ Test Theme app's form model """

    def setUp(self):
        """Set up test user and category instance """
        self.category = Category.objects.create(
            name='Fiction',
            introduction='testonly'
        )
        self.category.save()

    def test_form_is_valid(self):
        """ Test if form is valid """
        category = get_object_or_404(Category, slug='fiction')
        form = ThemeForm({'title': 'Test',
                          'category': category})
        self.assertTrue(form.is_valid())

    def test_title_is_required(self):
        """ Test if theme title is required """
        category = get_object_or_404(Category, slug='fiction')
        form = ThemeForm({'title': '',
                          'category': category})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors[
            'title'][0], 'This field is required.')

    def test_category_is_required(self):
        """ Test if category title is required """
        form = ThemeForm({'title': 'Test',
                          'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors[
            'category'][0], 'This field is required.')


class TestCommentForm(TestCase):
    """ Test Comment Form """

    def setUp(self):
        """Set up test user and instance will use for testing """
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

    def test_form_is_valid(self):
        """ Test if form is valid """
        user = get_object_or_404(User, username='test')
        theme = get_object_or_404(Theme, slug="test2")
        form = CommentForm({'theme': theme,
                            'user': user,
                            'comment_body': '<i>Test comments</i>'})
        self.assertTrue(form.is_valid())
