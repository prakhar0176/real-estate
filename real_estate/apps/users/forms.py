from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

# UserCreationForm is designed for creating new users (including setting the password), while UserChangeForm is used for updating existing user details.

class CustomUserCreationForm(UserCreationForm):
    # The Meta class is used to define the configuration for the form. It allows you to specify which model the form is associated with, which fields should be included, and any additional options like custom error classes.
    class Meta(UserCreationForm):
        # model = User: Specifies that this form should be tied to your custom User model.
        model = User
        # fields = ['email', 'username', 'first_name', 'last_name']: Specifies the fields from your User model that should be included in the form. These are the fields that the user will fill out when creating a new user.
        fields = ['email', 'username', 'first_name', 'last_name']
        error_class  = 'error'
    
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        error_class = 'error'


