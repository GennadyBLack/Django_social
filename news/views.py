from django.shortcuts import render,get_object_or_404,redirect
from .models import News,Review
from django.views.generic.base import View
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.views.generic.edit import CreateView
from .forms import NewsForm
from django.contrib.auth.decorators import login_required




def news_list(request):
	news = News.objects.filter(draft=False)
	return render(request,'news/index.html',context = {'news':news})

@login_required(login_url='login')
def edit(request,id):
	form = NewsForm(instance=News.objects.get(id=id))
	if request.method =="POST":
		form = NewsForm(request.POST,instance=News.objects.get(id=id))
		if form.is_valid():
			form.save()
			messages.success(request, 'news has been changed')
			return render(request,'news/news_edit.html',{'id':id,'form':form})
	return render(request,'news/news_edit.html',{'id':id,'form':form})


@login_required(login_url='login')
def news_create(request):
	form = NewsForm()
	if request.method =="POST":
		form = NewsForm(request.POST,request.FILES)
		if form.is_valid():
			news = form.save(commit=False)
			news.avtor = request.user
			news.save()
			return render(request, 'news/index.html')
	return render(request, 'news/news_create.html',context={'form':form})
    


def news_detail(request,id):
	news = get_object_or_404(News,pk=id)
	return render(request,'news/news_detail.html',context = {'news':news})

@login_required(login_url='login')
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


def search_news(request):
	if request.method == "POST":
		if request.POST['search']:
			news = News.objects.filter(Q(title__icontains=request.POST['search']) | Q(text__icontains=request.POST['search']) | Q(description__icontains=request.POST['search']))
			messages.success(request,'Было найдено' + str(news.count()) + 'статей')
			return render(request,'news/index.html',context = {'news':news})
	
	news = News.objects.filter(draft=False)
	return render(request,'news/index.html',context = {'news':news})