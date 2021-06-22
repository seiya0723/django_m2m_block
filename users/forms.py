from django import forms 

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,BlockUser

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model   = CustomUser
        fields  = ("username",)

class BlockUserForm(forms.ModelForm):

    class Meta:
        model   = BlockUser
        fields  = ["from_user","to_user"]
