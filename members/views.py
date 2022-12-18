from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from main_app.models import Item, User
from .models import Profile
from .forms import EditProfileForm, PasswordChangingForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('index')


def login_user(request):
    if request.method == "POST":            
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = User.objects.get(username=username)
            return redirect('edit_profile')
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

