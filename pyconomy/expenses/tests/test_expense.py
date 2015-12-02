import django

from pyconomy.accounts.models import Account
from pyconomy.expenses.models import Expense

django.setup()
from rest_framework import status
from rest_framework.test import APITestCase


class ExpenseTest(APITestCase):
    def test_create_expense(self):
        account = Account.objects.create(name='HSBC personal account',
                                         type='Saving account')

        # TODO: include date
        expense_data = {'description': 'Lunch at Tiramisu',
                        'amount': '12.55',
                        'category': 'Food',
                        'account': account.id,
                        'is_paid': 'True'}

        response = self.client.post('/v1/expenses/', expense_data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(expense_data['description'], response.data['description'])
        self.assertEqual(expense_data['amount'], response.data['amount'])
        self.assertEqual(expense_data['category'], response.data['category'])
        self.assertEqual(expense_data['account'], response.data['account'])
        self.assertTrue(response.data['is_paid'])

    def test_get_expense(self):
        account = Account.objects.create(name='HSBC personal account',
                                         type='Saving account')
        expense_data = {'description': 'Lunch at Tiramisu',
                        'amount': '12.55',
                        'category': 'Food',
                        'account': account,
                        'is_paid': True}
        Expense.objects.create(**expense_data)
        expense_data.update(account=account.id)

        response = self.client.get('/v1/expenses/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

        # updating the dicts to be able to compare them
        expense_data.update(account=account.id)
        del response.data[0]['id']

        self.assertDictEqual(expense_data, response.data[0])
