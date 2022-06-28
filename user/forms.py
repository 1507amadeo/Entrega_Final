from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django.forms import ModelForm
from user.models import Avatar

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', min_length=3)
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    fecha_nacimiento=forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','fecha_nacimiento']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'perfil']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        help_texts = {k: "" for k in fields}



class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )