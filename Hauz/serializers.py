from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    # first_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(min_length=8)

    # create new usser method using create_user method from the User Class
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['first_name'],
                                        validated_data['last_name'], validated_data['username'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
