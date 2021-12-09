from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """ Show model in admin table with follow rules"""
    list_filter = ('user', 'theme', 'report_type')
    list_display = ('user', 'theme', 'submit_on')
    search_fields = ['user', 'theme', 'description']

    def checked_report(self, request, queryset):
        """ Action to mark the request as approved """
        queryset.update(checked=True)

    def reset_checked_status(self, request, queryset):
        """ Action to reset the approved status """
        queryset.update(checked=False)
