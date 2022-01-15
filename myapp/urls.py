from django.urls import path

from myapp.api.AdminEnquiryFormsAPI import AdminEnquiryforms
from myapp.api.EmployeeAPI import AllEmployees
from myapp.api.EnquiryformAPI import AllEnquiryforms, EmployeeClaim

urlpatterns = [
    path('users/employees/', AllEmployees.as_view(), name="AllEmployees"),
    path('users/enquiryforms/', AllEnquiryforms.as_view(), name="AllEnquiryforms"),
    path('users/adminenquiryforms/', AdminEnquiryforms.as_view(), name="AdminEnquiryforms"),
    path('users/claimenquiryforms/<int:pk>/', EmployeeClaim.as_view(), name="EmployeeClaim"),

]
