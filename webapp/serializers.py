from rest_framework import serializers
from . models import User
from . models import *


class Userserializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    user_dob = serializers.models.DateField()
    class Meta:
        model= User
        fields = '__all__'
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_dob = validated_data.get('user_dob', instance.user_dob)
        instance.save()
        return instance