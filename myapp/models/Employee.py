from django.db import models

from user.models import CustomUser


class Employee(models.Model):
    user = models.ForeignKey(CustomUser,related_name='employees',on_delete=models.CASCADE,null=True,blank=True)
    department = models.CharField(max_length=200)
    year_of_exp = models.PositiveIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)

