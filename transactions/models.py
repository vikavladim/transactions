from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    """Модель финансовой транзакции.

    Хранит информацию о финансовых операциях с привязкой к справочникам:
    - Статус операции
    - Тип операции (доход/расход)
    - Категория и подкатегория
    - Сумма и дата операции

    Attributes:
        date (DateField): Дата проведения операции.
        status (ForeignKey): Ссылка на статус операции.
        operation_type (ForeignKey): Тип операции (доход/расход).
        category (ForeignKey): Категория операции.
        subcategory (ForeignKey): Подкатегория операции (опционально).
        amount (DecimalField): Сумма операции.
        comment (TextField): Комментарий к операции.
        created_at (DateTimeField): Дата создания записи.
        updated_at (DateTimeField): Дата последнего обновления.
    """

    date = models.DateField(
        verbose_name="Дата операции",
        default=timezone.now,
        help_text="Дата проведения финансовой операции"
    )
    status = models.ForeignKey(
        'reference.Status',
        on_delete=models.PROTECT,
        verbose_name="Статус",
        help_text="Текущий статус проведения операции"
    )
    operation_type = models.ForeignKey(
        'reference.OperationType',
        on_delete=models.PROTECT,
        verbose_name="Тип операции",
        help_text="Тип операции - доход или расход"
    )
    category = models.ForeignKey(
        'reference.Category',
        on_delete=models.PROTECT,
        verbose_name="Категория",
        help_text="Основная категория операции"
    )
    subcategory = models.ForeignKey(
        'reference.SubCategory',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Подкатегория",
        help_text="Дополнительная детализация категории (необязательно)"
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма",
        help_text="Сумма операции с точностью до копеек"
    )
    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий",
        help_text="Дополнительная информация об операции"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания записи в системе"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата последнего обновления записи"
    )

    class Meta:
        """Мета-настройки модели Transaction.

        Attributes:
            verbose_name (str): Человекочитаемое имя в единственном числе.
            verbose_name_plural (str): Человекочитаемое имя во множественном числе.
            ordering (list): Порядок сортировки по умолчанию (по дате в обратном порядке).
        """
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
        ordering = ['-date']

    def __str__(self):
        """Строковое представление транзакции.

        Returns:
            str: Описание транзакции в формате "Дата - Сумма (Категория)".
        """
        return f"{self.date} - {self.amount} руб. ({self.category})"

    def save(self, *args, **kwargs):
        """Переопределение метода сохранения с валидацией связей.

        Проверяет:
        - Соответствие категории типу операции
        - Соответствие подкатегории выбранной категории (если подкатегория указана)

        Raises:
            ValueError: Если обнаружены несоответствия в связях между объектами.
        """
        if self.category.operation_type != self.operation_type:
            raise ValueError(
                f"Категория '{self.category}' не соответствует "
                f"типу операции '{self.operation_type}'"
            )

        if self.subcategory and self.subcategory.category != self.category:
            raise ValueError(
                f"Подкатегория '{self.subcategory}' не соответствует "
                f"категории '{self.category}'"
            )

        super().save(*args, **kwargs)