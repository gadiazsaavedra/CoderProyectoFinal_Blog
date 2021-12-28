from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email")
    password1 = forms.CharField(label="Ingrese su contraseña")
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
        
class Meta:
    model = User
    fields = ('email', 'password1', 'password2', 'last_name', 'first_name')

class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
   #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)

   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


    
class BlogFormulario(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.TextField()
    blogger = forms.ForeignKey(Blogger, on_delete=forms.CASCADE)
    created_at = forms.DateTimeField(auto_now_add=True)
    updated_at = forms.DateTimeField(auto_now=True)

class Bloggere