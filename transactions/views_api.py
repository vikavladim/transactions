"""ViewSet для работы с транзакциями через REST API.

Предоставляет полный набор CRUD операций для транзакций с поддержкой:
- Фильтрации по различным полям
- Поиска по комментариям и суммам
- Сортировки по дате, сумме и времени создания
- Разных сериализаторов для чтения и записи
"""

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transaction
from .serializers import TransactionSerializer, TransactionCreateSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet для управления транзакциями через API.

    Attributes:
        queryset (QuerySet): Набор транзакций, отсортированный по дате (новые сначала).
        permission_classes (list): Требуется аутентификация пользователя.
        filter_backends (list): Подключенные бэкенды фильтрации.
        filterset_fields (list): Поля для точной фильтрации.
        search_fields (list): Поля для поиска по подстроке.
        ordering_fields (list): Поля для сортировки результатов.

    Methods:
        get_serializer_class: Выбирает сериализатор в зависимости от действия.
    """

    queryset = Transaction.objects.all().order_by('-date')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'operation_type', 'category', 'subcategory', 'date']
    search_fields = ['comment', 'amount']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_serializer_class(self):
        """Определяет класс сериализатора в зависимости от типа запроса.

        Для операций создания и обновления использует TransactionCreateSerializer,
        для остальных операций - TransactionSerializer с вложенными данными.

        Returns:
            Serializer: Класс сериализатора в зависимости от действия.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return TransactionCreateSerializer
        return TransactionSerializer