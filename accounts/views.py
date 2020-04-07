from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in now')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method =="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That user is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    auth.login(request,user)
                    messages.success(request,'You are logged in now')
                    return redirect('index')
        else:
            messages.error(request,'passwords do not match')
            return redirect('register')
    return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are logged out now')
        return redirect('index')
    return render(request,'room/index.html')



@login_required(login_url='login')
def dashboard(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(dashboard)
    return render(request,'accounts/dashboard.html',{'form':form})

@login_required(login_url='login')
def edit_profile(request):
    form = ProfileForm(instance=Profile.objects.get(user=request.user))
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect(dashboard)
    return render(request,'accounts/edit_profile.html',{'form':form})


@login_required(login_url='login')
def profile_list(request):
    users = User.objects.all()
    return render(request,'accounts/profile_list.html',{'users':users})
