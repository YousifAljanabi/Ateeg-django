from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from backend.abstract.models import IntEntity
from backend.account.models import CommonAccountMixin


class CustomUserManager(UserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('User must provide an email')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.name = name
        user.is_active = True
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('user must have email')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(IntEntity, AbstractUser, CommonAccountMixin):
    username = None
    email = models.EmailField('البريد الإلكتروني', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, **kwargs):
        super(User, self).save()


