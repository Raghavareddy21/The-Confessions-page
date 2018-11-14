from django import forms
from django.contrib.auth.models import User
from . import models
class Category(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=('category',)
class Confess(forms.ModelForm):
    class Meta:
        model=models.Confession
        fields=('Confession','image','categories')
#class Comment(forms.ModelForm):
#    class Meta:
#        model=models.Comment
#        fields=('comment',)
