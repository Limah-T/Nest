from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomManager(BaseUserManager):
    ...

class CustomUser(AbstractUser):
    ...