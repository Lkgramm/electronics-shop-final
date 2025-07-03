# 🛒 Интернет-магазин электроники на Django

> Полноценный интернет-магазин электроники, написанный на Django.  
Поддерживает регистрацию пользователей, каталог товаров, корзину, оформление заказов, оплату и API.

---

## 📦 Основные функции

- ✅ Регистрация / Авторизация / Профиль пользователя  
- ✅ Каталог товаров с фильтрами и поиском  
- ✅ Корзина и оформление заказа  
- ✅ История заказов  
- ✅ Админка Django  
- ✅ REST API
- ✅ Интеграция с платежными системами (Stripe)  
- ✅ Деплой через Docker и GitHub Actions  

---

## 🧰 Технологии

| Название        | Версия             |
|----------------|--------------------|
| Python         | 3.13               |
| Django         | 4.2.x              |
| PostgreSQL     | >= 12              |
| Poetry         | ^1.7               |
| Gunicorn       | ^21.2              |
| dj-database-url| ^2.2               |
| Whitenoise     | ^6.6               |
| Stripe SDK     | ^9.0 *(опционально)* |

---

## 🚀 Установка и запуск

### 1. Установка зависимостей

```bash
poetry install
```

### 2. Активация виртуального окружения

```bash
poetry shell
```

### 3. Настройка базы данных

Создайте `.env` файл из шаблона:

```bash
cp .env.example .env
```

И настройте переменные окружения.

### 4. Применение миграций

```bash
python manage.py migrate
```

### 5. Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 6. Запуск сервера

```bash
python manage.py runserver
```

---

## 🐳 Через Docker (разработка)

```bash
docker-compose up --build
```

Открыть: http://localhost:8000

---

## 🔐 Переменные окружения

Пример `.env`:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

DATABASE_URL=postgres://store_user:store_password@db:5432/electronics_store
```

---

## 🌐 API (если используется DRF)

| Endpoint                  | Метод   | Описание                      |
|--------------------------|---------|-------------------------------|
| `GET /api/products/`     | GET     | Список товаров                |
| `GET /api/products/{id}` | GET     | Детали товара                 |
| `POST /api/cart/add`     | POST    | Добавить товар в корзину      |
| `GET /api/orders/`       | GET     | История заказов               |
| `POST /api/orders/create`| POST    | Создать заказ                 |

---

## 💵 Платежи (Stripe)

Если интегрировано:

```env
STRIPE_PUBLIC_KEY=your-public-key
STRIPE_SECRET_KEY=your-secret-key
STRIPE_WEBHOOK_SECRET=your-webhook-secret
```

---

## 📈 CI/CD

Проект поддерживает автоматический деплой через Docker и GitHub Actions.  
Контейнер собирается, пушится в Docker Hub и деплоится на целевой хостинг.

