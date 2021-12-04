""" Promote Request Model display in admin site """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PromoteRequest


@admin.register(PromoteRequest)
class PromoteRequestAdmin(SummernoteModelAdmin):
    """ Show model in admin table with follow rules"""
    summernote_fields = ('reason')
    list_filter = ('user', 'category')
    list_display = ('user', 'category', 'submit_on')
    search_fields = ['user', 'reason']
