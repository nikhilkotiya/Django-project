from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Quize,Save_test,Company,Test_name
from users.models import User,Profile
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import CompanyR,QuizeF,Test
def company(request):
    if request.method=="POST":
        # form=CompanyR()
        # form.company_name=request.POST["name"]
        # form.tagline=request.POST["tagline"]
        # form.website_url=request.POST["url"]
        # form.user_id=User.objects.filter(email=request.user.email).first()
        # form.company_type=request.POST["type"]
        # if form.is_valid():
        #     r="Registration done"
        #     print("1")
        #     form.save()
        #     print("2")
        c=request.POST["name"]
        t=request.POST["tagline"]
        u=request.POST["url"]
        type=request.POST["type"]
        user=User.objects.filter(email=request.user.email).first()
        data=Profile.objects.filter(user_id=request.user.id).first()
        data.company=request.POST["name"]
        print(data.company)
        data.save()
        #print(user.email)
        Company.objects.create(company_name=c,website_url=u,company_type=type,user_id=user,tagline=t)
        r="done"
        return render(request,"company.html")
        # else:
        #     print("error")
        #     return render(request,"company.html")
    return render(request,"company.html")

def quizeF(request,company_name=None,test_name=None):
    if company_name!=None:
        if request.method=="POST":
            q=request.POST["question"]
            o1=request.POST["option1"]
            o2=request.POST["option2"]
            o3=request.POST["option3"]
            o4=request.POST["option4"]
            a=request.POST["answer"]
            t=Test_name.objects.get(test_name=test_name)
            x=Company.objects.get(company_name=company_name)
            Quize.objects.create(company=x,test=t,question=q,option1=o1,option2=o2,option3=o3,option4=o4,answer=a)
            print("No error")
            #data = Quize()
            #data.test_name__test_name=25
            # data.comp__company_name=company_name
            # data.question=request.POST["question"]
            # data.option1=request.POST["option1"]
            # data.option2=request.POST["option2"]
            # data.option3=request.POST["option3"]
            # data.option4=request.POST["option4"]
            # data.answer=request.POST["answer"]
            # data.save()
        return render(request,"quize.html")
    else:
        return HttpResponse("Register Your Compony First")
@csrf_exempt
def test_name(request):
    if request.method=="POST":
        t=request.POST["test"]
        user=Profile.objects.filter(user_id=request.user.id).first()
        print(user.company)
        d=user.company
        x=Company.objects.get(company_name=d)
        #data.company__company_name=user.company
        Test_name.objects.create(test_name=t,company=x)
        print("No error")
        # data.company_name__company_name=u
        # data.save()
        # print(data) 
        #Test_name.objects.create(test_name=t,company__company_name=user.company) 
        
        return render(request,"test_register.html")
    form=Test_name()
    return render(request,"test_register.html",{"form":form})


def index(request,test_name=None,company_name=None):
    if request.user.is_authenticated:
        id = User.objects.get(pk=request.user.id)
        print(test_name)
        obj = Quize.objects.filter(company__company_name=company_name,test__test_name=test_name)
        count =Quize.objects.filter(company__company_name=company_name,test__test_name=test_name).count()
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
    answers = Quize.objects.filter(company__company_name=company_name,test__test_name=test_name)
    anslist = []
    for i in answers:
        anslist.append(i.answer)
    score =0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score +=1
    lst.clear()
    u=User.objects.filter(email=request.user.email).first()
    print(u)      
    print(score)
    s=score
    try:
        c=Company.objects.get(company_name=company_name)
        print(c)
        t=Test_name.objects.get(test_name=test_name)
        print(t)
        Save_test.objects.create(user_id=u,score=s,test=t,company=c)
        print("no error")
    except:
        print("Error")
    return render(request,'result.html',{'score':score,'lst':lst})

def save_ans(request,test_name=None,company_name=None):
    ans = request.GET['ans']
    lst.append(ans)
def welcome(request,company_name=None):
    if company_name!=None:
        t=company_name
        print("welcome")
        print(t)
        #test=company.objects.filter(test__test_name=x)
        test=Test_name.objects.filter(company_name__company_name=t)
        print(test)
        return render(request,'welcome.html',{'t':test})
    else:
        lst.clear()
        return render(request,'welcome.html')