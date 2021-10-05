from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterUserAppuser
from .serializers import AppUserSerializer

class listAPIView(APIView):
    def get(self,request,email=None):
            if email is not None:
                try:
                    user = RegisterUserAppuser.objects.get(email=email)
                    serializer = AppUserSerializer(user)
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                except:
                    return Response("Please enter a valid Email address",status=status.HTTP_400_BAD_REQUEST)
            else:    
                users = RegisterUserAppuser.objects.all()
                serializer = AppUserSerializer(users, many=True)
                return Response(serializer.data,status=status.HTTP_201_CREATED)