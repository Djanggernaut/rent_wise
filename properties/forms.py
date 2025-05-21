from django import forms
from .models import Property, Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "full_address",
            "street_address",
            "complement",
            "neighborhood",
            "city",
            "state",
            "country",
            "zip_code",
        ]


class PropertyForm(forms.ModelForm):
    property_type = forms.ChoiceField(choices=Property.PROPERTY_TYPES)

    class Meta:
        model = Property
        fields = [
            "property_type",
            "price",
            "bedroom",
            "bathroom",
            "square_meter",
        ]