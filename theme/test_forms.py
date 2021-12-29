""" Theme Form and Comment Form test cases """
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
                          'category': category,
                          'excerpt': 'test optional field',
                          'feature_image': 'testimg'
                          })
        self.assertTrue(form.is_valid())
    
    def test_form_is_invalid(self):
        """ Test if form is invalid """
        category = get_object_or_404(Category, slug='fiction')
        form = ThemeForm({'title': 'Test',
                          'category': 'invalid input',
                          'excerpt': 'test optional field',
                          'feature_image': 'testimg'
                          })
        self.assertFalse(form.is_valid())

    def test_title_is_required(self):
        """ Test if theme title is required """
        category = get_object_or_404(Category, slug='fiction')
        form = ThemeForm({'title': '',
                          'category': category,
                          'excerpt': 'test optional field',
                          'feature_image': 'testimg'
                          })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors[
            'title'][0], 'This field is required.')

    def test_category_is_required(self):
        """ Test if category title is required """
        form = ThemeForm({'title': 'Test',
                          'category': '',
                          'excerpt': 'test optional field',
                          'feature_image': 'testimg'
                          })
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors[
            'category'][0], 'This field is required.')

    def test_excerpt_is_optional(self):
        """ Test if excerpt is optional """
        category = get_object_or_404(Category, slug='fiction')
        form = ThemeForm({'title': 'Test',
                          'category': category,
                          'feature_image': 'testimg'
                          })
        self.assertTrue(form.is_valid())

    def test_feature_image_is_optional(self):
        """ Test if feature image is optional """
        category = get_object_or_404(Category, slug='fiction')
        form = ThemeForm({'title': 'Test',
                          'category': category,
                          'excerpt': 'test optional field'
                          })
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):
    """ Test Comment Form """

    def test_form_is_valid(self):
        """ Test if comment form is valid """
        form = CommentForm({'comment_body': '<i>Test comments</i>'})
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        """ Test if comment form is invalid """
        form = CommentForm({'comment_body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment_body', form.errors.keys())
        self.assertEqual(form.errors[
            'comment_body'][0], 'This field is required.')
