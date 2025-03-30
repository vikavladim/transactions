"""Модуль ViewSets для API справочников.

Предоставляет конечные точки REST API для работы со справочниками:
- Статусы
- Типы операций
- Категории
- Подкатегории

Все ViewSets требуют аутентификации пользователя.
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Status, OperationType, Category, SubCategory
from .serializers import StatusSerializer, OperationTypeSerializer, CategorySerializer, SubCategorySerializer


class StatusViewSet(viewsets.ModelViewSet):
    """ViewSet для работы со статусами через API.

    Предоставляет стандартные CRUD операции:
    - Создание (POST)
    - Чтение списка (GET) и деталей (GET /id/)
    - Обновление (PUT, PATCH)
    - Удаление (DELETE)

    Attributes:
        queryset (QuerySet): Набор всех объектов Status.
        serializer_class (StatusSerializer): Сериализатор для модели Status.
        permission_classes (list): Требуется аутентификация.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]


class OperationTypeViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с типами операций через API.

    Предоставляет стандартные CRUD операции:
    - Создание (POST)
    - Чтение списка (GET) и деталей (GET /id/)
    - Обновление (PUT, PATCH)
    - Удаление (DELETE)

    Attributes:
        queryset (QuerySet): Набор всех объектов OperationType.
        serializer_class (OperationTypeSerializer): Сериализатор для модели OperationType.
        permission_classes (list): Требуется аутентификация.
    """
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с категориями через API.

    Предоставляет стандартные CRUD операции:
    - Создание (POST)
    - Чтение списка (GET) и деталей (GET /id/)
    - Обновление (PUT, PATCH)
    - Удаление (DELETE)

    Attributes:
        queryset (QuerySet): Набор всех объектов Category.
        serializer_class (CategorySerializer): Сериализатор для модели Category.
        permission_classes (list): Требуется аутентификация.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class SubCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с подкатегориями через API.

    Предоставляет стандартные CRUD операции:
    - Создание (POST)
    - Чтение списка (GET) и деталей (GET /id/)
    - Обновление (PUT, PATCH)
    - Удаление (DELETE)

    Attributes:
        queryset (QuerySet): Набор всех объектов SubCategory.
        serializer_class (SubCategorySerializer): Сериализатор для модели SubCategory.
        permission_classes (list): Требуется аутентификация.
    """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]