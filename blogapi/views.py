from django.shortcuts import render
from blog.models import Post
from users.models import User
from .serializers import PostS
# Create your views here.
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostS
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Detail = self.get_object(pk)
        serializer = PostS(Detail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        u=self.request.user.email
        if snippet.user.email==u:
            serializer = PostS(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        msg="You can't edit this post"
        return Response(msg)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        u=self.request.user.email
        if snippet.user.email==u:
            print(snippet)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            msg="You can't delete this post"
            print(msg)
            return Response(msg)