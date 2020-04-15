from django.forms import ModelForm
from .models import Review,News,Rating,RatingStar
from django import forms

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['text']


class NewsForm(ModelForm):
	class Meta:
		model = News
		fields = ['title','text','description','year','poster','tag','category','url']


class RatingForm(ModelForm):
	star = forms.ModelChoiceField(queryset=RatingStar.objects.all(),widget=forms.RadioSelect(),empty_label=None)

	class Meta:
		model = Rating 
		fields = ['star']

