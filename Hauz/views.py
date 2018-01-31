from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import UserSerializer, ProprtyGroupsSerializer, PropertiesSerializer, PropertyTypeSerializer, PropertyGroupSerializer, PropertySerializer, NewPropertySerializer, NewPaymentSerializer, PaymentSerializer, NewHouseSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from . models import Property_Group, Property, Property_Type, Payment, House
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


# class PropertyTypeList(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get_property_types(self):
#         return Property_Type.objects.all()
#
#     def get(self, request, format='json'):
#         property_types = self.get_property_types()
#         serializer = PropertyTypeSerializer(property_types, many=True)
#         json = serializer.data
#         return Response(json)

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


class PropertyTypes(APIView):
    permission_classes = (IsAuthenticated, AllowAny, )

    def get_all_property_types(self):
        try:
            return Property_Type.objects.all()
        except Property_Type.DoesNotExist:
            return Http404

    def get(self, request, format='json'):
        property_types = self.get_all_property_types()
        serializers = PropertyTypeSerializer(property_types, many=True)
        json = serializers.data
        return Response(json, status=status.HTTP_200_OK)


class PropertyHousesView(APIView):
    def get_property_houses(self, pk):
        return Property.objects.get(pk=pk)

    def get(self, request, pk, format='json'):
        properties = self.get_property_houses(pk=pk)
        serializers = PropertiesSerializer(properties)
        json = serializers.data
        return Response(json, status=status.HTTP_200_OK)


class PropertyPayments(APIView):
    def get_property_payments(self, property_id_id):
        return Payment.objects.filter(property_id_id=property_id_id)

    def get(self, request, property_id_id, format='json'):
        payments = self.get_property_payments(property_id_id=property_id_id)
        serializers = PaymentSerializer(payments, many=True)
        json = serializers.data
        return Response(json, status=status.HTTP_200_OK)

    #  def put(self, request, pk, format=json):
    #     merch = self.get_merch(pk)
    #     serializers = MerchSerializer(merch, request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     else:
    #         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_property(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Http404

    def get(self, request, pk, format='json'):
        single_property = self.get_property(pk=pk)
        serializers = PropertySerializer(single_property)
        return Response(serializers.data)

    def put(self, request, pk, format='json'):
        single_property = self.get_property(pk=pk)
        serializers = PropertySerializer(single_property, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format='json'):
        single_property = self.get_property(pk=pk)
        if single_property:
            single_property.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_house(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            return Http404

    def get(self, request, pk, format='json'):
        house = self.get_house(pk=pk)
        serializers = NewHouseSerializer(house)
        return Response(serializers.data)

    def put(self, request, pk, format='json'):
        house = self.get_property(pk=pk)
        serializers = NewHouseSerializer(house, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format='json'):
        house = self.get_property(pk=pk)
        if house:
            house.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_payment(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Http404

    def get(self, request, pk, format='json'):
        payment = self.get_payment(pk=pk)
        serializers = NewPaymentSerializer(payment)
        return Response(serializers.data)

    def put(self, request, pk, format='json'):
        payment = self.get_payment(pk=pk)
        serializers = NewPaymentSerializer(payment, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format='json'):
        payment = self.get_payment(pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
