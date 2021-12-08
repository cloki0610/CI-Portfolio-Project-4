"""
THEME APPLICATION VIEWS
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Theme
from .forms import CommentForm, ThemeForm


class ThemeOverView(LoginRequiredMixin, View):
    """ Overview page to show the details and comments """
    def get(self, request, slug):
        """ GET method """
        theme = get_object_or_404(Theme, slug=slug)
        comments = theme.theme_comments.order_by('created_on')
        return render(
            request,
            "theme/theme_overview.html",
            {
                "theme": theme,
                "comments": comments,
                "comment_form": CommentForm(),
            })

    def post(self, request, slug):
        """ POST method """
        theme = get_object_or_404(Theme, slug=slug)
        comments = theme.theme_comments.order_by('created_on')
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
            "theme/theme_overview.html",
            {
                "theme": theme,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )


class NewThemeView(LoginRequiredMixin, View):
    """ return a page with theme form mode to add a new theme """
    def get(self, request):
        """ get method """
        theme_form = ThemeForm()
        return render(
            request,
            "theme/new_theme.html", {
                "theme_form": theme_form
            }
        )

    def post(self, request):
        """ post method """
        theme_form = ThemeForm(request.POST)
        if theme_form.is_valid():
            new_theme = theme_form.save(commit=False)
            new_theme.author = request.user
            comments = new_theme.theme_comments.order_by('created_on')
            new_theme.save()
            messages.success(request,
                             'New theme has been created. '
                             + 'Thanks your support!')
        else:
            messages.warning(request,
                             'Submit failed, Please check and Try Again!')
            return redirect(reverse('home'))
        return render(
            request,
            "theme/theme_overview.html",
            {
                "theme": new_theme,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )


class EditThemeView(LoginRequiredMixin, View):
    """ return a form model to edit a exist theme record """
    def get(self, request, slug):
        """ GET method"""
        edit_theme = get_object_or_404(Theme, slug=slug)
        theme_form = ThemeForm(instance=edit_theme)
        return render(
            request,
            "theme/edit_theme.html",
            {
                "theme_form": theme_form,
                "theme": edit_theme
            },
        )

    def post(self, request, slug):
        """ POST method """
        edit_theme = get_object_or_404(Theme, slug=slug)
        theme_form = ThemeForm(request.POST, request.FILES,
                               instance=edit_theme)
        if theme_form.is_valid():
            edited_theme = theme_form.save(commit=False)
            edited_theme.author = request.user
            edited_theme.slug = slugify(edited_theme.title)
            edited_theme.save()
            messages.success(request,
                             'Your theme has been updated.')
        else:
            messages.warning(request,
                             'Updated failed, Please check and Try Again!')
            return HttpResponseRedirect(reverse('theme_overview',
                                        args=[edit_theme.slug]))
        return HttpResponseRedirect(reverse('theme_overview',
                                    args=[edited_theme.slug]))


class DeleteTheme(LoginRequiredMixin, View):
    """ View to delete theme after confirmation """

    def post(self, request, slug):
        """ POST method """
        try:
            delete_theme = get_object_or_404(Theme, slug=slug)
            delete_theme.delete()
            messages.success(request,
                             'Your theme is successfully deleted.')
        except ObjectDoesNotExist:
            messages.error(request, "Record does not exist.")
            return redirect(reverse('home'))
        return redirect(reverse('home'))
