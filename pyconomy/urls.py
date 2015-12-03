from django.conf.urls import patterns, url

from pyconomy.accounts.views import AccountListView
from pyconomy.expenses.views import ExpenseListView
from pyconomy.incomes.views import IncomeListView

urlpatterns = patterns('',
                       url(r'^v1/accounts/', AccountListView.as_view()),
                       url(r'^v1/expenses/', ExpenseListView.as_view()),
                       url(r'^v1/incomes/', IncomeListView.as_view()),
                       )
