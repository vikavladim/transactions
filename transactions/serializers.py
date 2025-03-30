from rest_framework import serializers
from .models import Transaction
from reference.serializers import StatusSerializer, OperationTypeSerializer, CategorySerializer, SubCategorySerializer


class TransactionSerializer(serializers.ModelSerializer):
    """Сериализатор для детального отображения транзакций.

    Включает вложенные сериализаторы для связанных моделей:
    - Статус
    - Тип операции
    - Категория
    - Подкатегория (если указана)

    Attributes:
        status (StatusSerializer): Вложенный сериализатор статуса.
        operation_type (OperationTypeSerializer): Вложенный сериализатор типа операции.
        category (CategorySerializer): Вложенный сериализатор категории.
        subcategory (SubCategorySerializer): Вложенный сериализатор подкатегории.

    Meta:
        model (Transaction): Связь с моделью Transaction.
        fields (str): Все поля модели.
        read_only_fields (tuple): Поля только для чтения (даты создания и обновления).
    """
    status = StatusSerializer(read_only=True)
    operation_type = OperationTypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class TransactionCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления транзакций.

    Использует базовый функционал ModelSerializer без вложенных сериализаторов,
    что позволяет принимать ID связанных объектов вместо полных вложенных структур.

    Meta:
        model (Transaction): Связь с моделью Transaction.
        fields (str): Все поля модели.
    """

    class Meta:
        model = Transaction
        fields = '__all__'