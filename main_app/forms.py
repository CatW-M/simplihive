from .models import Item, Choice, Comment, Status
from django import forms

choices = Status.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'significance', 'status', 'anonymous')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'significance': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'anonymous': forms.RadioSelect(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }