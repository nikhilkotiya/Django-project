from django.contrib import admin
from django.urls import path, include
import users
from test_api import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('quize/',views.quize,name="quize"),
    path('company/<str:company_name>/',views.welcome),  
    path('company/<str:company_name>/<str:test_name>/quiz/',views.index),
    path('company/<str:company_name>/<str:test_name>/quiz/save_ans/',views.save_ans,name="saveans"),
    path('company/<str:company_name>/<str:test_name>/quiz/result/',views.result,name="result"),
    path('accounts/', include('users.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)