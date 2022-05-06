from rest_framework import serializers
from .models import *
from accounts.serializers import PublicUserSerializer
from DevroomTrialProject import exceptions

class TransactionSerializer(serializers.ModelSerializer):

    from_card = serializers.SlugRelatedField(slug_field='number', queryset=Card.objects.all())
    to_card = serializers.SlugRelatedField(slug_field='number', queryset=Card.objects.all())

    class Meta:
        model = Transaction
        fields = '__all__'


    def validate(self, data):
        if data['amount'] > data['from_card'].balance:
            raise exceptions.BadRequest("You don't have enough funds")
        if data['from_card'] == data['to_card']:
            raise exceptions.BadRequest("You cannot transfer funds to yourself")
        if self.context['request'].user != data['from_card'].owner:
            raise exceptions.BadRequest("You don't have enough permissions")
        return data
    
    def create(self, validated_data):
        validated_data['from_card'].balance -= validated_data['amount']
        validated_data['to_card'].balance += validated_data['amount']
        validated_data['to_card'].save()
        validated_data['from_card'].save()
        transaction = super().create(validated_data)
        return transaction

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

class CardSerializerWithHistory(serializers.ModelSerializer):

    history = TransactionSerializer(many=True)

    class Meta:
        model = Card
        fields = '__all__'



class CreateCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

