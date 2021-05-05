from django.shortcuts import render
from django.http import HttpResponse
from .models import Quize,Save_test,Company,Test_name
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import CompanyR,QuizeF

def company(request):
    if request.method=="POST":
        form=CompanyR(request.POST)
        print(form)
        print("form")
        if form.is_valid():
            r="Registration done"
            form.save()
            return render(request,"company.html",{"r":r})
        else:
            return render(request,"company.html",{'form': form})
    form = CompanyR()
    return render(request,"company.html",{"form":form})

def quizeF(request,company_name=None):
    if company_name!=None:
        if request.method=="POST":
            form=QuizeF(request.POST)
            if form.is_valid():
                form.save()
                return render(request,"quize.html")
            return render(request,"quize.html",{'form': form})
        
        else:
            form = QuizeF()
        return render(request,"quize.html",{"form":form})
    else:
        return HttpResponse("Register Your Compony First")
def index(request,test_name=None,company_name=None):
    if request.user.is_authenticated:
        id = User.objects.get(pk=request.user.id)
        obj = Quize.objects.filter(company_name__company_name=company_name,test_name__test_name=test_name)
        count =Quize.objects.filter(company_name__company_name=company_name,test_name__test_name=test_name).count()
        paginator = Paginator(obj,1)
        try:
            page = int(request.GET.get('page','1'))  
        except:
            page =1
        try:
            questions = paginator.page(page)
        except(EmptyPage,InvalidPage):
            questions=paginator.page(paginator.num_pages)
        return render(request,'index.html',{'obj':obj,'questions':questions,'count':count,'id':id})
    else:
        return HttpResponse("Login First")
def quize(request):
    x=Test_name.objects.all()
    return HttpResponse(x)
lst = []
def result(request,test_name=None,company_name=None):
    answers = Quize.objects.filter(company_name__company_name=company_name,test_name__test_name=test_name)
    anslist = []
    for i in answers:
        print("here")
        anslist.append(i.answer)
        print("here2")
    score =0
    print("here3")
    for i in range(len(lst)):
        print("here4")
        if lst[i]==anslist[i]:
            print("here5")
            score +=1
            print("here6")
    print("here7")  
    lst.clear()
    print("list clear")      
    u=User.objects.filter(email=request.user.email).first()
    print(score)
    s=score
    try:
        print("Name")
        c=company_name
        print(test_name)
        Save_test.objects.create(user_id=u,score=s,test_name=test_name,company_name=c)
        print("no error")
    except:
        print("Error")
    return render(request,'result.html',{'score':score,'lst':lst})
def home(request):
    return HttpResponse("this is the home page")
def save_ans(request,test_name=None,company_name=None):
    ans = request.GET['ans']
    lst.append(ans)
def welcome(request,company_name=None):
    if company_name!=None:
        t=company_name
        print("welcome")
        print(t)
        #test=company.objects.filter(test__test_name=x)
        test=Test_name.objects.filter(company__company_name=t)
        print(test)
        return render(request,'welcome.html',{'t':test})
    else:
        lst.clear()
        return render(request,'welcome.html')