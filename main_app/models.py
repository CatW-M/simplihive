from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    significance = models.CharField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_image = models.ImageField(null=True, blank=True, upload_to='images/')
    anonymous = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='deciding')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    item = models.ForeignKey(Item, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.item.name, self.name)


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

