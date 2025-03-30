from django.contrib import admin
from .models import Status, OperationType, Category, SubCategory


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Status.

    Attributes:
        list_display (tuple): Поля, отображаемые в списке объектов.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели OperationType.

    Attributes:
        list_display (tuple): Поля, отображаемые в списке объектов.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Category.

    Attributes:
        list_display (tuple): Поля, отображаемые в списке объектов.
        list_filter (tuple): Поля для фильтрации списка объектов.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """
    list_display = ('name', 'operation_type')
    list_filter = ('operation_type',)
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели SubCategory.

    Attributes:
        list_display (tuple): Поля, отображаемые в списке объектов.
        list_filter (tuple): Поля для фильтрации списка объектов.
        search_fields (tuple): Поля, по которым осуществляется поиск.

    Methods:
        get_operation_type: Возвращает тип операции для подкатегории.
    """
    list_display = ('name', 'category', 'get_operation_type')
    list_filter = ('category', 'category__operation_type')
    search_fields = ('name', 'category__name')

    def get_operation_type(self, obj):
        """Получает тип операции связанной категории.

        Args:
            obj (SubCategory): Объект подкатегории.

        Returns:
            OperationType: Тип операции связанной категории.
        """
        return obj.category.operation_type

    get_operation_type.short_description = 'Тип операции'