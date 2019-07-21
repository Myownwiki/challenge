from rest_framework import serializers
from . models import User
from . models import *
from datetime import date



class Userserializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=30)
    user_dob = serializers.models.DateField()
    class Meta:
        model= User
        fields = '__all__'
        
    def create(self, validated_data):
        """
        Create and return a new `user` instance, given the validated data.
        """
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `user` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.user_dob = validated_data.get('user_dob', instance.user_dob)
        instance.save()
        return instance