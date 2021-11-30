"""
HOME PAGE APP VIEWS
"""
from django.shortcuts import render


# Create your views here.
def index(request):
    """ simple view of the index.html """
    return render(request, 'home/index.html')
