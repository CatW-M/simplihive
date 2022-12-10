from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item
# from .forms import ImageForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/items'

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'description', 'significance', 'anonymous']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/items/' + str(self.object.pk))

class ItemDelete(DeleteView):
    model = Item
    success_url = '/items'

# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'index.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def items_index(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', { 'items': items })

def items_show(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/show.html', {'item': item})

def profile(request, username):
    user = User.objects.get(username=username)
    item = list(Item.objects.filter(user=user))
    return render(request, 'profile.html', {'username': username, 'items': item})

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else: 
          return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})