from django.contrib import admin
from .models import Category
from theme.models import Theme


class ThemeInline(admin.TabularInline):
    model = Theme


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'introduction')
    search_fields = ['name']
    inlines = [ThemeInline]
