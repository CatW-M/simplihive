from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    significance = models.CharField(max_length=250)
    date_posted = models.DateTimeField('date listed')
    active = models.BooleanField(True)
