from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

USER_MODEL = get_user_model()


@admin.register(USER_MODEL)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email'
    )
    list_display_links = ('username',)
    readonly_fields = ('last_login', 'date_joined',)
    add_fieldsets = (
        (None,
         {"fields": (
             "username",
             "password1",
             "password2"
         )}),
        ('Персональная информация',
         {"fields": (
             "first_name",
             "last_name",
             "email"
         )}),
        ('Права доступа',
         {"fields": (
             "is_staff",
         )}),
    )
    fieldsets = (
        (None,
         {"fields": (
             "username",
             "password",
         )}),
        ('Персональная информация',
         {"fields": (
             "first_name",
             "last_name",
             "email"
         )}),
        ('Права доступа',
         {'classes': ('collapse',),
          "fields": (
              "is_staff",
              "is_active",
              "groups",
              "user_permissions"
          )}),
        ('Важные даты',
         {"fields": (
             "last_login",
             "date_joined"
         )}),
    )
