from django.contrib import admin
from django.contrib.auth.models import User
from . models import Property_Type, Property, House, Maintenance, Amenity, Tenant, Payment, Expense
# Create a custom ModelAdmin class


class HouseAdmin(admin.ModelAdmin):
    filter_horizontal = ('amenity_id')


class ExpenseAdmin(admin.ModelAdmin):
    filter_horizontal = ('maintenance')


# Register your models here.
admin.site.register(Property_Type)
admin.site.register(Property)
admin.site.register(House, HouseAdmin)
admin.site.register(Amenity)
admin.site.register(Tenant)
admin.site.register(Maintenance, ExpenseAdmin)
admin.site.register(Expense)
admin.site.register(Payment)
