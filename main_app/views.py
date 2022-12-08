from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item

class ItemCreate(CreateView):
    model: Item


def index(request):
    return render(request, 'index.html')

def items_index(request):
    items=Item.objects.all()
    return render(request, 'items/index.html', {'items': items})
