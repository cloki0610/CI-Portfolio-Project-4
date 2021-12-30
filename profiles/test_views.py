""" Profiles app views test cases """
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserProfilesForm


class TestProfilesView(TestCase):
    """ Test Profiles apps views """

    def setUp(self):
        """ Set up required instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='password',
                    email='test@example.com')
        self.user.save()

    def test_get_profile(self):
        """ Test get method to render profile.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_profile_redir(self):
        """ Test get method to render prfile.html without login """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profiles/')

    def test_get_edit_profile(self):
        """ Test get method to render edit_profile.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/profiles/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')

    def test_get_edit_profile_redir(self):
        """ Test get method to render edit_profile.html without login """
        response = self.client.get('/profiles/edit/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profiles/edit/')

    def test_post_edit_profile(self):
        """ Test post data by edit_profile.html """
        self.client.login(username='test', password='password')
        response = self.client.post('/profiles/edit/', {
            'user_icon': 'iconimg',
            'name': 'Test Display Name',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        form = UserProfilesForm({
            'user_icon': 'iconimg',
            'name': 'Test Display Name',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profiles/')

    def test_post_edit_profile_invalid(self):
        """ Test post data by edit_profile.html with invalid input"""
        self.client.login(username='test', password='password')
        response = self.client.post('/profiles/edit/', {
            'user_icon': 'iconimg',
            'name': 'teststringmorethan20characterandinputisinvalid',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        form = UserProfilesForm({
            'user_icon': 'iconimg',
            'name': 'teststringmorethan20characterandinputisinvalid',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profiles/')

    def test_post_edit_profile_redir(self):
        """ Test post data by edit_profile.html without login """
        response = self.client.post('/profiles/edit/', {
            'user_icon': 'iconimg',
            'name': 'Test Display Name',
            'location': 'United Kingdom',
            'bio': 'Test user profile form'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profiles/edit/')

    def test_get_delete_acc(self):
        """ Test get method to render delete_acc.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/profiles/delete_account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/delete_acc.html')

    def test_get_delete_acc_redir(self):
        """ Test get method to render delete_acc.html without login """
        response = self.client.get('/profiles/delete_account/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profiles/delete_account/')

    def test_post_delete_action_redir(self):
        """ Test post method to delete user without login """
        response = self.client.post('/profiles/delete_action/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profiles/delete_action/')

    def test_post_delete_action(self):
        """ Test post method to delete user without login """
        self.client.login(username='test', password='password')
        response = self.client.post('/profiles/delete_action/')
        self.assertFalse(User.objects.filter(username='test').exists())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
