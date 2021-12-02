""" Profiles app view """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from cloudinary.forms import cl_init_js_callbacks
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
            profile_form.save()
        return render(
            request,
            "profiles/profile.html",
            {
                "user": user
            },
        )
