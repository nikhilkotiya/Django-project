from django.contrib import admin
from django.urls import path
from test_paper import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome),
    path('quiz/',views.index),
    path('save_ans/',views.save_ans,name="saveans"),
    path('result/',views.result,name="result"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)