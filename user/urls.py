from django.urls import path

from user.api.UsersAPI import AllUsers

urlpatterns = [
    path('api/users/all/',AllUsers.as_view(),name="AllUsers"),
]
