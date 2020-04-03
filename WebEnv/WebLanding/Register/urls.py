from django.urls import include, re_path,path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_view
from Register.views import RegisterView

app_name = 'Register'
urlpatterns = [
    path('',RegisterView.as_view(), name = 'Register'),
]