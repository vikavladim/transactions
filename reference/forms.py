from django import forms
from .models import Status, OperationType, Category, SubCategory


class StatusForm(forms.ModelForm):
    """Форма для создания и редактирования статусов.

    Attributes:
        model (Status): Модель, с которой связана форма.
        fields (list): Поля, включаемые в форму.
        widgets (dict): Виджеты для полей формы с дополнительными атрибутами.
    """
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статуса'
            })
        }


class OperationTypeForm(forms.ModelForm):
    """Форма для создания и редактирования типов операций.

    Attributes:
        model (OperationType): Модель, с которой связана форма.
        fields (list): Поля, включаемые в форму.
        widgets (dict): Виджеты для полей формы с дополнительными атрибутами.
    """
    class Meta:
        model = OperationType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название типа'
            })
        }


class CategoryForm(forms.ModelForm):
    """Форма для создания и редактирования категорий.

    Attributes:
        model (Category): Модель, с которой связана форма.
        fields (list): Поля, включаемые в форму.
        widgets (dict): Виджеты для полей формы с дополнительными атрибутами.
    """
    class Meta:
        model = Category
        fields = ['name', 'operation_type']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название категории'
            }),
            'operation_type': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class SubCategoryForm(forms.ModelForm):
    """Форма для создания и редактирования подкатегорий с динамической загрузкой категорий.

    Attributes:
        model (SubCategory): Модель, с которой связана форма.
        fields (list): Поля, включаемые в форму.
        widgets (dict): Виджеты для полей формы с дополнительными атрибутами.

    Methods:
        __init__: Инициализирует форму и настраивает queryset для поля category.
    """
    def __init__(self, *args, **kwargs):
        """Инициализирует форму, устанавливает пустой queryset для категорий
        и при необходимости загружает конкретную категорию.

        Args:
            *args: Позиционные аргументы.
            **kwargs: Именованные аргументы.
        """
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['category'].queryset = Category.objects.filter(id=category_id)
            except (ValueError, TypeError):
                pass

    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название подкатегории'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }