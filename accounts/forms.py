from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User  

class UserRegistrationForm(UserCreationForm):
    picture = forms.ImageField(required=False)
    is_manager = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
    is_coordinator = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = User  
        fields = ['username', 'password1', 'password2', 'picture', 'is_manager', 'is_coordinator']
        labels = {
            'username': _('Username'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
            'picture': _('Profile Picture'),
            'is_manager': _('Manager'),
            'is_coordinator': _('Coordinator'),
        }
