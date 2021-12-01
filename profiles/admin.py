from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio')
    list_filter = ('membership', 'registered_on')
    list_display = ('user', 'name', 'membership', 'registered_on')
    search_fields = ['user', 'name', 'bio']
    actions = ['promote_to_creator', 'promote_to_admin', 'demote_to_member']

    def promote_to_creator(self, request, query_set):
        query_set.update(membership=1)

    def promote_to_admin(self, request, query_set):
        query_set.update(membership=2)

    def demote_to_member(self, request, query_set):
        query_set.update(membership=0)
