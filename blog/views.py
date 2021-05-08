from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    p=Post.objects.all()
    return render(request,'home.html',{'post':p})