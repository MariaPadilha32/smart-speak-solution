from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Add contact filters to admin panel"""
    list_display = ('email', 'subject', 'message')
    list_filter = ('email',)
    search_fields = ('email',)
