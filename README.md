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
