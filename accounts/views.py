import re
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.backends import JWTAuthentication, authenticate
from .serializers import *
from DevroomTrialProject import exceptions
from .models import *

from django.core.mail import send_mail



class RegisterView(APIView):

    def post(self, request):
        data = request.data.copy()
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(True)
        user = User.objects.create_user(serializer.validated_data['email'], serializer.validated_data['password'])
        
        return Response(UserSerializer(user).data)

class LoginView(APIView):

    def post(self, request):
        data = request.data.copy()
        serializer = AuthSerializer(data=data)
        serializer.is_valid(True)
        user = authenticate(serializer.validated_data['email'], serializer.validated_data['password'])
        
        if not user:
            raise exceptions.NotFound('User not found')
        if not user.is_active:
            raise exceptions.BadRequest("Your is deactivated")
        return Response(UserSerializer(user).data)

class ProfileView(APIView):

    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

class LogoutView(APIView):

    def delete(self, request):
        try:
            prefix, token = request.headers['Authorization'].split()
        except ValueError:
            raise exceptions.BadRequest("Token is invalid")
        try:
            token = UserToken.objects.get(token=token)
            if not token.is_active:
                raise exceptions.BadRequest("Token is deactivated")
            token.is_active = False
            token.save()
        except UserToken.DoesNotExist:
            pass
        return Response(status=204)


        