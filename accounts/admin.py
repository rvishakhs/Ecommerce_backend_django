from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Changing the accounts fields view 
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name')
    search_fields = ('email', 'first_name', 'last_name', 'user_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Account, AccountAdmin)
