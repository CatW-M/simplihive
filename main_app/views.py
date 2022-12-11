from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item, Choice, Comment
from .forms import CommentForm, ItemForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class ItemIndex(ListView):
    model = Item
    template_name = 'item_index.html'

class ItemCreate(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'main_app/item_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
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

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main_app/add_comment.html'
    def form_valid(self, form):
        form.instance.item_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)
    success_url = '/items'


def index(request):
    return render(request, 'index.html')




    
# def items_show(request, item_id):
#     item = Item.objects.get(id=item_id)
#     try:
#         selected_choice = item.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'items/detail.html', {
#             'item': item,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#     return render(request, 'items/detail.html', {'item': item})

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