from django.contrib import admin
from django.contrib.admin import display

from myapp.models.Employee import Employee
from myapp.models.Enquiryform import Enquiryform


@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ['id','user','department','year_of_exp']
    list_filter = ['department','year_of_exp']
    # search_fields = []
    date_hierarchy = 'created_at'

    # @display(ordering='user__email', description='Email')
    # def get_user_email(self, obj):
    #     return obj.user.email


@admin.register(Enquiryform)
class EnquiryformAdmin(admin.ModelAdmin):
    list_display = ['id','student','department','course','semester','employee','created_at']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
