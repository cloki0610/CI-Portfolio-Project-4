"""
HOME APPLICATION VIEWS
"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from theme.models import Theme
from .models import Category


class index(generic.ListView):
    """ List all the theme from latest to oldest """
    model = Theme
    query_set = Theme.objects.all().order_by('-updated_on')
    template_name = 'home/index.html'
    paginate_by = 10


class CategoryView(View):
    """ List all the theme in the category """
    def get(self, request, category_slug):
        """ GET method """
        category = get_object_or_404(Category, slug=category_slug)
        themes = category.category_theme.order_by('-updated_on')
        theme_paginator = Paginator(themes, 10) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        theme_page = theme_paginator.get_page(page_number)
        return render(
            request,
            "home/category.html",
            {
                "category": category,
                "theme_page": theme_page
            }
        )
