from django import forms
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from .models import Record

class CustomRegistrationForm(RegistrationForm):
    email = forms.EmailField(required=True)

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['nombre', 'seccion', 'casilla', 'votosmorenapvpt', 
                  'votosmc', 'votospripanprd', 'imagen']