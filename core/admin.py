# from django.contrib import admin
# from core.models import User
# from django.contrib.auth.admin import UserAdmin
#
#
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     """
#     Класс с кастомной настройкой админ-панели пользователя
#     """
#     list_display = ('email', 'username', 'first_name', 'last_name',  'is_superuser', )
#     search_fields = ('email', 'username')
#     list_filter = ('is_superuser', 'is_staff', 'is_active')


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User


class CustomUserAdmin(UserAdmin):
    """
    Класс с кастомной настройкой админ-панели пользователя
    """
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, CustomUserAdmin)
