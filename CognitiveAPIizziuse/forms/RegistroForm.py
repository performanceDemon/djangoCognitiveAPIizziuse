
from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    SEXO_CHOICES = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    sexo = forms.ChoiceField(choices=SEXO_CHOICES)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña'
        self.fields['email'].label = 'Correo electrónico'
        self.fields['sexo'].label = 'Sexo'