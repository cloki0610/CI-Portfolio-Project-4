""" Profiles app view """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserProfilesForm


class UserProfileView(LoginRequiredMixin, View):
    """ Return the data to view the user profile"""

    def get(self, request, user, *args, **kwargs):
        """ get method """
        user = get_object_or_404(User, username=user)
        return render(
            request,
            "profiles/profile.html",
            {
                "user": user
            },
        )


class EditUserProfileView(LoginRequiredMixin, View):
    """ Return a form model to edit the profile """

    def get(self, request, user, *args, **kwargs):
        """ get method """
        user = get_object_or_404(User, username=user)
        profile_form = UserProfilesForm(instance=user.userprofile)
        return render(
            request,
            "profiles/edit_profile.html",
            {
                "profile_form": profile_form
            },
        )

    def post(self, request, user, *args, **kwargs):
        """post method"""
        user = get_object_or_404(User, username=user)
        profile_form = UserProfilesForm(request.POST,
                                        request.FILES,
                                        instance=user.userprofile)
        if profile_form.is_valid():
            messages.success(request, 'Your Profile Has Updated.')
            profile_form.save()
        else:
            messages.warning(request,
                             'Updated Invalid, Edit and Try Again!')
        return render(
            request,
            "profiles/profile.html",
            {
                "user": user
            },
        )


class DeleteAccount(LoginRequiredMixin, View):
    """ confirm page for delete account """

    def get(self, request, user, *args, **kwargs):
        """ get method """
        user = get_object_or_404(User, username=user)
        return render(
            request,
            "profiles/delete_acc.html",
            {
                "user": user
            },
        )


class DeleteAction(LoginRequiredMixin, View):
    """ View to delete account after confirmation """

    def get(self, request, user, *args, **kwargs):
        """ get method """
        user = get_object_or_404(User, username=user)
        user.delete()
        messages.success(request,
                         'Thanks for join us and hope to see you again!')
        return redirect(reverse('home'))
