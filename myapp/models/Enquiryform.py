from django.db import models

from myapp.models.Employee import Employee
from user.models import CustomUser


class Enquiryform(models.Model):
    student = models.ForeignKey(CustomUser, related_name='students', on_delete=models.CASCADE, null=True, blank=True)
    department = models.CharField(max_length=200)
    course = models.CharField(max_length=2500, blank=True, null=True)
    semester = models.CharField(null=True, blank=True, max_length=250)
    employee = models.ForeignKey(Employee,related_name='counsellor',on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)
