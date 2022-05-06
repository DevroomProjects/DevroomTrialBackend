from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

import requests

class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **fields):
        user = self.create_user(email, password, True, is_superuser=True, **fields)
        return user

    def create_user(self, email, password, is_staff=False, **fields):
        if not email:
            raise ValueError('Used username is null.')
        
        if not password:
            raise ValueError('User password is null.')
        
        user = self.model(email=email, password=make_password(password), is_staff=is_staff, **fields)
        user.save()
        return user