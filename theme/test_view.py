""" Theme app views testsuit """
from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Category
from .models import Theme

class TestThemeView(TestCase):
    """ Test Theme apps views """

    def setUp(self):
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

    def test_theme_overview(self):
        """ test theme_overview.html template rendering """
        response = self.client.get('/theme/test2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme_ovewview.html')

    # def test_edit_theme(self):

    # def test_edit_theme_redir(self):

    # def test_new_theme(self):

    # def test_new_theme_redir(self):