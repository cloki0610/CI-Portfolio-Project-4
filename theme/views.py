"""
THEME APPLICATION VIEWS
"""
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Theme
from .forms import CommentForm


class ThemeOverView(LoginRequiredMixin, View):
    """ Overview page to show the details and comments """
    def get(self, request, slug, *args, **kwargs):
        """ GET method """
        theme = get_object_or_404(Theme, slug=slug)
        comments = theme.theme_comments.order.order_by('created_on')
        return render(
            request,
            "theme_overview.html",
            {
                "theme": theme,
                "comments": comments,
                "comment_form": CommentForm(),
            })

    def post(self, request, slug, *args, **kwargs):
        """ POST method """
        theme = get_object_or_404(Theme, slug=slug)
        comments = theme.theme_comments.order.order_by('created_on')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.theme = theme
            comment.save()
            messages.success(request,
                             'Your Comment is successfully submit.')
        else:
            comment_form = CommentForm()
            messages.error(request,
                           'Error, please contact admin or try again.')

        return render(
            request,
            "theme_overview.html",
            {
                "theme": theme,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
