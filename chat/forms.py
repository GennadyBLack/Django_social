from django.forms import ModelForm
from .models import Chat,Room
from django import forms


class MessageForm(ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Chat
        fields =['text']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields=['name','invited']
