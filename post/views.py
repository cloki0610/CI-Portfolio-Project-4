"""
POST APPLICATION VIEWS
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from theme.models import Theme
from .models import Post
from .forms import PostForm


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
            messages.warning(request,
                             'Submit failed, Please check and Try Again!')
        return HttpResponseRedirect(reverse('theme_overview',
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
            edited_post.slug = slugify(edited_post.title)
            edited_post.save()
            messages.success(request,
                             'Your post have been successfully updated.')
        else:
            messages.warning(request,
                             'Updated failed, Please check and Try Again!')
        return HttpResponseRedirect(reverse('theme_overview',
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
                             'Your theme is successfully deleted.')
        except ObjectDoesNotExist:
            messages.error(request, "Record does not exist.")
            return HttpResponseRedirect(reverse('theme_overview',
                                        args=[theme.slug]))
        return HttpResponseRedirect(reverse('theme_overview',
                                    args=[theme.slug]))
