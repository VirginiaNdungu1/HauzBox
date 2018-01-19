from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import UserSerializer, ProprtyGroupSerializer, PropertiesSerializer, PropertyTypeSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from . models import Property_Group, Property, Property_Type
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CreateUser(APIView):
    '''
    creates user
    '''

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyGroupList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_property_by_user(self, user_id):
        try:
            return Property_Group.objects.filter(user_id=user_id).all()
        except Property_Group.DoesNotExist:
            return Http404

    def get(self, request, format='json'):
        user = request.user
        user_id = user.id
        property_groups = self.get_property_by_user(user_id)
        # property_types = self.get_property_type()
        serializers = ProprtyGroupSerializer(
            property_groups, many=True)

        json = serializers.data
        return Response(json)


class PropertyTypeList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_property_types(self):
        return Property_Type.objects.all()

    def get(self, request, format='json'):
        property_types = self.get_property_types()
        serializer = PropertyTypeSerializer(property_types, many=True)
        json = serializer.data
        return Response(json)
