import random
from django.db import models
from django.utils import timezone
from accounts.models import User
from DevroomTrialProject import exceptions
from django.db.models import Q

def set_expire():
    return timezone.now() + timezone.timedelta(days=365 * 5)

def set_csc():
    return random.randint(111, 999)

class Card(models.Model):

    type = models.CharField(choices=[
        ('MasterCard', 'MasterCard'),
        ('Visa', 'Visa')
    ], max_length=32)
    csc = models.CharField(max_length=3, default=set_csc)
    number = models.IntegerField(max_length=16, default=0)
    expire = models.DateTimeField(default=set_expire)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    balance = models.FloatField(default=100)

    def save(self, **kwargs) -> None:
        if not self.id:
            if self.type == 'Visa':
                self.number = f'4{random.randint(111, 999)}{random.randint(1111, 9999)}{random.randint(1111, 9999)}{random.randint(1111, 9999)}'
            elif self.type == 'MasterCard':
                self.number = f'50{random.randint(11, 99)}{random.randint(1111, 9999)}{random.randint(1111, 9999)}{random.randint(1111, 9999)}'
        return super().save(**kwargs)

    @property
    def history(self):
        return Transaction.objects.filter(Q(from_card=self) | Q(to_card=self)).order_by('-id')

class Transaction(models.Model):

    from_card = models.ForeignKey(Card, on_delete=models.DO_NOTHING, related_name="from_card", null=True)
    to_card = models.ForeignKey(Card, on_delete=models.DO_NOTHING, related_name="to_card", null=True)
    amount = models.FloatField()
    type = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs) -> None:
        if self.amount < 0:
            raise exceptions.BadRequest("Server error")
        return super().save(**kwargs)