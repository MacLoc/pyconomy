from rest_framework.generics import ListCreateAPIView
from pyconomy.accounts.serializers import AccountSerializer


class AccountListView(ListCreateAPIView):
    serializer_class = AccountSerializer
