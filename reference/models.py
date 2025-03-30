from django.db import models


class Status(models.Model):
    """Модель статуса операции.

    Attributes:
        name (CharField): Название статуса (уникальное поле).

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.

    Methods:
        __str__: Возвращает строковое представление объекта.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        """Строковое представление статуса.

        Returns:
            str: Название статуса.
        """
        return self.name


class OperationType(models.Model):
    """Модель типа операции.

    Attributes:
        name (CharField): Название типа операции (уникальное поле).

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.

    Methods:
        __str__: Возвращает строковое представление объекта.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"

    def __str__(self):
        """Строковое представление типа операции.

        Returns:
            str: Название типа операции.
        """
        return self.name


class Category(models.Model):
    """Модель категории операции.

    Attributes:
        name (CharField): Название категории.
        operation_type (ForeignKey): Ссылка на тип операции.

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.
        unique_together (tuple): Комбинация полей, которые должны быть уникальными.

    Methods:
        __str__: Возвращает строковое представление объекта.
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
        verbose_name="Тип операции"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ('name', 'operation_type')

    def __str__(self):
        """Строковое представление категории.

        Returns:
            str: Название категории с указанием типа операции.
        """
        return f"{self.name} ({self.operation_type})"


class SubCategory(models.Model):
    """Модель подкатегории операции.

    Attributes:
        name (CharField): Название подкатегории.
        category (ForeignKey): Ссылка на родительскую категорию.

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.
        unique_together (tuple): Комбинация полей, которые должны быть уникальными.

    Methods:
        __str__: Возвращает строковое представление объекта.
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ('name', 'category')

    def __str__(self):
        """Строковое представление подкатегории.

        Returns:
            str: Название подкатегории с указанием родительской категории.
        """
        return f"{self.name} ({self.category})"