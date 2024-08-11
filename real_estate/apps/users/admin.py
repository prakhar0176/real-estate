from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

class userAdmin(BaseUserAdmin):
    # Specifies that the users should be ordered by their email addresses in the admin interface.
    ordering = ['email']

    # Specifies the form to use when creating a new user. This form handles user creation, including setting the password.
    add_form = CustomUserCreationForm

    # Specifies the form to use when updating an existing user. This form is used to modify user details.
    form = CustomUserChangeForm

    # Specifies the model this admin class is tied to, which is your custom User model.
    model = User

    # Defines the columns that will be displayed in the list view of the admin interface for users.
    list_display = ['pkid', 'id', 'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']

    # Specifies which fields in the list view should be clickable links that lead to the detail view of the user.
    list_display_links = ['id', 'email']

    # Adds filters to the right-hand side of the user list in the admin interface, allowing the admin to filter users by these fields.
    list_filter = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']

    # Purpose: The fieldsets option defines how the fields are grouped and displayed on the user detail/edit page in the admin interface.

    # Structure:
    # Login Credential: Includes fields for email and password.
    # Personal Information: Includes fields for username, first_name, and last_name.
    # Permissions and Groups: Includes fields for managing user permissions and group memberships.
    # Important Dates: Includes fields for last_login and date_joined.
    # Each tuple in fieldsets contains a section title (translated using gettext_lazy), and a dictionary specifying which fields belong to that section.

    fieldsets = (
        (
            _('Login Credential'),
            {
                'fields': ('email', 'password',)
            },
        ),
        (
            _('Personal Information'),
            {
                'fields': ('username', 'first_name', 'last_name',)
            },
        ),
        (
            _('Permissions and Groups'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        (
            _('Important Dates'),
            {'fields': ('last_login', 'date_joined',)},
        ),
    )

    # Purpose: add_fieldsets is similar to fieldsets, but it’s specifically for the form used to create new users.
    # Structure:
    # No section title (hence None).
    # Applies the wide CSS class for styling.
    # Includes fields for email, password1, password2, is_staff, and is_active.
    add_fieldsets=(
        None, 
        {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        },
    )

    # Purpose: Specifies which fields should be searchable in the user list view.
    # Usage: This allows an admin to search for users based on their email, username, first name, or last name.
    search_fields = ['email', 'username', 'first_name', 'last_name']


# Purpose: Registers your custom User model with the userAdmin class in the Django admin site.
# Effect: This tells Django to use your userAdmin class to manage User objects in the admin interface.
admin.site.register(User, userAdmin)

    
