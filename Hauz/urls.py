from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^api/users/$', views.CreateUser.as_view(), name='account-create'),
]
