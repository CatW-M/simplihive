from .models import Item, Choice, Comment, MemberProfile
from django import forms

# choices = Status.objects.all().values_list('name','name')

choice_list = [('DECIDING', 'Deciding'), ('DONATED', 'Donated'), ('TRASHED', 'Trashed'), ('KEPT', 'Kept'),]

# for item in choices:
#     choice_list.append(item)


vote_choice = [('DONATE', 'Donate'), ('TRASH', 'Trash'), ('KEEP', 'Keep'),]

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'significance', 'status', 'item_image', 'anonymous')
        labels = {
            'name': '',
            'description': '',
            'significance': '',
            'status': 'Choose status of item...',
            'item_image': 'Upload image:',
            'anonymous': 'Post anonymously?',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
            'significance': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Significance (if any)'}),
            'status': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ('bio', 'profile_pic', 'city', 'state')
        labels = {
            'bio': '',
            'profile_pic': 'Upload image:',
            'city': '',
            'state': '',

        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share something about yourself...'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Share your city (optional)'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Share your state (optional)'}),
        }

class VoteForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('name', )
        widgets = {
             'name': forms.Select(choices=vote_choice, attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment here'}),
        }