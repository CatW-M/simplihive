from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    significance = models.CharField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Choice(models.Model):
    DONATE = 'donate'
    TRASH = 'trash'
    KEEP = 'keep'
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    CHOICE_TEXT = [
        (DONATE, 'Donate'),
        (TRASH, 'Trash'),
        (KEEP, 'Keep'),
    ]
    choice_text = models.CharField(
        max_length=32,
        choices=CHOICE_TEXT,
    )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

