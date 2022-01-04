""" Post Form test cases """
from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):
    """ Test Post app's form model """

    def test_form_is_valid(self):
        """ Test form model with a valid input """
        form = PostForm({
            'title': 'Test Title',
            'excerpt': 'Test Excerpt',
            'post_body': 'Test content to test post form.'
        })
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        """ Test form model with an invalid input """
        form = PostForm({
            'title': '*' * 201,
            'excerpt': 'Test Excerpt',
            'post_body': 'Test content to test post form.'
        })
        self.assertFalse(form.is_valid())

    def test_title_is_required(self):
        """ Test if title field is required """
        form = PostForm({
            'title': '',
            'excerpt': 'Test Excerpt',
            'post_body': 'Test content to test post form.'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors[
            'title'][0], 'This field is required.')

    def test_excerpt_is_optional(self):
        """ Test if excerpt field is optional """
        form = PostForm({
            'title': 'Test PostForm Title',
            'excerpt': '',
            'post_body': 'Test content to test post form.'
        })
        self.assertTrue(form.is_valid())

    def test_post_body_is_required(self):
        """ Test if post_body field is required """
        form = PostForm({
            'title': 'Test PostForm Title',
            'excerpt': 'Test Excerpt',
            'post_body': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('post_body', form.errors.keys())
        self.assertEqual(form.errors[
            'post_body'][0], 'This field is required.')
