from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from . models import users
from . serializers import usersserializers
from datetime import *
from django.http import Http404
from django.test import signals
import logging
from datetime import *


class userList(APIView):
    

   def get(self, request):
       users1= users.objects.all()
       serializer=usersserializers(users1, many= True)
       return Response(serializer.data)

   def post(self, request, format=None):
        serializer = usersserializers(data=request.data)
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
        user = users.objects.get(username=username)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = usersserializers(user)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = usersserializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def happyBirthday(date):
        today = datetime.datetime.now()
        if users.objects.filter(user_dob__month=today.month, user_dob__day=today.day)
          print ("Happy Birthday " + username)
        else 
          nextdob= users.objects.filter(date.month - user_dob__month,date.day-user_dob__day)
		  return (nextdob)
    
    