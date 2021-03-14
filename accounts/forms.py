from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class Signup(UserCreationForm):

    class Meta():
        fields = ('first_name','last_name','username','email','password1','password2')
        model = get_user_model()