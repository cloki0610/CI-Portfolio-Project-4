from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    """ A view to return the data required user profile"""
    model = User
    template_name = 'profiles/profile.html'

    def get_object(self):
        pass
