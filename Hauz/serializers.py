from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from . models import Property_Group, Property, Property_Type, House


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=32,
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    # create new usser method using create_user method from the User Class
    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('house_no', 'description', 'bedrooms',
                  'bathrooms', 'price', 'occupancy')


class PropertiesSerializer(serializers.ModelSerializer):
    # house_set = HouseSerializer(many=True)

    class Meta:
        model = Property
        fields = ('name', 'description', 'house_count',
                  'user', )


class PropertyTypeSerializer(serializers.ModelSerializer):
    property_set = PropertiesSerializer(many=True)

    class Meta:
        model = Property_Type
        fields = ('id', 'name', 'created_at', 'property_set')


class ProprtyGroupSerializer(serializers.ModelSerializer):
    group_property = PropertiesSerializer(many=True)

    class Meta:
        model = Property_Group
        fields = ('name', 'created_at', 'user', 'group_property')
