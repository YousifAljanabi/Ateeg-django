from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from backend.abstract.models import ProvinceChoices


class Address(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=ProvinceChoices.choices,
    )
    postal_code = models.CharField(max_length=255, null=True, blank=True)

