from rest_framework.generics import ListCreateAPIView

from pyconomy.incomes.serializers import IncomeSerializer


class IncomeListView(ListCreateAPIView):
    serializer_class = IncomeSerializer

