from django import forms
from reference.models import SubCategory
from .models import Transaction


class TransactionForm(forms.ModelForm):
    """Форма для создания и редактирования транзакций.

    Настраивает виджеты полей и динамически управляет доступными подкатегориями
    в зависимости от выбранной категории.

    Attributes:
        model (Transaction): Модель, связанная с формой.
        fields (list): Поля модели, включаемые в форму.

    Methods:
        __init__: Инициализирует форму, настраивает виджеты и динамические queryset'ы.
    """

    def __init__(self, *args, **kwargs):
        """Инициализация формы с настройкой виджетов и динамических зависимостей.

        Настройки включают:
        - Установку виджета DateInput для поля даты
        - Настройку Textarea для поля комментария
        - Добавление классов Bootstrap для всех полей
        - Динамическое управление доступными подкатегориями
        - Сделать поле подкатегории необязательным

        Args:
            *args: Позиционные аргументы.
            **kwargs: Именованные аргументы.
        """
        super().__init__(*args, **kwargs)

        # Настройка виджета для поля даты
        self.fields['date'].widget = forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        )

        # Настройка виджета для поля комментария
        self.fields['comment'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3
        })

        # Добавление класса form-control для основных полей
        for field in ['status', 'operation_type', 'category', 'subcategory', 'amount']:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        # Поле подкатегории необязательное
        self.fields['subcategory'].required = False

        # Динамическое управление доступными подкатегориями
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(
                    category_id=category_id
                ).order_by('name')
            except (ValueError, TypeError):
                pass  # Оставляем пустой queryset при невалидных данных
        elif self.instance.pk:
            # Для существующей транзакции показываем подкатегории текущей категории
            self.fields['subcategory'].queryset = (
                self.instance.category.subcategory_set.all().order_by('name')
            )
        else:
            # Для новой транзакции без выбранной категории - пустой список
            self.fields['subcategory'].queryset = SubCategory.objects.none()

    class Meta:
        model = Transaction
        fields = [
            'date',
            'status',
            'operation_type',
            'category',
            'subcategory',
            'amount',
            'comment'
        ]