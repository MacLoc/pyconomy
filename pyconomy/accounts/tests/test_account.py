import django
from rest_framework.test import APITestCase

django.setup()

from rest_framework import status
from pyconomy.accounts.models import Account


class AccountTest(APITestCase):
    def test_create_account(self):
        account_data = {'name': 'HSBC personal account',
                        'type': 'saving account'}
        response = self.client.post('/v1/accounts/', account_data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Account.objects.count())

    def test_get_account(self):
        Account.objects.create(name='HSBC personal account',
                               type='Saving account')

        response = self.client.get('/v1/accounts/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))
        self.assertEqual('HSBC personal account', response.data[0]['name'])
        self.assertEqual('Saving account', response.data[0]['type'])
