from rest_framework import serializers
from DevroomTrialProject import exceptions
from .models import *
import string

class UserSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

class AuthSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password']

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise exceptions.BadRequest('Email already exists')
        return data

    def validate_password(self, data):
        """        print(string.punctuation)
        if len(data) < 8:
            raise exceptions.BadRequest("Password must consist of 8 characters")
        nice = False
        for i in string.punctuation:
            if i in data:
                nice = True
        if not nice:
            raise exceptions.BadRequest("Password must contain punctuation characters")
        nice = False
        for i in string.digits:
            if i in data:
                nice = True
        if not nice:
            raise exceptions.BadRequest("Password must contain digits")
        nice = False
        for i in string.ascii_letters:
            if i in data:
                nice = True
        if not nice:
            raise exceptions.BadRequest("Password must contain letters")"""
        return data

class PublicUserSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id']
