from django.contrib import admin
from .models import Item, Choice, Comment, MemberProfile

admin.site.register(Item)
admin.site.register(Choice)
admin.site.register(Comment)
# admin.site.register(Status)
admin.site.register(MemberProfile)

