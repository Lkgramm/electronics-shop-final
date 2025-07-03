# Путь к manage.py
DJANGO_MANAGE = poetry run python manage.py

# Основные команды
.PHONY: help install run migrate makemigrations createsuperuser shell test coverage lint

help:
	@echo "Основные команды:"
	@echo "  make install           - Установить зависимости через poetry"
	@echo "  make run               - Запустить сервер Django"
	@echo "  make migrate           - Применить миграции"
	@echo "  make makemigrations    - Создать миграции"
	@echo "  make createsuperuser   - Создать суперпользователя"
	@echo "  make shell             - Открыть Django shell"
	@echo "  make test              - Запустить тесты через pytest"
	@echo "  make coverage          - Покрытие кода (pytest + coverage)"
	@echo "  make lint              - Проверка PEP8 (если есть flake8/ruff)"
	@echo "  make env               - Создать .env файл (если отсутствует)"

install:
	poetry install

run:
	$(DJANGO_MANAGE) runserver

migrate:
	$(DJANGO_MANAGE) migrate

makemigrations:
	$(DJANGO_MANAGE) makemigrations

createsuperuser:
	$(DJANGO_MANAGE) createsuperuser

shell:
	$(DJANGO_MANAGE) shell

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=. --cov-report=term --cov-report=html

lint:
	poetry run flake8 . || echo "flake8 не установлен. Добавьте в pyproject.toml, если нужно."

demo:
	poetry run python manage.py runscript demo_products

env:
	@if not exist .env (
		copy .env.example .env
	) else (
		echo ".env уже существует"
	)
