from django.urls import path, include
from blogapi import views

urlpatterns = [
    path('',views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]