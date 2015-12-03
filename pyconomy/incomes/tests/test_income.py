import django

from pyconomy.accounts.models import Account
from pyconomy.incomes.models import Income

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

    def test_get_income(self):
        account = Account.objects.create(name='HSBC personal account',
                                         type='Saving account')
        income_data = {'description': 'January Salary',
                       'amount': '1503.90',
                       'category': 'Salary',
                       'account': account,
                       'is_received': True}

        Income.objects.create(**income_data)
        income_data.update(account=account.id)

        response = self.client.get('/v1/incomes/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

        # updating the dicts to be able to compare them
        income_data.update(account=account.id)
        del response.data[0]['id']

        self.assertDictEqual(income_data, response.data[0])
