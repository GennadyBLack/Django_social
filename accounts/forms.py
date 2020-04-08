from django.forms import ModelForm
from .models import Profile
from django import forms


class DateInput(forms.DateInput):
    birthday = 'date'


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields =['phone','avatar','birthday','description','status']
        widgets = {
            'birthday': DateInput(attrs={'type':'date'})
        }
