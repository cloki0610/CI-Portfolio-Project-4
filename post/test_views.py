""" Post app views test cases """
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from home.models import Category
from theme.models import Theme
from .models import Post


class TestPostView(TestCase):
    """ Test Post apps views """

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
        self.theme = Theme.objects.create(
            title='Test1',
            author=self.user,
            category=self.category)
        self.theme.save()
        self.post = Post.objects.create(
            title='Test Post Title',
            theme=self.theme,
            excerpt='Test Excerpt',
            post_body='Test content to test post form.'
        )

    def test_get_contents(self):
        """ Test get method to render contents.html """
        response = self.client.get('/theme/test1/post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/contents.html')

    def test_get_contents_with_login(self):
        """ Test get method to render contents.html with user login """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/contents.html')

    def test_get_post_detail(self):
        """ Test get method to render post_detail.html """
        response = self.client.get('/theme/test1/post/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post_detail.html')

    def test_get_post_detail_with_login(self):
        """ Test get method to render post_detail.html with user login """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/post/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post_detail.html')

    def test_get_new_post(self):
        """ Test get method to render new_post.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/post/new_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/new_post.html')

    def test_get_new_post_redir(self):
        """ Test get method to render new_post.html without login """
        response = self.client.get('/theme/test1/post/new_post/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme' +
                             '/test1/post/new_post/')

    def test_post_new_post(self):
        """ Test post method by new_post.html """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/post/new_post/', {
            'title': 'Test Title',
            'excerpt': 'Test Excerpt',
            'post_body': 'Test content to test post form.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/post/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'New post has been created.')

    def test_post_new_post_redir(self):
        """ Test post method by new_post.html without login """
        response = self.client.post('/theme/test1/post/new_post/', {
            'title': 'Test Title',
            'excerpt': 'Test Excerpt',
            'post_body': 'Test content to test post form.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme' +
                             '/test1/post/new_post/')

    def test_post_new_post_invalid(self):
        """ Test post method by new_post.html with invalid input """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/post/new_post/', {
            'title': '*' * 201,
            'excerpt': 'Test Excerpt',
            'post_body': 'Test content to test post form.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/post/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Submit failed, Please check and Try Again!')

    def test_get_edit_post(self):
        """ Test get method to render edit_post.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/post/edit_post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/edit_post.html')

    def test_get_edit_post_redir(self):
        """ Test get method to render edit_post.html without login """
        response = self.client.get('/theme/test1/post/edit_post/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme' +
                             '/test1/post/edit_post/1/')

    def test_post_edit_post(self):
        """ Test post method by edit_post.html """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/post/edit_post/1/', {
            'title': 'Test Edit post',
            'excerpt': 'Test Edit Excerpt',
            'post_body': 'Test content to test edit post.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/post/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Your post have been successfully updated.')

    def test_post_edit_post_redir(self):
        """ Test post method by edit_post.html without login """
        response = self.client.post('/theme/test1/post/edit_post/1/', {
            'title': 'Test Edit post',
            'excerpt': 'Test Edit Excerpt',
            'post_body': 'Test content to test edit post.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme' +
                             '/test1/post/edit_post/1/')

    def test_post_edit_post_invalid(self):
        """ Test post method by edit_post.html with invalid input """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/post/edit_post/1/', {
            'title': '*' * 201,
            'excerpt': 'Test Edit Excerpt',
            'post_body': 'Test content to test edit post.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/post/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Updated failed, Please check and Try Again!')

    def test_get_confirm_delete(self):
        """ Test get method to render confirm_delete_post.html """
        self.client.login(username='test', password='password')
        response = self.client.get('/theme/test1/post/confirm_delete_post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/confirm_delete_post.html')

    def test_get_confirm_delete_redir(self):
        """
        Test get method to render confirm_delete_post.html without login
        """
        response = self.client.get('/theme/test1/post/confirm_delete_post/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme' +
                             '/test1/post/confirm_delete_post/1/')

    def test_post_delete_post(self):
        """ Test post method to delete a post """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/post/delete_post/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/post/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Selected post is successfully deleted.')

    def test_post_delete_post_redir(self):
        """ Test post method to delete a post without login """
        response = self.client.post('/theme/test1/post/delete_post/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/theme' +
                             '/test1/post/delete_post/1/')

    def test_post_delete_post_invalid(self):
        """ Test post method to delete a post with invalid primary key """
        self.client.login(username='test', password='password')
        response = self.client.post('/theme/test1/post/delete_post/16/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/theme/test1/post/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Record does not exist.')
