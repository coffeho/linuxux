.PHONY: help install install-dev test lint format type-check clean build upload-test all

PYTHON := python3
PIP := $(PYTHON) -m pip

help:
	@echo "Доступные команды:"
	@echo "  make install-dev  - Установить зависимости"
	@echo "  make test         - Запустить тесты"
	@echo "  make lint         - Проверить код"
	@echo "  make format       - Форматировать код"
	@echo "  make build        - Собрать пакет"
	@echo "  make all          - Выполнить все проверки"

install-dev:
	@echo "=== Установка зависимостей ==="
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e .
	@echo "✓ Зависимости установлены"

test:
	@echo "=== Запуск тестов ==="
	$(PYTHON) -m pytest tests/ -v --cov=awesome_calculator --cov-report=term-missing

lint:
	@echo "=== Проверка стиля ==="
	$(PYTHON) -m flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503

format:
	@echo "=== Форматирование кода ==="
	$(PYTHON) -m black src/ tests/

type-check:
	@echo "=== Проверка типов ==="
	$(PYTHON) -m mypy src/ || true

clean:
	@echo "=== Очистка ==="
	rm -rf build/ dist/ src/*.egg-info
	rm -rf .pytest_cache/ .mypy_cache/ .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "✓ Очистка завершена"

build: clean
	@echo "=== Сборка пакета ==="
	$(PYTHON) -m build
	@echo "✓ Пакет собран"
	@ls -lh dist/

upload-test: build
	@echo "=== Загрузка на test.pypi.org ==="
	$(PYTHON) -m twine check dist/*
	$(PYTHON) -m twine upload --repository testpypi dist/*
	@echo "✓ Загружено на test.pypi.org"

all: install-dev format lint type-check test build
	@echo ""
	@echo "=========================================="
	@echo "✓ Все проверки пройдены успешно!"
	@echo "=========================================="
