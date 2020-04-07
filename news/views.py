from django.shortcuts import render,get_object_or_404
from .models import News,Review
from django.views.generic.base import View
from django.contrib import messages
from django.urls import reverse


def news_list(request):
	news = News.objects.filter(draft=False)
	return render(request,'news/index.html',context = {'news':news})

def news_create(request):
    return render(request,'news/news_create.html')

def news_detail(request,id):
	news = get_object_or_404(News,pk=id)
	return render(request,'news/news_detail.html',context = {'news':news})


def add_review(request):
	if request.method == "POST":
		
		text = request.POST['text']	
		news_id = request.POST['news_id']
		news = get_object_or_404(News,pk=int(news_id))
		if request.POST['parent']:
			review = Review.objects.create(news=news,text=text,user=request.user,parent_id=request.POST['parent'])
		else:
			review = Review.objects.create(news=news,text=text,user=request.user)
		review.save()
		messages.success(request,'review is added')
		return render(request,'news/news_detail.html',context = {'news':news})
	return render(request,'news/news_detail.html',context = {'news':news})