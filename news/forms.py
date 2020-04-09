from django.forms import ModelForm
from .models import Review,News
from django import forms

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['text']


class NewsForm(ModelForm):
	class Meta:
		model = News
		fields = ['title','text','description','year','poster','tag','category','url']