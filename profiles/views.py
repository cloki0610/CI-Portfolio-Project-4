"""
PROFILES APPLICATION VIEWS
"""
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserProfilesForm


class UserProfileView(LoginRequiredMixin, View):
    """ Return the data to view the user profile"""

    def get(self, request):
        """ get method """
        return render(
            request,
            "profiles/profile.html",
        )


class EditUserProfileView(LoginRequiredMixin, View):
    """ Return a form model to edit the profile """

    def get(self, request):
        """ get method """
        profile_form = UserProfilesForm(instance=request.user.userprofile)
        return render(
            request,
            "profiles/edit_profile.html",
            {
                "profile_form": profile_form
            },
        )

    def post(self, request):
        """post method"""
        profile_form = UserProfilesForm(request.POST,
                                        request.FILES,
                                        instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Profile Has Updated.')
        else:
            print(profile_form.errors)
            messages.error(request,
                           'Updated Invalid, Edit and Try Again!')
        return redirect(reverse('profile'))


class DeleteAccount(LoginRequiredMixin, View):
    """ confirm page for delete account """

    def get(self, request):
        """ get method """
        return render(
            request,
            "profiles/delete_acc.html",
        )


class DeleteAction(LoginRequiredMixin, View):
    """ View to delete account after confirmation """

    def post(self, request):
        """ POST method """
        try:
            request.user.delete()
            messages.success(request,
                             'Thanks for join us and hope to see you again!')
        except ObjectDoesNotExist:
            messages.error(request, "Record does not exist.")
            return redirect(reverse('home'))
        return redirect(reverse('home'))
