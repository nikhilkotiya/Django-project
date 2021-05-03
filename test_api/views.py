from django.shortcuts import render
from django.http import HttpResponse
from .models import Quize,Save_test,Compony,Test_name
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@csrf_exempt
def index(request,test_name=None,compony_name=None):
    if request.user.is_authenticated:
        id = User.objects.get(pk=request.user.id)
        obj = Quize.objects.filter(compony_name__compony_name=compony_name,test_name__test_name=test_name)
        count =Quize.objects.filter(compony_name__compony_name=compony_name,test_name__test_name=test_name).count()
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
def result(request,test_name=None,compony_name=None):
    answers = Quize.objects.filter(compony_name__compony_name=compony_name,test_name__test_name=test_name)
    print(answers)
    anslist = []
    for i in answers:
        anslist.append(i.answer)
    score =0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score +=1
    u=User.objects.filter(email=request.user.email).first()
    print(score)
    s=score
    try:
        print("Name")
        print(test_name)
        Save_test.objects.create(user_id=u,score=s,test_name=test_name)
        print("no error")
    except:
        print("Error")
    return render(request,'result.html',{'score':score,'lst':lst})

def home(request):
    return HttpResponse("this is the home page")

def save_ans(request,test_name=None,compony_name=None):
    ans = request.GET['ans']
    lst.append(ans)
def welcome(request,compony_name=None):
    if compony_name!=None:
        t=compony_name
        #test=Compony.objects.filter(test__test_name=x)
        test=Test_name.objects.filter(compony__compony_name=t)
        print(test)
        return render(request,'welcome.html',{'t':test})
    else:
        lst.clear()
        return render(request,'welcome.html')
