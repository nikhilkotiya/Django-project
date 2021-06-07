from django.shortcuts import render
from rest_framework import generics
from .serializers import companyS,Test_name_S,QuizeS
from test_api.models import Test_name
from test_api.models import Company as comp
from test_api.models import Quize as Q
from users.models import User
from users.models import Profile
# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# company registration
class Company(generics.ListCreateAPIView):
    queryset = comp.objects.all()
    serializer_class = companyS
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        s=serializer.data.get("company_name")
        print(s)
        u=self.request.user
        p=Profile.objects.get(user_id=self.request.user.id)
        p.company=s
        p.save()
# Test registration
class Test(generics.ListCreateAPIView):
    queryset = Test_name.objects.all()
    serializer_class = Test_name_S
    def perform_create(self, serializer):
        user=Profile.objects.filter(user_id=self.request.user.id).first()
        print(user.company)
        d=user.company
        x=comp.objects.get(company_name=d)
        serializer.save(company=x)
        print(serializer)

# class Quize(APIView):
#     def get(self, request, format=None):
#         user=Profile.objects.get(user_id=self.request.user.id)
#         print(user.company)
#         d=user.company
#         x=comp.objects.get(company_name=d)
#         data=Q.objects.all()
#         serializer = QuizeS(data, many=True)
#         return Response(serializer.data)
#     def post(self, request,format=None):
#         user=Profile.objects.filter(user_id=self.request.user.id).first()
#         print(user.company)
#         d=user.company
#         # test_name='devopers test'
#         # test=Test_name.objects.get(test_name=test_name)
#         # print(test)
#         x=comp.objects.get(company_name=d)
#         print(x)
#         data=request.data
#         data.company=x
#         print(data)
#         serializer = QuizeS(data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # serializer = QuizeS
#         # user=Profile.objects.filter(user_id=self.request.user.id).first()
#         # print(user.company)
        # d=user.company
        # test_name='devopers test'
        # test=Test_name.objects.filter(test_name=test_name)
        # print(test)
        # x=comp.objects.get(company_name=d)
        # print(x)
        # QuizeS.save(company=x,test=test)

    #         queryset = Test_name.objects.all()
    # serializer_class = QuizeS
    # def perform_create(self, serializer):
    #     user=Profile.objects.filter(user_id=self.request.user.id).first()
    #     print(user.company)
    #     d=user.company
    #     test_name='google developer'
    #     test=Test_name.objects.filter(test_name=test_name)
    #     print(test)
    #     x=comp.objects.get(company_name=d)
    #     print(x)
    #     serializer.save(company=x,test=test)


class Quize(viewsets.ModelViewSet):
    queryset=Q.objects.all()
    serializer_class = QuizeS