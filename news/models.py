from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Category(models.Model):
	name = models.CharField('Категория',max_length=150, unique=True, blank=False, null=False)
	description = models.TextField('Description',max_length=500)
	url = models.SlugField(max_length=160,unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class Tag(models.Model):
	name = models.CharField('Tag',max_length=150, unique=True, blank=False, null=False)
	description = models.TextField('Description',max_length=500)
	url = models.SlugField(max_length=160,unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

class News(models.Model):
	title = models.CharField('Title',max_length=100)
	text = models.TextField(max_length=5000)
	description = models.TextField('Description',max_length=500)
	poster = models.ImageField('Постер',upload_to='movies/')
	year = models.PositiveIntegerField('Дата выхода',default=2019)
	avtor = models.ForeignKey(User,verbose_name='avtor',related_name='news_avtor',on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag,related_name='tags')
	category = models.ForeignKey(Category,on_delete= models.SET_NULL,null=True,blank=True)
	url = models.SlugField(max_length=160,unique=True)
	draft = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)

	def get_review(self):
		return self.review_set.filter(parent__isnull=True)

	def get_absolute_url(self):
		return reverse('news_detail', kwargs={"id":self.id})


	def __str__(self):
		return self.title

	class Meta:
		verbose_name='News'
		verbose_name_plural='News'

class NewsShots(models.Model):
	title= models.CharField('Title',max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='news_shots/')
	news = models.ForeignKey(News,on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Кадр'
		verbose_name_plural ='Кадры'


class RatingStar(models.Model):
	value = models.PositiveIntegerField(default=0)

	def __str__(self):
		return str(self.value)

	class Meta:
		verbose_name='Звезда рейтинга'
		verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
	ip = models.CharField(max_length=15)
	star = models.ForeignKey(RatingStar,on_delete=models.CASCADE)
	news =models.ForeignKey(News,on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.star} - {self.news}"

	class Meta:
		verbose_name = 'Рейтинг'
		verbose_name_plural = 'Рейтинги'

class Review(models.Model):
	text = models.TextField(max_length=1000)
	parent = models.ForeignKey('self',on_delete=models.SET_NULL,blank=True,null=True)
	news = models.ForeignKey(News,on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	
	def __str__(self):
		return f"{self.user.username} - {self.news}"

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'

