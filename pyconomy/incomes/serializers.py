

from rest_framework import serializers
from pyconomy.incomes.models import Income


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
