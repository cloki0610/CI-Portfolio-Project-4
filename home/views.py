"""
HOME APPLICATION VIEWS
"""
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Count
from theme.models import Theme
from .models import Category


class HomePage(View):
    """ List all the theme from latest to oldest """
    def get(self, request):
        """ GET method """
        # get the required data
        all_theme = Theme.objects.all().order_by('-updated_on')
        top_theme = Theme.objects.annotate(most_upvote=Count('upvote')) \
                         .order_by('-most_upvote')[:3]
        # use paginator to manage the result
        theme_paginator = Paginator(all_theme, 10)
        page_number = request.GET.get('page')
        theme_page = theme_paginator.get_page(page_number)

        # return data with template
        return render(
            request,
            "home/index.html",
            {
                "theme_page": theme_page,
                "top_theme": top_theme
            }
        )


class CategoryView(View):
    """ List all the theme in the category """
    def get(self, request, category_slug):
        """ GET method """
        # get the list of required data
        category = get_object_or_404(Category, slug=category_slug)
        themes = category.category_theme.order_by('-updated_on')

        # use paginator to manage the result
        theme_paginator = Paginator(themes, 10)
        page_number = request.GET.get('page')
        theme_page = theme_paginator.get_page(page_number)

        # return data with template
        return render(
            request,
            "home/category.html",
            {
                "category": category,
                "theme_page": theme_page
            }
        )
