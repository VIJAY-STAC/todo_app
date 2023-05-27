import uuid
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone
from django.db import transaction
from .core import CreatedByModel, LastModifiedByModel, PrimaryUUIDTimeStampedModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser




class User(AbstractUser, PrimaryUUIDTimeStampedModel):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dob = models.DateTimeField(blank=True)