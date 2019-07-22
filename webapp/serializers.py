from rest_framework import serializers
from rest_framework.parsers import JSONParser
from . models import User
from . models import *
from datetime import date


class Userserializers(serializers.ModelSerializer):

    today = date.today()
    alphanumeric = RegexValidator(r'^[a-z]*$', 'Only alphabets are allowed.')
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=30,validators=[alphanumeric] )
    user_dob = serializers.DateField()

    
    class Meta:
        model= User
        fields = '__all__'
    def validate_user_dob(self, dob):
        today = date.today()
        if (not( dob < today)):
            raise serializers.ValidationError("message: Enter date before today date")
        return dob

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.user_dob = validated_data.get('user_dob', instance.user_dob)
        instance.save()
        return instance