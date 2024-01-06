from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
# Create your models here.

class VisitorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    birth_date = models.DateField(null=True, blank=True)
    account_created  = models.DateField(auto_now_add=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)