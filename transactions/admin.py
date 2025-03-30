from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Transaction.

    Настройки отображения и функциональности транзакций в админ-панели Django.

    Attributes:
        list_display (tuple): Поля, отображаемые в списке транзакций.
        list_filter (tuple): Поля для фильтрации списка транзакций.
        search_fields (tuple): Поля для поиска по транзакциям.
        date_hierarchy (str): Поле для иерархической навигации по датам.
        ordering (tuple): Поля для сортировки транзакций по умолчанию.
        fieldsets (tuple): Группировка полей на форме редактирования.
    """
    list_display = (
        'date',
        'status',
        'operation_type',
        'category',
        'subcategory',
        'amount',
        'created_at'
    )
    list_filter = (
        'status',
        'operation_type',
        'category',
        'subcategory'
    )
    search_fields = (
        'comment',
        'amount'
    )
    date_hierarchy = 'date'
    ordering = (
        '-date',
        '-created_at'
    )
    fieldsets = (
        (None, {
            'fields': (
                'date',
                'status',
                'operation_type',
                'amount'
            )
        }),
        ('Категории', {
            'fields': (
                'category',
                'subcategory'
            )
        }),
        ('Дополнительно', {
            'fields': ('comment',),
            'classes': ('collapse',)
        })
    )

    def get_queryset(self, request):
        """Оптимизация запроса к БД через select_related.

        Args:
            request: HttpRequest объект.

        Returns:
            QuerySet: Оптимизированный queryset с уменьшенным числом запросов к БД.
        """
        return super().get_queryset(request).select_related(
            'status',
            'operation_type',
            'category',
            'subcategory'
        )