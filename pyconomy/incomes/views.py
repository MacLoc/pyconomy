from rest_framework.generics import ListCreateAPIView
from pyconomy.incomes.models import Income

from pyconomy.incomes.serializers import IncomeSerializer


class IncomeListView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
