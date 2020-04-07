from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsAdminForm(forms.ModelForm):
	description = forms.CharField(widget=CKEditorUploadingWidget())
	text = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = News
		fields = '__all__'

@admin.register( Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ['name','url','id']
	list_display_links = ['name','id','url']

class ReviewInline(admin.StackedInline):
	model= Review
	extra = 1 #дополнительное поле 

@admin.register(News)
class NewsCategory(admin.ModelAdmin):
	list_display = ['title','avtor','draft','id']
	list_display_links = ['title','id','avtor']
	list_filter = ['title','category','tag']
	search_fields = ['title','category__name']
	inlines = [ReviewInline] # вывести все комментарии к фильму
	readonly_fields =['avtor']
	save_on_top = True #кнопка сохранения сверху
	list_editable = ['draft']
	form = NewsAdminForm

@admin.register( NewsShots)
class NewsShotsCategory(admin.ModelAdmin):
	list_display = ['title','image','news']
	list_display_links = ['title','image','news']



@admin.register( Tag)
class TagCategory(admin.ModelAdmin):
	list_display = ['name','url','id']
	list_display_links = ['name','id','url']



@admin.register( Review)
class REviewCategory(admin.ModelAdmin):
	list_display = ['news','parent','user']
	list_display_links = ['news','parent','user']



@admin.register( RatingStar)
class RatingStarCategory(admin.ModelAdmin):
	list_display = ['value','id']
	list_display_links = ['value','id']



@admin.register( Rating)
class RatingCategory(admin.ModelAdmin):
	list_display = ['star','id','news']
	list_display_links = ['star','id','news']



