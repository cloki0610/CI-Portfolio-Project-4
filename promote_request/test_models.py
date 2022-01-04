""" Promote Request Models test cases """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from home.models import Category
from .models import PromoteRequest


class TestPromoteRequestModels(TestCase):
    """ Test promote request models """
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

    def test_promote_request_string_method(self):
        """ Test string method in data model """
        user = User.objects.get(username="test")
        category = get_object_or_404(Category, slug='fiction')
        promote_request_obj = PromoteRequest.objects.create(
            user=user,
            category=category,
            reason='test promote request model'
        )
        self.assertEqual(str(promote_request_obj), 'Promote Request from test')
