from django.shortcuts import render

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterUserAppuser
from .serializers import AppUserSerializer

class UpdateUserAPIView(APIView):
    def put(self,request):
        try:
            email = request.data.get('email')
            user = RegisterUserAppuser.objects.get(email=email)
        except RegisterUserAppuser.DoesNotExist:
            return Response("Please enter a valid Email address.",status=status.HTTP_400_BAD_REQUEST)
        serializer = AppUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("User details have been updated successfully.",status=status.HTTP_201_CREATED)
        return Response("Sorry ! Failed to update. Please check the entered data.",status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        try:
            email = request.data.get('email')
            user= RegisterUserAppuser.objects.get(email=email)
        except RegisterUserAppuser.DoesNotExist:
            return Response("Please enter a valid Email address.",status=status.HTTP_400_BAD_REQUEST)
        
        user.delete()
        return Response("User Details have been successfully deleted.",status=status.HTTP_201_CREATED)

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




    
    
        














       