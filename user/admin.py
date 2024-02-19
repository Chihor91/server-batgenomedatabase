from django.contrib import admin
from user.models import Account
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models

# Register your models here.
class UserAdminConfig(UserAdmin):
    model = Account
    search_fields = ('email', 'username',)
    list_filter = ('email', 'username',)
    ordering = ('-date_created',)
    list_display = ('email', 'username',)

    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)
        }),
    )

admin.site.register(Account, UserAdminConfig)