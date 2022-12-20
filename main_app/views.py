from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import generic
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item, Choice, Comment, MemberProfile
from .forms import CommentForm, ItemForm, VoteForm, MemberForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from calendar import HTMLCalendar
from datetime import datetime
from django.urls import reverse_lazy


class ItemIndex(ListView):
    model = Item
    template_name = 'main_app/item_index.html'

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
    form_class = ItemForm
    template_name = 'main_app/item_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/items'

class ItemDelete(DeleteView):
    model = Item
    template_name = 'main_app/item_delete.html'
    success_url = '/items'

class ItemDetailView(DetailView):
    model = Item
    form_class = VoteForm
    template_name = 'main_app/item_detail.html'

class MemberProfileCreateView(CreateView):
    model = MemberProfile
    form_class = MemberForm
    template_name = 'main_app/member_edit.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('edit_profile')

class MemberProfileUpdateView(UpdateView):
    model = MemberProfile
    form_class = MemberForm
    template_name = 'main_app/member_edit.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('edit_profile')

class ResultsView(generic.DetailView):
    model = Item
    template_name = 'main_app/results.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main_app/add_comment.html'

    class Meta:
        ordering = ['-date_added',]
        
    def form_valid(self, form):
        form.instance.item_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)
    success_url = '/items'

class VoteItem(CreateView):
    model = Choice
    form_class = VoteForm
    template_name = 'main_app/item_vote.html'
    
    def form_valid(self, form):
        form.instance.item_id = self.kwargs['pk']
        form.instance.user = self.request.user
        # if Item.choice.choice_text:
        #     form.instance.votes += 1

        return super().form_valid(form)

    success_url = 'results'

def index(request):
    return render(request, 'index.html')




