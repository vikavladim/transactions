"""Модуль представлений для работы со справочниками.

Содержит классы и функции для:
- Отображения главной страницы справочников
- CRUD операций для статусов, типов операций, категорий и подкатегорий
- AJAX обработчиков для динамических форм
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from .models import Status, OperationType, Category, SubCategory
from .forms import StatusForm, OperationTypeForm, CategoryForm, SubCategoryForm


class ReferenceView(ListView):
    """Класс-представление для отображения главной страницы справочников.

    Attributes:
        template_name (str): Путь к шаблону страницы.
        context_object_name (str): Имя переменной контекста в шаблоне.

    Methods:
        get_queryset: Возвращает данные для отображения в шаблоне.
    """
    template_name = 'reference/index.html'
    context_object_name = 'reference_data'

    def get_queryset(self):
        """Получает данные для отображения на главной странице справочников.

        Returns:
            dict: Словарь с данными всех справочников, отсортированными по имени.
        """
        return {
            'statuses': Status.objects.all().order_by('name'),
            'operation_types': OperationType.objects.all().order_by('name'),
            'categories': Category.objects.all().order_by('name'),
            'subcategories': SubCategory.objects.all().order_by('name')
        }


def status_create(request):
    """Создание нового статуса.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно создан')
            return redirect('reference:index')
    else:
        form = StatusForm()

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Создание статуса'
    })


def status_update(request, pk):
    """Редактирование существующего статуса.

    Args:
        request: HttpRequest объект.
        pk: id редактируемого статуса.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно обновлен')
            return redirect('reference:index')
    else:
        form = StatusForm(instance=status)

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Редактирование статуса'
    })


def status_delete(request, pk):
    """Удаление статуса.

    Args:
        request: HttpRequest объект.
        pk: id удаляемого статуса.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        messages.success(request, 'Статус успешно удален')
        return redirect('reference:index')

    return render(request, 'reference/confirm_delete.html', {
        'obj': status,
        'type': 'статус'
    })


def operation_type_create(request):
    """Создание нового типа операции.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    if request.method == 'POST':
        form = OperationTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тип операции успешно создан')
            return redirect('reference:index')
    else:
        form = OperationTypeForm()

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Создание типа операции'
    })


def operation_type_update(request, pk):
    """Редактирование существующего типа операции.

    Args:
        request: HttpRequest объект.
        pk: id редактируемого типа операции.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    operation_type = get_object_or_404(OperationType, pk=pk)
    if request.method == 'POST':
        form = OperationTypeForm(request.POST, instance=operation_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тип операции успешно обновлен')
            return redirect('reference:index')
    else:
        form = OperationTypeForm(instance=operation_type)

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Редактирование типа операции'
    })


def operation_type_delete(request, pk):
    """Удаление типа операции.

    Args:
        request: HttpRequest объект.
        pk: id удаляемого типа операции.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    operation_type = get_object_or_404(OperationType, pk=pk)
    if request.method == 'POST':
        operation_type.delete()
        messages.success(request, 'Тип операции успешно удален')
        return redirect('reference:index')

    return render(request, 'reference/confirm_delete.html', {
        'obj': operation_type,
        'type': 'тип операции'
    })


def category_create(request):
    """Создание новой категории.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана')
            return redirect('reference:index')
    else:
        form = CategoryForm()

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Создание категории'
    })


def category_update(request, pk):
    """Редактирование существующей категории.

    Args:
        request: HttpRequest объект.
        pk: id редактируемой категории.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно обновлена')
            return redirect('reference:index')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Редактирование категории'
    })


def category_delete(request, pk):
    """Удаление категории.

    Args:
        request: HttpRequest объект.
        pk: id удаляемой категории.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Категория успешно удалена')
        return redirect('reference:index')

    return render(request, 'reference/confirm_delete.html', {
        'obj': category,
        'type': 'категорию'
    })


def subcategory_create(request):
    """Создание новой подкатегории.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Подкатегория успешно создана')
            return redirect('reference:index')
    else:
        form = SubCategoryForm()
        category_id = request.GET.get('category')
        if category_id:
            form.fields['category'].initial = category_id
            form.fields['category'].queryset = Category.objects.filter(id=category_id)

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Создание подкатегории'
    })


def subcategory_update(request, pk):
    """Редактирование существующей подкатегории.

    Args:
        request: HttpRequest объект.
        pk: id редактируемой подкатегории.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Подкатегория успешно обновлена')
            return redirect('reference:index')
    else:
        form = SubCategoryForm(instance=subcategory)
        form.fields['category'].queryset = Category.objects.filter(id=subcategory.category.id)

    return render(request, 'reference/form.html', {
        'form': form,
        'title': 'Редактирование подкатегории'
    })


def subcategory_delete(request, pk):
    """Удаление подкатегории.

    Args:
        request: HttpRequest объект.
        pk: id удаляемой подкатегории.

    Returns:
        HttpResponse: Результат обработки запроса.
    """
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        subcategory.delete()
        messages.success(request, 'Подкатегория успешно удалена')
        return redirect('reference:index')

    return render(request, 'reference/confirm_delete.html', {
        'obj': subcategory,
        'type': 'подкатегорию'
    })


def load_categories(request):
    """AJAX обработчик для загрузки категорий по типу операции.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: HTML с опциями категорий.
    """
    operation_type_id = request.GET.get('operation_type')
    categories = Category.objects.filter(operation_type_id=operation_type_id).order_by('name')
    return render(request, 'reference/includes/category_options.html', {
        'categories': categories
    })


def load_subcategories(request):
    """AJAX обработчик для загрузки подкатегорий по категории.

    Args:
        request: HttpRequest объект.

    Returns:
        HttpResponse: HTML с опциями подкатегорий.
    """
    category_id = request.GET.get('category')
    subcategories = SubCategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'reference/includes/subcategory_options.html', {
        'subcategories': subcategories
    })