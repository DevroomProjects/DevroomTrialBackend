from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.backends import JWTAuthentication
from .serializers import *
from DevroomTrialProject import exceptions
from .models import *

from django.core.mail import send_mail

class CardsView(APIView):

    authentication_classes = [JWTAuthentication]

    def get(self, request):
        cards = Card.objects.filter(owner=request.user)
        return Response(CardSerializer(cards, many=True).data)

    def post(self, request):
        data = request.data.copy()
        data['owner'] = request.user.id
        serializer = CreateCardSerializer(data=data)
        serializer.is_valid(True)
        card = serializer.save()
        transaction = Transaction()
        transaction.amount = 100
        transaction.from_card = None
        transaction.to_card = card
        transaction.type = 'deposit'
        transaction.save()
        return Response(CardSerializer(card).data)

class CardView(APIView):

    authentication_classes = [JWTAuthentication]

    def get(self, request, id):
        try:
            card = Card.objects.get(id=id)
        except Card.DoesNotExist:
            raise exceptions.NotFound("Card not found")
        return Response(CardSerializerWithHistory(card).data)

class TransactionsView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request):
        data = request.data.copy()
        data['type'] = 'transaction'
        if 'to_card' in data:
            try:
                Card.objects.get(number=data['to_card'])
            except Card.DoesNotExist:
                raise exceptions.BadRequest("To card not found")
        serializer = TransactionSerializer(data=data, context={'request': request})
        serializer.is_valid(True)
        transaction = serializer.save()
        return Response(TransactionSerializer(transaction).data)
