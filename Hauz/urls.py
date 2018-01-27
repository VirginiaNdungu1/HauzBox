from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'houses', HouseViewSet)
# router.register(r'propertytypes', PropertyTypeViewSet)

urlpatterns = [
    url(r'^api/users/register/$', views.CreateUser.as_view(), name='account-create'),
    url(r'^api/property_group/$',
        views.PropertyGroupList.as_view()),
    url(r'^api/property_types/$', views.PropertyTypes.as_view()),
    url(r'^api/properties/$', views.PropertiesList.as_view()),
    url(r'^api/houses/$', views.PropertyHouses.as_view()),
    url(r'^api/payment/new/$', views.Payments.as_view()),
    url(r'^api/property/(?P<pk>[0-9]+)/$',
        views.PropertyHousesView.as_view()),
    # url(r'^api/property_group/properties/(?P<property_group_id>[0-9]+)/$',
    #     views.PropertiesList.as_view()),
]
