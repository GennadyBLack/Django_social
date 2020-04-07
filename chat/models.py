from django.db import models
from django.contrib.auth.models import User
from django import template


class Room(models.Model):
    name = models.CharField(verbose_name='Название Чата',max_length=100)
    creater = models.ForeignKey(User,verbose_name='Создатель',on_delete=models.CASCADE ,related_name='creator')
    invited = models.ForeignKey(User,verbose_name='Участник',on_delete=models.CASCADE,related_name='invited')
    date = models.DateTimeField('data',auto_now_add=True)
    private = models.BooleanField(default=False)


    def get_absolute_url(self):
        return 'chat:room_detail', (), {'id': self.pk }

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Диалог'
        verbose_name_plural = 'Диалоги'



class Chat(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text

    class Meta:
         verbose_name='Сообщение'
         verbose_name_plural='Сообщения'
         ordering=['-date']
