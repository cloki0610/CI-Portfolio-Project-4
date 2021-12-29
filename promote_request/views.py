"""
PROMOTE REQUEST APPLICATION VIEWS
"""
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PromoteRequestForm


class PromoteRequestView(LoginRequiredMixin, View):
    """ Return a form model to submit request """

    def get(self, request):
        """ get method """
        # get required form model
        request_form = PromoteRequestForm()
        # return form model with template
        return render(
            request,
            "promote_request/request.html", {
                "request_form": request_form
            }
        )

    def post(self, request):
        """ post method """
        # get form model and fill the form with user input
        request_form = PromoteRequestForm(request.POST)
        # form validation
        if request_form.is_valid():
            promote_request = request_form.save(commit=False)
            promote_request.user = request.user
            promote_request.save()
            messages.success(request,
                             'Form submited, please wait for approved')
        else:
            # if input invalid, show error message and redirect to profile page
            messages.error(request,
                           'Submit failed, Please check and Try Again!')
            return HttpResponseRedirect(reverse('profile'))
        # return to profile page if success
        return render(
            request,
            "profiles/profile.html",
        )
