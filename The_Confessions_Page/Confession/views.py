from django.shortcuts import render
# Create your views here.
from django.views import generic
from . import models
from django.http import HttpResponse
from . import forms

def add_confession(request):
    if request.method=='POST':
        form=forms.Confess(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Confession added")
    else:
        form=forms.Confess()
        return render(request,'Confession/confess.html',{'form':form})
def Home(request):
    confessions=models.Confession.objects.all()
    return render(request,'Confession/Confessions.html',{'Confessions':confessions})

#def add_comment(request):
#    if request.user.is_authenticated:
#        if request.method=='POST':
#            form=forms.Comment(request.POST)
#            if form.is_valid():
#                form.save()
#                return HttpResponse("Comment added")
#        else:
#            form=forms.Comment()
#            return render(request,'Confession/list.html',{'form':form})
#    else:
#        return HttpResponse("You need to login to add comments")
