from rest_framework import serializers
from .models import VerifyCode

class VerifyCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VerifyCode
        fields = '__all__'