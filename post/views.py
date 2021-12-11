"""
POST APPLICATION VIEWS
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from theme.models import Theme
from .models import Post
from .forms import PostForm


class ContentsView(generic.ListView):
    """ Content page display all post of the theme """
    model = Post
    template_name = 'post/contents.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        """ Queryset to get the query with argument """
        post = self.model.objects.all()
        if self.kwargs.get('slug'):
            theme = get_object_or_404(Theme, slug=self.kwargs['slug'])
            post = post.filter(theme=theme).order_by('-publish_on')

        return post

    def get_theme(self, *args, **kwargs):
        """ get the theme slug for return to overview page"""
        return get_object_or_404(Theme, slug=self.kwargs['slug'])


class PostDetailView(View):
    """ Page to disply full content of the post """
    def get(self, request, slug, post_pk):
        """ GET method """
        theme = get_object_or_404(Theme, slug=slug)
        post = get_object_or_404(Post, pk=post_pk)
        return render(
            request,
            "post/post_detail.html",
            {
                "theme": theme,
                "post": post
            }
        )


class NewPostView(LoginRequiredMixin, View):
    """ View to add a new post to the theme last visit """
    def get(self, request, slug):
        """ get method """
        theme = get_object_or_404(Theme, slug=slug)
        post_form = PostForm()
        return render(
            request,
            "post/new_post.html", {
                "post_form": post_form,
                "theme": theme,
            }
        )

    def post(self, request, slug):
        """ POST method """
        theme = get_object_or_404(Theme, slug=slug)
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.theme = theme
            new_post.save()
            messages.success(request,
                             'New post has been created.')
        else:
            messages.error(request,
                           'Submit failed, Please check and Try Again!')
        return HttpResponseRedirect(reverse('contents',
                                    args=[theme.slug]))


class EditPostView(LoginRequiredMixin, View):
    """ View to add a new post to the theme last visit """
    def get(self, request, slug, post_pk):
        """ GET method """
        theme = get_object_or_404(Theme, slug=slug)
        edit_post = get_object_or_404(Post, pk=post_pk)
        post_form = PostForm(instance=edit_post)
        return render(
            request,
            "post/edit_post.html",
            {
                "post_form": post_form,
                "theme": theme,
                "post": edit_post
            },
        )

    def post(self, request, slug, post_pk):
        """ POST method """
        theme = get_object_or_404(Theme, slug=slug)
        edit_post = get_object_or_404(Post, pk=post_pk)
        post_form = PostForm(request.POST, instance=edit_post)
        if post_form.is_valid():
            edited_post = post_form.save(commit=False)
            edited_post.theme = theme
            edited_post.save()
            messages.success(request,
                             'Your post have been successfully updated.')
        else:
            messages.error(request,
                           'Updated failed, Please check and Try Again!')
        return HttpResponseRedirect(reverse('contents',
                                    args=[theme.slug]))


class DeletePost(LoginRequiredMixin, View):
    """ View to delete post after confirmation """

    def post(self, request, slug, post_pk):
        """ POST method """
        try:
            theme = get_object_or_404(Theme, slug=slug)
            delete_post = get_object_or_404(Post, pk=post_pk)
            delete_post.delete()
            messages.success(request,
                             'Selected post is successfully deleted.')
        except ObjectDoesNotExist:
            messages.error(request, "Record does not exist.")
        return HttpResponseRedirect(reverse('contents',
                                    args=[theme.slug]))
