from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

# This imports the gettext_lazy function from Django's translation utilities. gettext_lazy is used to mark strings in your code that should be translated into different languages. The "lazy" part means that the string is not translated immediately but is instead marked for translation when it is actually used.

# BaseUserManager is a class provided by Django specifically for managing user objects. It comes with built-in methods for user creation, such as create_user and create_superuser, and other utilities.

# By inheriting from BaseUserManager, CustomUserManager can use or override these existing methods to tailor them to the specific needs of your application.

# CustomUserManager is class that inherits from BaseUserManager.
class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide a valid email address'))
        
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValueError(_('Users must submit a user name'))
        
        if not first_name:
            raise ValueError(_('Users must submit a first name'))
        
        if not last_name:
            raise ValueError(_('Users must submit a last name'))
        
        if email:
            # normalize_email is a method that likely formats or cleans up the email address to ensure consistency (e.g., converting it to lowercase, trimming whitespace)
            email = self.normalize_email(email)
            # email_validator method probably checks if the email is in a valid format or adheres to certain criteria.
            self.email_validator(email)
        else:
            raise ValueError(_('Base User Account: An email address is required'))
        
        # self.model refers to the model class associated with the manager or class where this code resides. 
        # creation of a new user object by calling the model's constructor.
        
        user = self.model(
            username=username, 
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        # Instead of storing the password as plain text, set_password hashes the password using Django's password hashing system. This ensures that even if the database is compromised, the passwords are not exposed in their original form.
        user.set_password(password)
        # setdefault checks if the key 'is_staff' is present in the extra_fields dictionary. If it's not, it sets it to False.
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # using=self._db specifies which database to use, which is useful in projects with multiple databases. In most cases, this will use the default database.
        # The save method commits the user instance to the database.
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        if not password:
            raise ValueError(_('Superuser must have password'))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Admin Account: An email address is required'))
        
        user = self.create_user( username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user
