from django.contrib import admin

from .models import Message, Comment, Like


admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Like)