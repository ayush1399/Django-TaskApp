from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):
    phone = PhoneNumberField()
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'gender')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)