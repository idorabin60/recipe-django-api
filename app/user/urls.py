"""
URL mapping for the user API
"""
from django.urls import path

from .views import CreateUserView, CreateTokeView, LogoutView, ManagaUserView

app_name = 'user'

urlpatterns = [
    path('/create', CreateUserView.as_view(), name='create'),
    path('/token', CreateTokeView.as_view(), name='token'),
    path('/logout', LogoutView.as_view(), name='log-out'),
    path('/me', ManagaUserView.as_view(), name='me')
]
