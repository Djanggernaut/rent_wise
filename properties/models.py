from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import User

class Address(models.Model):
    full_address = models.CharField(max_length=250)
    street_address = models.CharField(max_length=100)
    complement = models.CharField(max_length=100, blank=True, null=True)  # e.g., Apt 4B
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)  # adjust default as needed
    zip_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.full_address

class Property(models.Model):
    PROPERTY_TYPES = (
        ("House", "House"),
        ("Apartament", "Apartament"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    property_type = models.CharField(
        max_length=15, choices=PROPERTY_TYPES, default="House"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    bedroom = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)])
    bathroom = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)])
    square_meter = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return f"{self.property_type} - {self.address}"
    
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')