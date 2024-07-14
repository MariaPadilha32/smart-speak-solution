from django.contrib import admin
from .models import Newsletter
from .models import SubscribedUsers

# Register your models here.

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')


admin.site.register(SubscribedUsers, SubscribedUsersAdmin)