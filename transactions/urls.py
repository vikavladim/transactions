"""Конфигурация URL-адресов для работы с транзакциями.

Определяет маршруты для:
- Просмотра списка транзакций
- Создания, редактирования и удаления транзакций
- AJAX-эндпоинтов для динамической загрузки категорий и подкатегорий

Attributes:
    app_name (str): Пространство имен для URL-адресов ('transactions').
    urlpatterns (list): Список URL-маршрутов приложения.
"""

from django.urls import path, include
from . import views

app_name = 'transactions'

urlpatterns = [
    # Основные маршруты для работы с транзакциями
    path('', views.transaction_list, name='list'),
    path('create/', views.create_transaction, name='create'),
    path('<int:pk>/update/', views.update_transaction, name='update'),
    path('<int:pk>/delete/', views.delete_transaction, name='delete'),

    # AJAX-эндпоинты для динамических форм
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),

    path('api/', include('transactions.urls_api')),
]