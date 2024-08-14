from django import forms
from .RegistroForm import RegistroForm
from django.contrib.auth import authenticate

class LoginForm(RegistroForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Elimina los campos que no son necesarios para el login
        self.fields.pop('sexo')  # Reemplaza 'campo1' con el nombre del campo que deseas eliminar
       # self.fields.pop('campo2')  # Reemplaza 'campo2' con el nombre del campo que deseas eliminar

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Usuario o contraseña incorrectos')
        return self.cleaned_data