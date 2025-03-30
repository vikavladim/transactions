"""Модуль представлений для работы с транзакциями.

Содержит функции для:
- Отображения и фильтрации списка транзакций
- Создания, редактирования и удаления транзакций
- Обработки AJAX-запросов для динамических форм
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .models import Transaction
from .forms import TransactionForm
from reference.models import Status, OperationType, Category, SubCategory


def transaction_list(request):
    """Отображает список транзакций с возможностью фильтрации.

    Поддерживает фильтрацию по:
    - Диапазону дат (по умолчанию текущий месяц)
    - Статусу операции
    - Типу операции (доход/расход)
    - Категории и подкатегории

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: HTML страница с отфильтрованным списком транзакций.
    """
    today = timezone.now().date()
    default_date_from = today.replace(day=1)  # Первое число текущего месяца
    default_date_to = today  # Текущая дата

    # Получаем параметры фильтрации из GET-запроса
    date_from = request.GET.get('date_from', default_date_from.strftime('%Y-%m-%d'))
    date_to = request.GET.get('date_to', default_date_to.strftime('%Y-%m-%d'))
    status_id = request.GET.get('status')
    operation_type_id = request.GET.get('operation_type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')

    # Обработка и валидация дат
    try:
        date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
        date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        date_from = default_date_from
        date_to = default_date_to

    # Базовый запрос с оптимизацией через select_related
    transactions = Transaction.objects.filter(
        date__range=[date_from, date_to]
    ).select_related(
        'status', 'operation_type', 'category', 'subcategory'
    ).order_by('-date', '-created_at')

    # Применение дополнительных фильтров
    if status_id:
        transactions = transactions.filter(status_id=status_id)
    if operation_type_id:
        transactions = transactions.filter(operation_type_id=operation_type_id)
    if category_id:
        transactions = transactions.filter(category_id=category_id)
    if subcategory_id:
        transactions = transactions.filter(subcategory_id=subcategory_id)

    # Получение данных для фильтров
    statuses = Status.objects.all()
    operation_types = OperationType.objects.all()
    categories = Category.objects.filter(
        operation_type_id=operation_type_id) if operation_type_id else Category.objects.all()
    subcategories = SubCategory.objects.filter(category_id=category_id) if category_id else SubCategory.objects.all()

    context = {
        'transactions': transactions,
        'statuses': statuses,
        'operation_types': operation_types,
        'categories': categories,
        'subcategories': subcategories,
        'date_from': date_from.strftime('%Y-%m-%d'),
        'date_to': date_to.strftime('%Y-%m-%d'),
        'default_date_from': default_date_from.strftime('%Y-%m-%d'),
        'default_date_to': default_date_to.strftime('%Y-%m-%d'),
        'selected_status': status_id,
        'selected_operation_type': operation_type_id,
        'selected_category': category_id,
        'selected_subcategory': subcategory_id,
    }
    return render(request, 'transactions/transaction_list.html', context)


def create_transaction(request):
    """Обрабатывает создание новой транзакции.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: Результат обработки формы создания.
    """
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            messages.success(request, f'Транзакция от {transaction.date.strftime("%d.%m.%Y")} создана!')
            return redirect('transactions:list')
    else:
        form = TransactionForm()

    return render(request, 'transactions/transaction_form.html', {
        'form': form,
        'title': 'Создание транзакции'
    })


def update_transaction(request, pk):
    """Обрабатывает редактирование существующей транзакции.

    Args:
        request: HttpRequest объект.
        pk: id редактируемой транзакции.

    Returns:
        HttpResponse: Результат обработки формы редактирования.
    """
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Транзакция обновлена!')
            return redirect('transactions:list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'transactions/transaction_form.html', {
        'form': form,
        'title': 'Редактирование транзакции',
        'transaction': transaction
    })


def delete_transaction(request, pk):
    """Обрабатывает удаление транзакции.

    Args:
        request: HttpRequest объект.
        pk: id удаляемой транзакции.

    Returns:
        HttpResponse: Подтверждение удаления или редирект.
    """
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Транзакция удалена!')
        return redirect('transactions:list')

    return render(request, 'transactions/confirm_delete.html', {
        'transaction': transaction
    })


def load_categories(request):
    """AJAX-обработчик для загрузки категорий по типу операции.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: HTML с вариантами категорий.
    """
    operation_type_id = request.GET.get('operation_type')
    categories = Category.objects.filter(operation_type_id=operation_type_id)
    return render(request, 'transactions/includes/category_options.html', {
        'categories': categories
    })


def load_subcategories(request):
    """AJAX-обработчик для загрузки подкатегорий по категории.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: HTML с вариантами подкатегорий.
    """
    category_id = request.GET.get('category')
    subcategories = SubCategory.objects.filter(category_id=category_id)
    return render(request, 'transactions/includes/subcategory_options.html', {
        'subcategories': subcategories
    })