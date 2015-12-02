from rest_framework.generics import ListCreateAPIView
from pyconomy.accounts.models import Account
from pyconomy.accounts.serializers import AccountSerializer


class AccountListView(ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
