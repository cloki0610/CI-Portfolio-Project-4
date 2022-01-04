""" Category Model test cases """
from django.test import TestCase
from .models import Category


class TestCategoryModel(TestCase):
    """ Test Category data model """

    def test_category_string_method(self):
        """ Test string method in data model """
        category_obj = Category.objects.create(
            name='Test Category',
            introduction='Test category introduction'
            )
        self.assertEqual(str(category_obj), 'Test Category')

    def test_category_presave_slug(self):
        """ Test default slug when instance created """
        category_obj = Category.objects.create(
            name='Test Category',
            introduction='Test category introduction'
            )
        self.assertEqual(category_obj.slug, 'test-category')
