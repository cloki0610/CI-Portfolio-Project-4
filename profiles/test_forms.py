""" User Profile Form test cases """
from django.test import TestCase
from .forms import UserProfilesForm


class TestUserProfileForm(TestCase):
    """ Test Theme app's form model """

    def test_form_is_valid(self):
        """ Test if the form input is valid"""
        form = UserProfilesForm({
            'user_icon': 'iconimg',
            'name': 'Test Display Name',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        """ Test if the form input is invalid """
        form = UserProfilesForm({
            'user_icon': 'iconimg',
            'name': 'teststringmorethan20characterandinputisinvalid',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        self.assertFalse(form.is_valid())

    def test_user_icon_is_optional(self):
        """ Test if the user_icon is optional """
        form = UserProfilesForm({
            'user_icon': '',
            'name': 'Test Display Name',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        self.assertTrue(form.is_valid())

    def test_name_is_optional(self):
        """ Test if the name is optional """
        form = UserProfilesForm({
            'user_icon': 'iconimg',
            'name': '',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        self.assertTrue(form.is_valid())

    def test_location_is_optional(self):
        """ Test if the location is optional """
        form = UserProfilesForm({
            'user_icon': 'iconimg',
            'name': 'Test Display Name',
            'location': '',
            'bio': 'Test user profile form'
        })
        self.assertTrue(form.is_valid())

    def test_bio_is_optional(self):
        """ Test if the user bio is optional """
        form = UserProfilesForm({
            'user_icon': 'iconimg',
            'name': 'Test Display Name',
            'location': 'United Kingdom',
            'bio': ''
        })
        self.assertTrue(form.is_valid())
