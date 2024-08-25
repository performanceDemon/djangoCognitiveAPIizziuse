from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    SEXO_CHOICES = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    sexo = forms.ChoiceField(choices=SEXO_CHOICES, label='Sexo')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
