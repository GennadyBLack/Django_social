from django.shortcuts import render,get_object_or_404
from .models import News,Review
from django.views.generic.base import View
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q


def news_list(request):
	news = News.objects.filter(draft=False)
	return render(request,'news/index.html',context = {'news':news})



def news_create(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST,request.FILES)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.pizzashop = request.user.pizzashop
            pizza.save()
            return redirect(pizza_list)
    return render(request,'pizza/add_pizza.html',{form})
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

def search_news(request):
	if request.method == "POST":
		if request.POST['search']:
			news = News.objects.filter(Q(title__icontains=request.POST['search']) | Q(text__icontains=request.POST['search']) | Q(description__icontains=request.POST['search']))
			messages.success(request,'Было найдено' + str(news.count()) + 'статей')
			return render(request,'news/index.html',context = {'news':news})
	
	news = News.objects.filter(draft=False)
	return render(request,'news/index.html',context = {'news':news})