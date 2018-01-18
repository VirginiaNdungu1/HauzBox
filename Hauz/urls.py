from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^api/users/register/$', views.CreateUser.as_view(), name='account-create'),
    url(r'^api/property_group/(?P<user_id>[0-9]+)/$',
        views.PropertyGroupList.as_view()),
]
