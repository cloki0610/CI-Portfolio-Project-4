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
        category = get_object_or_404(Category, name=category_slug)
        themes = category.category_theme.order_by('-updated_on')
        paginator = Paginator(themes, 25) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "home/category.html",
            {
                "category": category,
                "page_obj": page_obj
            }
        )
