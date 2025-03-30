from rest_framework import serializers
from .models import Status, OperationType, Category, SubCategory


class StatusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Status."""
    class Meta:
        model = Status
        fields = '__all__'


class OperationTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели OperationType."""
    class Meta:
        model = OperationType
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""
    operation_type = serializers.PrimaryKeyRelatedField(
        queryset=OperationType.objects.all(),
        required=True
    )

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели SubCategory."""
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True
    )

    class Meta:
        model = SubCategory
        fields = '__all__'