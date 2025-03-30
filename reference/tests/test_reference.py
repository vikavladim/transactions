from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from reference.models import Status, OperationType, Category, SubCategory

User = get_user_model()


class ReferenceAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)

        # Создаем OperationType
        self.operation_type = OperationType.objects.create(name="Test Operation")

        # Создаем Category
        self.category1 = Category.objects.create(
            name="Category 1",
            operation_type=self.operation_type
        )
        self.category2 = Category.objects.create(
            name="Category 2",
            operation_type=self.operation_type
        )

        # Создаем Status
        self.status1 = Status.objects.create(name="Status 1")
        self.status2 = Status.objects.create(name="Status 2")

        # Создаем SubCategory
        self.subcategory = SubCategory.objects.create(
            name="SubCategory 1",
            category=self.category1
        )


class StatusViewSetTests(ReferenceAPITestCase):
    def test_list_statuses(self):
        url = reverse('status-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual({s['name'] for s in response.data}, {'Status 1', 'Status 2'})

    def test_create_status(self):
        url = reverse('status-list')
        data = {'name': 'New Status'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(), 3)
        self.assertTrue(Status.objects.filter(name='New Status').exists())

    def test_create_status_invalid_data(self):
        url = reverse('status-list')
        data = {'name': ''}  # invalid data
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CategoryViewSetTests(ReferenceAPITestCase):
    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual({c['name'] for c in response.data}, {'Category 1', 'Category 2'})

    def test_create_category(self):
        url = reverse('category-list')
        data = {
            'name': 'New Category',
            'operation_type': self.operation_type.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)
        self.assertTrue(Category.objects.filter(name='New Category').exists())

    def test_create_category_invalid_data(self):
        url = reverse('category-list')
        data = {
            'name': '',
            'operation_type': self.operation_type.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SubCategoryViewSetTests(ReferenceAPITestCase):
    def test_list_subcategories(self):
        url = reverse('subcategory-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'SubCategory 1')

    def test_create_subcategory(self):
        url = reverse('subcategory-list')
        data = {
            'name': 'New SubCategory',
            'category': self.category1.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCategory.objects.count(), 2)
        self.assertTrue(SubCategory.objects.filter(name='New SubCategory').exists())
        self.assertEqual(SubCategory.objects.get(name='New SubCategory').category.id, self.category1.id)

    def test_create_subcategory_invalid_data(self):
        url = reverse('subcategory-list')
        # Missing required category field
        data = {
            'name': 'Invalid SubCategory'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class OperationTypeViewSetTests(ReferenceAPITestCase):
    def test_list_operation_types(self):
        url = reverse('operationtype-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Operation')

    def test_create_operation_type(self):
        url = reverse('operationtype-list')
        data = {'name': 'New Operation Type'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OperationType.objects.count(), 2)
        self.assertTrue(OperationType.objects.filter(name='New Operation Type').exists())