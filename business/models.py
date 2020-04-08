from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
# import datetime

class BusinessInfo(models.Model):
    class BooleanChoices(models.TextChoices):
        YES = 'YES', _('Yes')
        NO = 'NO', _('No')

    businessName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    totalRevenue = models.FloatField()
    priorRevenue = models.FloatField()
    costOfGoodsSold = models.FloatField()
    operatingExpenses = models.FloatField()
    cashBalance = models.FloatField()
    currentAssets = models.FloatField()
    currentLiabilities = models.FloatField()
    longTermLiabilities = models.FloatField()
    ownerSatisfaction = models.IntegerField() # 1 to 11
    employeeSatisfaction = models.IntegerField() # 1 to 11
    newCustomers = models.IntegerField()
    startCustomers = models.IntegerField()
    endCustomers = models.IntegerField()
    rewardsProgram = models.CharField(max_length=3, choices=BooleanChoices.choices) # no default
    totalInventory = models.FloatField()
    deadInventory = models.FloatField()
    expansion = models.CharField(max_length=3, choices=BooleanChoices.choices) # no default