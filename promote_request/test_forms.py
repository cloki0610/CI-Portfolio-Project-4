""" Promote Request Form test cases """
from django.test import TestCase
from django.shortcuts import get_object_or_404
from home.models import Category
from .forms import PromoteRequestForm


class TestPromoteRequestForms(TestCase):
    """ Test report form model """

    def setUp(self):
        """ Set up required instance """
        self.category = Category.objects.create(
            name='Fiction',
            introduction='testonly'
        )
        self.category.save()

    def test_form_is_valid(self):
        """ Test form model with a valid input """
        category = get_object_or_404(Category, slug='fiction')
        form = PromoteRequestForm({
            'category': category.pk,
            'reason': 'test promote request form'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_input(self):
        """ Test form model with an invalid input """
        form = PromoteRequestForm({
            'category': 'invalid input',
            'reason': 'test promote request form'
        })
        self.assertFalse(form.is_valid())

    def test_category_is_reuqired(self):
        """ Test if category is required """
        form = PromoteRequestForm({
            'category': '',
            'reason': 'test promote request form'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors[
            'category'][0], 'This field is required.')

    def test_description_is_reuqired(self):
        """ Test if reason field is required """
        category = get_object_or_404(Category, slug='fiction')
        form = PromoteRequestForm({
            'category': category.pk,
            'reason': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('reason', form.errors.keys())
        self.assertEqual(form.errors[
            'reason'][0], 'This field is required.')
