from django.urls import reverse
from backend.account.models import CustomUserManager, User


class BusinessAccountManager(CustomUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(account_type=User.Type.BUSINESS)


class BusinessAccount(User):
    objects = BusinessAccountManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("account:business-detail", kwargs={"pk": self.pk})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, **kwargs):
        self.account_type = User.Type.BUSINESS
        super().save(force_insert, force_update, using, update_fields, **kwargs)