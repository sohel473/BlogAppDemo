from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

# Create some fields to override existing fields of django's forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Eamil Address", required=True)

    class Meta:
        model = User
        fields = ("username", 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)