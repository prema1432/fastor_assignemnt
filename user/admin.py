from django.contrib import admin
from django.contrib.admin import display

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.site_header = "FASTOR"
# admin.site.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = ('id','email','name','is_superuser','is_employee','is_student' )
    list_filter = ('is_student','is_employee')
    fieldsets = (
        (None, {'fields': ('email','name', 'password','phone_number','is_employee','is_student','is_staff','active','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'name', 'password1', 'password2','is_student','is_employee'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser,UserAdmin)


