from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AppUser
from .serializers import AppUserSerializer

class AppUserApi(APIView):
    def post(self,request):
        print(request.data)
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("User has been created successfully")
            return Response("User has been created successfully",status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        users = AppUser.objects.all()
        serializer = AppUserSerializer(users, many=True)
        return Response(serializer.data)
