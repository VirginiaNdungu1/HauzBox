from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
Month_Choices = (
    ('Jan', 'january'),
    ('Feb', 'february'),
    ('Mar', 'march'),
    ('Apr', 'april'),
    ('May', 'may'),
    ('Jun', 'june'),
    ('July', 'july'),
    ('Aug', 'august'),
    ('Sep', 'september'),
    ('Oct', 'october'),
    ('Nov', 'november'),
    ('Dec', 'december'),
)


class Property_Type(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'property_type'

    def __str__(self):
        return self.name


class Property_Group(models.Model):
    class Meta:
        db_table = 'property_group'

    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_property_group', null=True)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    class Meta:
        db_table = 'amenity'

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='property_amenity')

    def __str__(self):
        return self.name


class Property(models.Model):
    class Meta:
        db_table = 'property'

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True)
    house_count = models.PositiveIntegerField(default=0)
    property_type = models.ForeignKey(
        Property_Type, on_delete=models.CASCADE, related_name='all_property_types')
    property_group = models.ForeignKey(
        Property_Group, on_delete=models.CASCADE, related_name='group_property', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_property')
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.name


class House(models.Model):
    class Meta:
        db_table = 'houses'

    house_no = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    occupancy = models.BooleanField(default=False)
    property_types = models.ForeignKey(
        Property_Type, on_delete=models.CASCADE, related_name='house_id')
    house_property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='property_houses', null=True)
    # tenants = models.ForeignKey(
    #     Tenant, on_delete=models.CASCADE, related_name='house_tenant', blank=True, null=True)

    def __str__(self):
        return self.house_no


class Tenant(models.Model):
    class Meta:
        db_table = 'tenant'

    house_id = models.ForeignKey(
        House, on_delete=models.CASCADE, null=True, related_name='house_tenant')
    name = models.CharField(max_length=50)
    original_id = models.PositiveIntegerField()
    account_no = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='property_tenant')

    def __str__(self):
        return self.name


class Payment(models.Model):
    class Meta:
        db_table = 'payment'
    property_id = models.ForeignKey(Property,on_delete=models.CASCADE, related_name='property_payment')
    tenant_name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    
    # house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_payment')
    transaction_id = models.CharField(max_length=50)
    # month = models.CharField(max_length=30, choices=Month_Choices, default='jan', blank=True)
    # paid_at = models.TimeField(
    #     auto_now=False, auto_now_add=False, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    # is_paid = models. BooleanField(default=False)

    def __str__(self):
        return str(self.property_id)


class Maintenance(models.Model):
    class Meta:
        db_table = 'maintenance'

    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Expense(models.Model):
    class Meta:
        db_table = 'expense'

    property_id = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='property_expense', null=True)
    gabbage = models.DecimalField(max_digits=10, decimal_places=2)
    security = models.DecimalField(max_digits=10, decimal_places=2)
    cleaning = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(
        max_length=30, choices=Month_Choices, default='jan', blank=True)
    maintenances = models.ManyToManyField(Maintenance)
    property_tax = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.month
