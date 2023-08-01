from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from backend.abstract.models import ProvinceChoices
from .address import Address


class CommonAccountMixin(models.Model):
    class Type(models.TextChoices):
        PERSONAL = "personal", "Personal"
        BUSINESS = "business", "Business"

    account_type = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=Type.choices,
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number1 = PhoneNumberField(null=True, blank=True)
    phone_number2 = PhoneNumberField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_address",
    )
    province = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=ProvinceChoices.choices,
    )

    class Meta:
        abstract = True
