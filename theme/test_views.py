""" Theme app views test cases """
from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from home.models import Category
from .models import Theme


class TestThemeView(TestCase):
    """ Test Theme apps views """

    def setUp(self):
        """ Set up required instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='password',
                    email='test@example.com')
        self.user.save()
        self.user.userprofile.membership = 1
        self.user.save()
        self.category = Category.objects.create(
            name='Fiction',
            introduction='testonly'
        )
        self.category.save()
        self.theme = Theme.objects.create(
            title='Test1',
            author=self.user,
            category=self.category)
        self.theme.save()

    def test_get_theme_overview(self):
        """
        Test get method to render theme_overview.html template without login
        """
        response = self.client.get('/theme/test1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/theme_overview.html')

    def test_get_theme_overview_with_login(self):
        """ Test get method to render theme_overview.html template """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/theme_overview.html')

    def test_post_theme_overview_comment(self):
        """ Test post method by ThemeOverView to post a comment """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/', {
            'comment_body': '<i>Test comments</i>'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/theme_overview.html')

    def test_post_theme_overview_comment_no_login(self):
        """
        Test post method by ThemeOverView to post a comment without login
        """
        response = self.client.post('/theme/test1/', {
            'comment_body': '<i>Test comments</i>'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/theme/test1/')

    def test_get_edit_theme(self):
        """ Test get method to render edit_theme.html template """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/edit_theme/test1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/edit_theme.html')

    def test_get_edit_theme_redir(self):
        """
        Test get method to render edit_theme.html template without login
        """
        response = self.client.get('/theme/edit_theme/test1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme/edit_theme/test1/')

    def test_post_edit_theme(self):
        """ Test post method by EditThemeView to send form data """
        self.client.login(username='test', password='password')
        category = get_object_or_404(Category, slug='fiction')
        response = self.client.post('/theme/edit_theme/test1/', {
            'title': 'Testedited',
            'category': category.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/testedited/')

    def test_post_edit_theme_invalid(self):
        """
        Test post method by EditThemeView to send form data with invalid input
        """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/edit_theme/test1/', {
            'title': 'Testedited',
            'category': 'invalid input'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/')

    def test_post_edit_theme_redir(self):
        """
        Test post method by EditThemeView to send form data without login
        """
        category = get_object_or_404(Category, slug='fiction')
        response = self.client.post('/theme/edit_theme/test1/', {
            'title': 'Testedited',
            'category': category.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme/edit_theme/test1/')

    def test_get_new_theme(self):
        """ Test get method to render new_theme.html template """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/new_theme/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/new_theme.html')

    def test_get_new_theme_redir(self):
        """ Test get method to render new_theme.html template without login """
        response = self.client.get('/theme/new_theme/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme/new_theme/')

    def test_post_new_theme(self):
        """  Test post method by NewThemeView to send form data """
        self.client.login(username='test', password='password')
        category = get_object_or_404(Category, slug='fiction')
        response = self.client.post('/theme/new_theme/', {
            'title': 'Test2',
            'category': category.pk
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme/theme_overview.html')

    def test_post_new_theme_invalid(self):
        """
        Test post method by NewThemeView to send form data with invalid input
        """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/new_theme/', {
            'title': 'Test2',
            'category': 'invalid input'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_post_new_theme_redir(self):
        """
        Test post method by NewThemeView to send form data without login
        """
        category = get_object_or_404(Category, slug='fiction')
        response = self.client.post('/theme/new_theme/', {
            'title': 'Test2',
            'category': category.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme/new_theme/')

    def test_upvote_view(self):
        """ Test ThemeUpvote view """
        theme = get_object_or_404(Theme, slug="test1")
        self.client.login(username='test', password='password')
        url = '/theme/theme_upvote/' + str(theme.pk) + '/'
        response = self.client.post(url, {
            'theme_pk': theme.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/')

    def test_downvote_view(self):
        """ Test Themedownvote view """
        theme = get_object_or_404(Theme, slug="test1")
        self.client.login(username='test', password='password')
        url = '/theme/theme_downvote/' + str(theme.pk) + '/'
        response = self.client.post(url, {
            'theme_pk': theme.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/')

    def test_delete_view(self):
        """ Test DeleteTheme view """
        theme = get_object_or_404(Theme, slug="test1")
        self.client.login(username='test', password='password')
        url = '/theme/delete_theme/' + str(theme.slug) + '/'
        response = self.client.post(url, {
            'slug': theme.slug
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
