SHELL := /bin/bash

VENV_DIR := .venv
PYTHON   := $(VENV_DIR)/bin/python
PIP      := $(VENV_DIR)/bin/pip
MYPY     := $(VENV_DIR)/bin/mypy
BLACK    := $(VENV_DIR)/bin/black

# Две скрытые метки (файлы-маркеры) для отслеживания состояния
VENV_CREATED := $(VENV_DIR)/.created
DEPS_UPDATED := $(VENV_DIR)/.deps_updated

.PHONY: all check typecheck lint format clean

# 1. Создаем venv, только если папки .venv вообще не существует
$(VENV_CREATED):
	@echo "==> Создаем виртуальное окружение..."
	python3 -m venv $(VENV_DIR)
	@touch $(VENV_CREATED)

# 2. Умная установка: pip запустится ТОЛЬКО если изменился pyproject.toml
$(DEPS_UPDATED): $(VENV_CREATED) pyproject.toml
	@echo "==> [Make обнаружил изменения] Обновляем зависимости..."
	$(PIP) install --upgrade pip
	$(PIP) install requests numpy fastapi mypy black types-requests
	@touch $(DEPS_UPDATED)

# Теперь все таргеты зависят от файла-маркера, а не от .PHONY команды!
typecheck: $(DEPS_UPDATED)
	@echo "==> Проверка типов..."
	$(MYPY) src/

lint: $(DEPS_UPDATED)
	@echo "==> Проверка стиля кода..."
	$(BLACK) --check src/

format: $(DEPS_UPDATED)
	@echo "==> Исправление форматирования..."
	$(BLACK) src/

check: typecheck lint