from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main_app.models import User
from .forms import EditProfileForm, PasswordChangingForm, UserCreateForm
from django.views import generic
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from main_app.models import MemberProfile, Item


# Create your views here.
class ShowProfilePageView(DetailView):
    model = User
    template_name = 'authenticate/user_profile.html'
    queryset = User.objects.all()
    lookup_field='user__pk'
    lookup_url_kwarg='pk'
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('index')

class UserRegisterView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'authenticate/signup.html'
    success_url = reverse_lazy('login')


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

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, ("Successfully Registered. Welcome!"))
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'authenticate/signup.html', {'form': form,})

