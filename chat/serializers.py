from rest_framework import serializers
from chat.models import Room,Chat
from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['created','invited','date','name','private']

class UserASerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
