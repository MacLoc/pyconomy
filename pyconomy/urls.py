from django.conf.urls import patterns, url

from pyconomy.accounts.views import AccountListView

urlpatterns = patterns('',
                       url(r'^v1/accounts/', AccountListView.as_view()),
                       )
