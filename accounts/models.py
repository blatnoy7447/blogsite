from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
