from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from . models import User
from . serializers import Userserializers
from datetime import date
from django.http import Http404
from django.test import signals
import logging
import calendar
import datetime

def calBirthday(user):
    print ('Hello World>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    

class userList(APIView):
    

   def get(self, request):
       user= User.objects.all()
       serializer=Userserializers(user, many= True)
       return Response(serializer.data)

   def post(self, request, format=None):
        serializer = Userserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def userDetail(request, username):
    """
    Retrieve, update or delete an user.
    """
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Userserializers(user)
        today=date.today()
        user_dob = user.user_dob
        current_year_dob = user_dob.replace(year=today.year)
        delta = today - current_year_dob
        if (delta.days == 0):
            return Response({"message": "Today is your birthday! Happy Birthday!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Your Birthday is in next " + str(delta.days)+ "days."}, status=status.HTTP_200_OK)
            
    elif request.method == 'PUT':
        serializer = Userserializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   