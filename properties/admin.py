from django.contrib import admin
from .models import Property, Address, PropertyImage


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ["full_address", "created_at", "updated_at"]


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "property_type",
        "address",
        "bedroom",
        "bathroom",
        "square_meter",
        "created_at",
        "updated_at",
    ]

class PropertyImageAdmin(admin.ModelAdmin):
    list = [
        "property"
    ]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
admin.site.register(Address, AddressAdmin)
