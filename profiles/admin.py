""" Manage User Profile Model display in admin site """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    """ Show model in admin table with follow rules"""
    summernote_fields = ('bio')
    list_filter = ('membership', 'registered_on')
    list_display = ('user', 'name', 'membership', 'registered_on')
    search_fields = ['user', 'name', 'bio']
    actions = ['promote_to_creator', 'promote_to_admin', 'demote_to_member']

    def promote_to_creator(self, request, query_set):
        """ Action to change user membership as creator """
        query_set.update(membership=1)

    def promote_to_admin(self, request, query_set):
        """ Action to change user membership as admin """
        query_set.update(membership=2)

    def demote_to_member(self, request, query_set):
        """ Action to change user membership as member """
        query_set.update(membership=0)
