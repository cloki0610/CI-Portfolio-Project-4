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
        # return template to display user profile
        return render(
            request,
            "profiles/profile.html",
        )


class EditUserProfileView(LoginRequiredMixin, View):
    """ Return a form model to edit the profile """

    def get(self, request):
        """ get method """
        # get required form model with user profile data
        profile_form = UserProfilesForm(instance=request.user.userprofile)
        # return the form with template
        return render(
            request,
            "profiles/edit_profile.html",
            {
                "profile_form": profile_form
            },
        )

    def post(self, request):
        """post method"""
        # get the form with user input
        profile_form = UserProfilesForm(request.POST,
                                        request.FILES,
                                        instance=request.user.userprofile)
        # form validation and show the result as message
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Profile Has Updated.')
        else:
            print(profile_form.errors)
            messages.error(request,
                           'Updated Invalid, Edit and Try Again!')
        # redirect to profile page
        return redirect(reverse('profile'))


class DeleteAccount(LoginRequiredMixin, View):
    """ confirm page for delete account """

    def get(self, request):
        # return template to confirm the action
        """ get method """
        return render(
            request,
            "profiles/delete_acc.html",
        )


class DeleteAction(LoginRequiredMixin, View):
    """ View to delete account after confirmation """

    def post(self, request):
        """ POST method """
        # use try/except to remove user
        try:
            request.user.delete()
            messages.success(request,
                             'Thanks for join us and hope to see you again!')
        # if user record not exist then raise the exception
        except ObjectDoesNotExist:
            messages.error(request, "Record does not exist.")
            return redirect(reverse('home'))
        # whatever the result redirect to home page
        return redirect(reverse('home'))
