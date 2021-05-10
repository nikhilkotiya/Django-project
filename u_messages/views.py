from django.shortcuts import render
from .models import Message
from django.views.generic import View
# Create your views here.
class SendMessageView(View):
    def post(self, request, *args, **kwargs):
        receiver_id = request.POST.get('receiver_id', '')
        file = request.FILES.get('file', '')
        Message.objects.create(sender=request.user, receiver__id=receiver_id, message_file=file)
        return render(request, 'success.html', {})