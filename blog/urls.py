from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('addpost/',views.add,name="add-post"),
    path('updatepost/<int:id>/',views.edit,name='edit'),
    path('deletepost/<int:id>/',views.delete,name="delete"),
]