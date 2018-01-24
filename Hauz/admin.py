from django.contrib import admin
from django.contrib.auth.models import User
from . models import Property_Type, Property, House, Amenity, Payment, Property_Group
# Create a custom ModelAdmin class


class PropertyAdmin(admin.ModelAdmin):
    filter_horizontal = ('amenities',)


class ExpenseAdmin(admin.ModelAdmin):
    filter_horizontal = ('maintenances',)



# Register your models here.
admin.site.register(Property_Type)
admin.site.register(Property, PropertyAdmin)
admin.site.register(House)
admin.site.register(Amenity)
# admin.site.register(Tenant)
# admin.site.register(Maintenance)
# admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Payment)
admin.site.register(Property_Group)
