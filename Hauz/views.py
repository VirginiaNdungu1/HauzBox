from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import UserSerializer, ProprtyGroupsSerializer, PropertiesSerializer, PropertyTypeSerializer, PropertyGroupSerializer, PropertySerializer, NewPropertySerializer, NewPaymentSerializer, PaymentSerializer, NewHouseSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from . models import Property_Group, Property, Property_Type, Payment
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
from django.views.generic.edit import CreateView
# from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt


class CreateUser(APIView):
    permission_classes = (AllowAny,)
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
    # user = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault())

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
        serializers = ProprtyGroupsSerializer(
            property_groups, many=True)

        json = serializers.data
        return Response(json)

    def post(self, request, format='json'):
        serializer = PropertyGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyTypeList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_property_types(self):
        return Property_Type.objects.all()

    def get(self, request, format='json'):
        property_types = self.get_property_types()
        serializer = PropertyTypeSerializer(property_types, many=True)
        json = serializer.data
        return Response(json)

# properties per user


class PropertiesList(APIView):
    permission_classes = (IsAuthenticated, )

    def get_user_properties(self, user_id):
        try:
            return Property.objects.filter(user_id=user_id).all()
        except Property.DoesNotExist:
            return Http404

    def get(self, request, format='json'):
        user = request.user
        user_id = user.id
        properties = self.get_user_properties(user_id)
        serializers = PropertySerializer(properties, many=True)
        json = serializers.data
        return Response(json)

    def post(self, request, format='json'):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Payments per user endpoint


class Payments(APIView):
    permission_classes = (IsAuthenticated,)

    def get_property_payments(self, user_id):
        try:
            return Payment.objects.filter(user_id=user_id).all()
        except Payment.DoesNotExist:
            return Http404

    def get(self, request, format='json'):
        user = request.user
        user_id = user.id
        # get all user properties.

        payments = self.get_property_payments(user_id)
        serializers = PaymentSerializer(payments, many=True)
        json = serializers.data
        return Response(json)

    def post(self, request, format='json'):
        serializer = NewPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyHouses(APIView):
    permission_classes = (IsAuthenticated, )

    def get_user_properties(self, user_id):
        try:
            return Property.objects.filter(user_id=user_id).all()
        except Property.DoesNotExist:
            return Http404

    def post(self, request, format='json'):
        serializer = NewHouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format='json'):
        user = request.user
        user_id = user.id
        properties = self.get_user_properties(user_id)
        serializers = PropertiesSerializer(properties, many=True)
        json = serializers.data
        return Response(json, status=status.HTTP_200_OK)
