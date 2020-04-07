from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,blank=True)
    avatar = models.ImageField(upload_to='avatar/%d/%Y/')
    birthday = models.DateTimeField()
    description = models.TextField(max_length=500,blank=True,null=True)
    status = models.CharField(max_length=60,blank=True,null=True)

    def __str__(self):
        return self.user.username
