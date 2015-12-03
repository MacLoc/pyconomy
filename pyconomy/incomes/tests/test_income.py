
import django

from pyconomy.accounts.models import Account

django.setup()
from rest_framework import status
from rest_framework.test import APITestCase


class IncomeTest(APITestCase):
    def test_create_income(self):
        account = Account.objects.create(name='HSBC personal account',
                                         type='Saving account')

        # TODO: include date
        income_data = {'description': 'January Salary',
                        'amount': '1503.90',
                        'category': 'Salary',
                        'account': account.id,
                        'is_received': 'True'}

        response = self.client.post('/v1/incomes/', income_data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(income_data['description'], response.data['description'])
        self.assertEqual(income_data['amount'], response.data['amount'])
        self.assertEqual(income_data['category'], response.data['category'])
        self.assertEqual(income_data['account'], response.data['account'])
        self.assertTrue(response.data['is_received'])
