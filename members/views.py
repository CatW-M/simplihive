from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from main_app.models import Item, User

# Create your views here.
def login_user(request):
    if request.method == "POST":            
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', {'username':username})
        else:
            messages.success(request, ("There was an Error logging in, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
     
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Successfully Registered. Welcome!"))
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/signup.html', {'form': form,})

@login_required
def profile(request):
    return render(request, 'authenticate/profile.html')