# CashFlow - Система учета финансовых операций
## 🚀 Быстрый старт
### 1. Установка зависимостей
```bash
python -m venv .venv
source .venv/bin/activate      # Активация (Linux/Mac)
.\.venv\Scripts\activate       # Активация (Windows)
pip install -r requirements.txt
```
### 2. Настройка базы данных
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python initialize_data.py
```
### 3. Запуск сервера
```bash
python manage.py runserver
```
- Доступно по адресу: http://localhost:8000
- Админка: http://localhost:8000/admin
- Документация: http://localhost:8000/admin/doc
- 
### 4. Запуск тестов
```bash
python manage.py test reference.tests
python manage.py test transactions.tests
```

## 📂 Структура проекта
```angular2html
cashflow/
├── .venv/ # Виртуальное окружение
│
├── cashflow/ # Основной пакет Django
│ ├── init.py
│ ├── asgi.py # ASGI-конфигурация
│ ├── settings.py # Настройки проекта
│ ├── urls.py # Главные URL-маршруты
│ └── wsgi.py # WSGI-конфигурация
│
├── reference/ # Приложение справочников
│ ├── migrations/ # Миграции БД
│ ├── templates/ # Шаблоны
│ │ └── reference/
│ │ ├── index.html # Главная страница
│ │ ├── form.html # Формы редактирования
│ │ └── ... # Другие шаблоны
│ ├── init.py
│ ├── admin.py # Админка
│ ├── apps.py # Конфиг приложения
│ ├── forms.py # Формы
│ ├── models.py # Модели данных
│ ├── serializers.py # Сериализаторы API
│ ├── urls.py # URL приложения
│ ├── views.py # Обычные представления
│ └── views_api.py # API представления
│
├── transactions/ # Приложение транзакций
│ ├── migrations/ # Миграции БД
│ ├── templates/ # Шаблоны
│ │ └── transactions/
│ │ ├── list.html # Список транзакций
│ │ ├── form.html # Форма транзакции
│ │ └── ... # Другие шаблоны
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ ├── views.py
│ └── views_api.py
│
├── static/ # Статические файлы
│ ├── css/
│ │ └── style.css # Основные стили
│ └── js/
│ ├── reference.js # JS для справочников
│ └── transactions.js # JS для транзакций
│
├── templates/ # Глобальные шаблоны
│ └── base.html # Базовый шаблон
│
├── .gitignore # Игнорируемые файлы
├── initialize_data.py # Инициализация тестовых данных
├── manage.py # Утилита управления
├── README.md # Документация
└── requirements.txt # Зависимости
```
## 🌐 API Endpoints
Основные методы:
- GET /api/transactions/ - Список транзакций
- POST /api/transactions/ - Создание транзакции
- GET /api/categories/ - Список категорий
- GET /api/operation-types/ - Типы операций
### Примеры запроса:
```bash
curl -X POST http://localhost:8000/api/transactions/ \
-H "Content-Type: application/json" \
-d '{"date":"2023-01-01","amount":"1000.00","category":1}'
```
## 🔧 Технологии
- Backend: Django 4.2 + DRF 3.14
- Frontend: Bootstrap 5 + jQuery
- База данных: SQLite (по умолчанию)
## 🛠 Требования
- Python 3.10+
- Установленный pip
## ⚠️ Устранение проблем
1. Ошибки миграций:
```bash
python manage.py makemigrations
python manage.py migrate
```
2. Очистка базы:
```bash
rm db.sqlite3
python initialize_data.py
```