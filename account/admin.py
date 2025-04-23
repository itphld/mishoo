from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('firstname', 'lastname', 'mobile', 'email', 'is_active', 'is_admin','password')
    ordering = ('-last_login',)
    list_display_links = ('firstname', 'lastname', 'mobile', 'email','password')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'is_admin')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)
'''list_display=('firstname','lastname','mobile','email','is_active','is_admin')
ordering=('-last_login',)
list_display_links=('firstname','lastname','mobile','email')
list_editable=('is_active',)
filter_horizontal=()
fieldsets= ()'''
