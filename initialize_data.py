"""Скрипт инициализации базовых данных для приложения.

Создает начальные данные в базе данных:
- Статусы транзакций
- Типы операций (доходы/расходы)
- Категории и подкатегории операций

Для использования:
1. Убедитесь, что Django настроен правильно
2. Запустите скрипт: `python initialize_data.py`
"""

import os
import django

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cashflow.settings')
django.setup()

from reference.models import Status, OperationType, Category, SubCategory


def initialize_data():
    """Инициализирует базовые данные в системе.

    Создает следующие данные, если они отсутствуют:
    - Статусы: Бизнес, Личное, Налог
    - Типы операций: Пополнение (доход), Списание (расход)
    - Категории:
      * Для расходов: Инфраструктура, Маркетинг, Зарплата
      * Для доходов: Продажи
    - Подкатегории для соответствующих категорий

    Использует get_or_create для предотвращения дублирования данных.
    """
    # Создание статусов транзакций
    business, _ = Status.objects.get_or_create(name="Бизнес")
    personal, _ = Status.objects.get_or_create(name="Личное")
    tax, _ = Status.objects.get_or_create(name="Налог")

    # Создание типов операций
    income, _ = OperationType.objects.get_or_create(name="Пополнение")
    expense, _ = OperationType.objects.get_or_create(name="Списание")

    # Создание категорий расходов
    infrastructure, _ = Category.objects.get_or_create(
        name="Инфраструктура",
        operation_type=expense
    )
    marketing, _ = Category.objects.get_or_create(
        name="Маркетинг",
        operation_type=expense
    )
    salary, _ = Category.objects.get_or_create(
        name="Зарплата",
        operation_type=expense
    )

    # Создание категории доходов
    sales, _ = Category.objects.get_or_create(
        name="Продажи",
        operation_type=income
    )

    # Создание подкатегорий
    SubCategory.objects.get_or_create(name="VPS", category=infrastructure)
    SubCategory.objects.get_or_create(name="Proxy", category=infrastructure)
    SubCategory.objects.get_or_create(name="Farpost", category=marketing)
    SubCategory.objects.get_or_create(name="Avito", category=marketing)
    SubCategory.objects.get_or_create(name="Офис", category=infrastructure)


if __name__ == "__main__":
    """Точка входа при запуске скрипта напрямую."""
    print("Creating initial data...")
    initialize_data()
    print("Initial data created successfully!")