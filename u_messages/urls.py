from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('send/', views.SendMessageView.as_view(), name="send_message")
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)