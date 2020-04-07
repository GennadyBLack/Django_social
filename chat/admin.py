from django.contrib import admin
from .models import Room,Chat

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display=['creater','date']


class ChatAdmin(admin.ModelAdmin):
    list_display=['user','date','text','room']



admin.site.register(Room,RoomAdmin)
admin.site.register(Chat,ChatAdmin)
