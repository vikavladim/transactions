from django.urls import path, include
from . import views

app_name = 'reference'

urlpatterns = [
    # Основное представление справочников.
    path('', views.ReferenceView.as_view(), name='index'),

    # API URL
    path('api/', include('reference.urls_api')),

    # Маршруты для работы со статусами.
    path('status/add/', views.status_create, name='status_create'),
    path('status/<int:pk>/edit/', views.status_update, name='status_update'),
    path('status/<int:pk>/delete/', views.status_delete, name='status_delete'),

    # Маршруты для работы с типами операций.
    path('operation-type/add/', views.operation_type_create, name='operation_type_create'),
    path('operation-type/<int:pk>/edit/', views.operation_type_update, name='operation_type_update'),
    path('operation-type/<int:pk>/delete/', views.operation_type_delete, name='operation_type_delete'),

    # Маршруты для работы с категориями.
    path('category/add/', views.category_create, name='category_create'),
    path('category/<int:pk>/edit/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Маршруты для работы с подкатегориями.
    path('subcategory/add/', views.subcategory_create, name='subcategory_create'),
    path('subcategory/<int:pk>/edit/', views.subcategory_update, name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', views.subcategory_delete, name='subcategory_delete'),

    # AJAX-эндпоинты для динамических форм.
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]