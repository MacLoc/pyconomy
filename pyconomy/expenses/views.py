from rest_framework.generics import ListCreateAPIView
from pyconomy.expenses.models import Expense

from pyconomy.expenses.serializers import ExpenseSerializer


class ExpenseListView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

