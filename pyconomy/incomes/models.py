
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from pyconomy.accounts.models import Account


class Income(models.Model):
    description = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0'))])
    category = models.CharField(max_length=50)
    account = models.ForeignKey(Account, default=None, null=False)
    is_received = models.BooleanField(default=True, null=False)
