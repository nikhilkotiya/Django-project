from django.urls import path, include
from test_android import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("quize",views.Quize,basename="quize")
urlpatterns = [
    path('company/', views.Company.as_view()),
    path('test/',views.Test.as_view()),
    # path('',views.Quize.as_view()),
    path("",include(router.urls)),
]