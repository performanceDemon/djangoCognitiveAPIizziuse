from django import forms

API_CHOICES = (
    ('CognitiveMicrosoft', 'CognitiveMicrosoft'),
)

class CognitiveHomeForm(forms.Form):
    api = forms.ChoiceField(choices=API_CHOICES, label='Selecciona la API')
    feelings = forms.CharField(label='Describe como te sientes', widget=forms.Textarea)