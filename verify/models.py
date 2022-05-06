from datetime import datetime, timedelta
import string
from django.db import models
from django.utils import timezone
from accounts.models import User
import random

def set_expire():
    return timezone.now() + timezone.timedelta(minutes=5)

class VerifyCode(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=16)
    expire = models.DateTimeField(default=set_expire)

    def generate(length, user):
        code = ''.join([random.choice(string.digits) for i in range(length)])
        return VerifyCode.objects.create(user = user, code = code)

    def verify(code, user):
        try:
            if user:
                return VerifyCode.objects.get(user=user, code=code, expire__gt=timezone.now())
            else:
                return VerifyCode.objects.get(code=code, expire__gt=timezone.now())
        except VerifyCode.DoesNotExist:
            return None