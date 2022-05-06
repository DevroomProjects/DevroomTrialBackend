import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
import time

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .utils import UserManager
from django.contrib.auth.models import Group as DjangoGroup

class Group(DjangoGroup):
    ru_name = models.CharField(max_length=128)
    color = models.CharField(max_length=32)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(db_index=True, max_length=256, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ()
    objects = UserManager()

    def __str__(self):
        return self.username

    def check_role(self, name):
        if self.groups.filter(name=name).exists():
            return True
        elif self.groups.filter(name="admin").exists():
            return True
        else:
            return False

    @property
    def token(self, days=30):
        return self._generate_jwt_token(days=days)

    def _generate_jwt_token(self, days):
        expire = time.time() + 60 * 60 * 60 * 24 * days
        token = jwt.encode({
            'id': self.pk,
            'exp': expire
        }, settings.SECRET_KEY, algorithm='HS256')
        UserToken.objects.create(user=self, token=token, expire=datetime.fromtimestamp(expire))
        return token

class UserToken(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=512)
    expire = models.DateTimeField()
    is_active = models.BooleanField(default=True)

