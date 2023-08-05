from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group',on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=100)
    