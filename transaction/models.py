from django.db import models
from visitor.models import VisitorModel
from .constants import TRANSACTION_TYPE
# Create your models here.

class TransactionModel(models.Model):
    account = models.ForeignKey(VisitorModel, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.user)


