from django.contrib import admin
from rest.subscribe.models import Subscribe
from .forms import SubscribeForm


class EmailSubscribeAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at', 'updated_at', 'id']
    search_fields = ['email', 'id']
    ordering = ['created_at']

admin.site.register(Subscribe, EmailSubscribeAdmin)