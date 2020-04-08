from django.forms import ModelForm
from .models import Review,News

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['text']


class NewsForm(ModelForm):
	class Meta:
		model = News
		fields = ['title','text','description','poster','year','tag','category']