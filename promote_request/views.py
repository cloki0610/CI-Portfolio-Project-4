"""
PROMOTE REQUEST APPLICATION VIEWS
"""
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PromoteRequestForm


class PromoteRequestView(LoginRequiredMixin, View):
    """ Return a form model to subit request """

    def get(self, request):
        """ get method """
        request_form = PromoteRequestForm()
        return render(
            request,
            "promote_request/request.html", {
                "request_form": request_form
            })

    def post(self, request):
        """ post method """
        request_form = PromoteRequestForm(request.POST)
        if request_form.is_valid():
            promote_request = request_form.save(commit=False)
            promote_request.user = request.user
            promote_request.save()
            messages.success(request,
                             'Form submited, please wait for approved')
        else:
            messages.warning(request,
                             'Invalid input, Please check and Try Again!')
        return render(
            request,
            "profiles/profile.html",
        )
