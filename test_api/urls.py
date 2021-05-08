from django.urls import path, include
import users
from  .import views
urlpatterns = [
    path('',views.home),
    path('quize/',views.quize,name="quize"),
    path('company/new/setup/',views.company, name="company"),
    #path('company/<str:company_name>/',views.welcome), 
    path('company/<str:company_name>/<str:test_name>/add/quize/',views.quizeF),
    path('company/add/test/',views.test_name),
    path('company/<str:company_name>/<str:test_name>/quiz/',views.index),
    path('company/<str:company_name>/<str:test_name>/quiz/save_ans/',views.save_ans,name="saveans"),
    path('company/<str:company_name>/<str:test_name>/quiz/result/',views.result,name="result"),

]