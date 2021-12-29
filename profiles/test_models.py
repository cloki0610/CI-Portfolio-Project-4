""" UserProfile Models test cases """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import UserProfile


class TestProfilesModels(TestCase):
    """ Test profiles app's models """

    def setUp(self):
        """Set up test user instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='password',
                    email='test@example.com')
        self.user.save()

    def test_auto_create_and_string_method(self):
        """
        Test profile create correctly when user create
        and display by string method
        """
        profile = get_object_or_404(UserProfile, user=1)
        self.assertEqual(str(profile), 'test')
