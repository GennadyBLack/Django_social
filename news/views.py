from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from .forms import NewsForm,RatingForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse, HttpResponse


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            print(x_forwarded_for)
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(ip,'IIIIPPPPPPPP')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                news_id=int(request.POST.get("news")),
                defaults={'star_id': int(request.POST.get("star"))} # Какое поле мы хотим поменять
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

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
	rating = RatingForm()
	return render(request,'news/news_detail.html',context = {'news':news,'star_form':rating})

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