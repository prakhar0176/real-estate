import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# AbstractBaseUser: A Django model class that provides the core implementation of a user model, without including flields like username, email, etc. It provides the basic functionality needed for a custom user model, such as password management and authentication.

# PermissionsMixin: A Django model mixin that provides the ability to assign permissions and groups to the user and includes fields like is_superuser.

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("UserName"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =["username", "first_name", "last_name"]

    objects = CustomUserManager()

    # The Meta class is an internal class in Django models that holds metadata for the model. This metadata is not related to the database schema but rather to how the model behaves in Django’s framework.

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
    

    # The @property decorator is used to define a method that can be accessed like an attribute, without needing to call it like a function. This means you can access get_full_name as user.get_full_name instead of user.get_full_name().
    
    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    def get_short_name(self):
        return self.username




