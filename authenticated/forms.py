from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MiUserCreationForm(UserCreationForm):
        
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2',]

class MiUserLoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario')  # Cambia la etiqueta del campo username a 'Nombre de Usuario'
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  # Cambia la etiqueta del campo password a 'Contraseña'







        