""" Theme Models testsuit """
from django.test import TestCase
from .models import Theme, Comment


class TestThemeModels(TestCase):
    """ Test Theme Models """

    def test_theme_string_method(self):
        """ Test string method """
        item = Theme.objects.create(
            title='Test Theme Title',
            category='Fiction',
            excerpt="Test Excerpt")
        self.assertEqual(str(item), 'Test Theme Title')


class TestCommentModels(TestCase):
    """ Test Comment Models """

    def test_comment_string_method(self):
        """ Test string method """
        theme = Theme.objects.create(
            title='Test Theme Title',
            category='Fiction',
            excerpt="Test Excerpt")
        item = Comment.objects.create(
            comment_body='Test Comment')
        self.assertEqual(str(item), 'Comment on Test Theme Title')
