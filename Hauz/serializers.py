from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from . models import Property_Group, Property, Property_Type, House, Amenity, Tenant, Expense, Maintenance,Payment


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


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('id', 'name', 'amount')


class MonthlyExpenseSerializer(serializers.ModelSerializer):
    maintenances = MaintenanceSerializer(many=True)

    class Meta:
        model = Expense
        fields = ('id', 'month', 'gabbage', 'security',
                  'cleaning', 'property_tax', 'maintenances')


class PropertyTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Type
        fields = ('id', 'name')


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id', 'name', 'original_id', 'account_no', 'phone_number')


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('id', 'name')


class NewPropertySerializer(serializers.ModelSerializer):
    # amenities = AmenitySerializer(many=True)
    amenities = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Amenity.objects.all())
    # property_type = serializers.CharField(source=property_type.id)

    class Meta:
        model = Property
        fields = ('id', 'name', 'description', 'house_count',
                  'property_type', 'property_group', 'user', 'amenities')

    # def create(self, validated_data):
    #     amenity_data = validated_data.pop('amenities')
    #     single_property = Property.objects.create(**validated_data)
    #     for amenity in amenity_data:
    #         d = dict(amenity)
    #         Property.objects.create(
    #             single_property=single_property, amenity=d['amenity'])
    #     return single_property


class PropertySerializer(serializers.ModelSerializer):
    property_expense = MonthlyExpenseSerializer(many=True)

    class Meta:
        model = Property
        fields = ('name', 'description', 'house_count',
                  'user', 'property_type', 'property_expense')


class PropertyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Group
        fields = ('id', 'name', 'user')


class HouseSerializer(serializers.ModelSerializer):
    # amenity_id = AmenitySerializer(many=True)
    # amenity_id = serializers.SlugRelatedField(many=True, read_only=True,
    #                                           slug_field='name')
    # tenants = TenantSerializer()
    property_types = PropertyTypeListSerializer()
    # tenant_id = serializers.SlugRelatedField(
    #     read_only=True, slug_field='name')

    class Meta:
        model = House
        fields = ('property_types', 'house_no', 'description', 'bedrooms',
                  'bathrooms', 'price', 'occupancy')


class PropertiesSerializer(serializers.ModelSerializer):
    property_houses = HouseSerializer(many=True)
    amenities = AmenitySerializer(many=True)
    property_type = PropertyTypeListSerializer()

    class Meta:
        model = Property
        fields = ('name', 'description', 'house_count',
                  'user', 'property_type', 'amenities', 'property_houses', )


class PropertyTypeSerializer(serializers.ModelSerializer):
    # house_id = PropertiesSerializer(many=True)
    # property_types  = Prop
    # house_id = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Property_Type
        fields = ('id', 'name', 'created_at',)


class ProprtyGroupsSerializer(serializers.ModelSerializer):
    group_property = PropertiesSerializer(many=True)

    class Meta:
        model = Property_Group
        fields = ('name', 'created_at', 'user', 'group_property')

# serializer for payments
class NewPaymentSerializer(serializers.ModelSerializer):
    # amenities = AmenitySerializer(many=True)
    # property_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Property.objects.all())
    # property_type = serializers.CharField(source=property_type.id)

    class Meta:
        model = Payment
        fields = ('tenant_name', 'month', 'transaction_id', 'amount', 'property_id')

    # def create(self, validated_data):
    #     amenity_data = validated_data.pop('amenities')
    #     single_property = Property.objects.create(**validated_data)
    #     for amenity in amenity_data:
    #         d = dict(amenity)
    #         Property.objects.create(
    #             single_property=single_property, amenity=d['amenity'])
    #     return single_property

