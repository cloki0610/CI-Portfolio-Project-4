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

    def approved_requests(self, request, queryset):
        """ Action to mark the request as approved """
        queryset.update(approved=True)

    def reset_approve_status(self, request, queryset):
        """ Action to reset the approved status """
        queryset.update(approved=False)
