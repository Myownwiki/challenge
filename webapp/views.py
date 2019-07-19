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


class userList(APIView):
   def get(self, request):
       logging.debug("Hello>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssssssss")
       users1= users.objects.all()
       serializer=usersserializers(users1, many= True)
       return Response(serializer.data)

   def post(self, request, format=None):
        serializer = usersserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class userDetail(APIView):
    pk_url_kwarg = "username"
    """
    Retrieve, update or delete an user
    """
    def get_object(self,pk):
        try:
            return users.objects.get(pk=pk)
        except users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        logging.debug("Hello>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssssssss")
        user2 = self.get_object(pk)
        serializer = usersserializers(user2)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user2 = self.get_object(pk)
        serializer = usersserializers(user2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user2 = self.get_object(pk)
        user2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)