from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from .forms import RegistrationForm


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, "profile.html")


def login_view(request):
    return render(request, 'login.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect(redirect_url)
    return render(request,'login.html',{"error": "Пользователь не найден"})


def profile_view(request):
    return render(request, 'profile.html')

def register_view(request):
   if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('profile')
   else:
        form = RegistrationForm()
   return render(request, 'register.html', {"form": form})
    # return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


