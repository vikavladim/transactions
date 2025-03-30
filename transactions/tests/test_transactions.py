from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from transactions.models import Transaction
from reference.models import Status, OperationType, Category, SubCategory
from datetime import date


class TransactionAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        """Создаем тестовые данные один раз для всех тестов"""
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Создаем справочные данные
        cls.status = Status.objects.create(name='Завершено')
        cls.operation_type = OperationType.objects.create(name='Расход')
        cls.category = Category.objects.create(
            name='Еда',
            operation_type=cls.operation_type
        )
        cls.subcategory = SubCategory.objects.create(
            name='Рестораны',
            category=cls.category
        )

        # Создаем тестовую транзакцию
        cls.transaction = Transaction.objects.create(
            date=date.today(),
            status=cls.status,
            operation_type=cls.operation_type,
            category=cls.category,
            subcategory=cls.subcategory,
            amount=1500.00,
            comment='Ужин в ресторане'
        )

    def setUp(self):
        """Выполняется перед каждым тестом"""
        self.client.force_authenticate(user=self.user)

    def test_transaction_list(self):
        url = reverse('transaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Убрали ['results']

    def test_transaction_filter_by_date(self):
        url = f"{reverse('transaction-list')}?date={date.today()}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Убрали ['results']

    def test_transaction_create(self):
        url = reverse('transaction-list')
        data = {
            'date': date.today().isoformat(),
            'status': self.status.id,
            'operation_type': self.operation_type.id,
            'category': self.category.id,
            'amount': '2000.00',
            'comment': 'Обед в кафе'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)

    def test_transaction_update(self):
        url = reverse('transaction-detail', args=[self.transaction.id])
        data = {
            'date': date.today().isoformat(),
            'status': self.status.id,
            'operation_type': self.operation_type.id,
            'category': self.category.id,
            'amount': '1800.00',
            'comment': 'Ужин в ресторане (обновлено)'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.transaction.refresh_from_db()
        self.assertEqual(self.transaction.comment, 'Ужин в ресторане (обновлено)')

    def test_transaction_delete(self):
        url = reverse('transaction-detail', args=[self.transaction.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Transaction.objects.count(), 0)