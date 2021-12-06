""" Manage Theme and Comment Model display in admin site """
from django.contrib import admin
from .models import Theme, Comment


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    """ Show model in admin table with follow rules"""
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'category', 'created_on', 'updated_on')
    list_display = ('title', 'author', 'created_on', 'updated_on')
    search_fields = ['title', 'excerpt']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Show model in admin table with follow rules"""
    list_filter = ('theme', 'user', 'created_on', 'updated_on')
    list_display = ('theme', 'user', 'created_on', 'updated_on')
    search_fields = ['theme', 'user', 'comment_body']
