from django.shortcuts import render,redirect
from .models import Post
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from users.models import User
def home(request):
    p=Post.objects.all()
    return render(request,'home.html',{'post':p})

@csrf_exempt
def add(request):
    if request.method=="POST":
        p=Post()
        p.title=request.POST["title"]
        p.description=request.POST["disc"]
        p.user=User.objects.filter(email=request.user.email).first()
        p.save()
        return redirect('/feed')
    return render(request,'post.html')



def edit(request,id):
    if request.method=="POST":
        p=Post.objects.get(pk=id)
        p.description=request.POST["disc"]
        p.title=request.POST["title"]
        p.save()
        return redirect('/feed')
    p=Post.objects.get(pk=id)
    return render(request,'update.html',{'p':p})



def delete(request,id):
    data=Post.objects.get(pk=id)
    data.delete()
    return redirect('/feed')