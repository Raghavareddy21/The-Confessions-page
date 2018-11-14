from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta

# Create your models here.
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
class Category(models.Model):
    category=models.CharField(blank=True,max_length=30)
    def __str__(self):
        return self.category
class Confession(models.Model):
    Confession=models.TextField(blank=False)
    image=models.FileField(upload_to='pictures/',blank=True)
    upload_date=models.DateTimeField(default=timezone.now())
    categories=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.Confession
#class Comment(models.Model):
#    comment=models.ForeignKey('Confession.Confession',on_delete=models.CASCADE,name='comments')
#    upload_date=models.DateTimeField(default=timezone.now())
#    author=models.ForeignKey(User,on_delete=models.CASCADE)
