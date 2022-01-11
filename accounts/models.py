from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Other'),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(blank=True, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.email