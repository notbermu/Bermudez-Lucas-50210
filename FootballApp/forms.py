from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class RegistroFormulario(UserCreationForm):
    
    username = forms.CharField(label="Usuario", max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", max_length=20)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email","first_name", "password1", "password2"]

class EditarFormulario(UserChangeForm):

    password = None

    username = forms.CharField(label="Usuario", max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", max_length=20)
    
    class Meta:
        model = User
        fields = ["username", "email","first_name"]


##Lo busque en chat gpt para poder eliminar lo que decía antes de cambiar la contraseña!
class PassForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = None



class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()