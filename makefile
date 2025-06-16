SHELL := /bin/bash

PYTHON := python
VENV_DIR := venv
VENV_ACTIVATE := source $(VENV_DIR)/Scripts/activate

.PHONY: help venv clean-venv clean-cache install lint format typecheck run all

help:
	@echo "Available commands:"
	@echo "  make venv         - Create virtual environment"
	@echo "  make clean-venv   - Delete virtual environment"
	@echo "  make clean-cache  - Delete __pycache__ and *.pyc files"
	@echo "  make install      - Install dependencies from requirements.txt"
	@echo "  make lint         - Run flake8 linter"
	@echo "  make format       - Format code with Black"
	@echo "  make typecheck    - Run mypy static type checker"
	@echo "  make run          - Run main module (python -m src.main)"
	@echo "  make all          - Run lint, format, typecheck"

venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		$(PYTHON) -m venv $(VENV_DIR); \
		echo "venv created."; \
	else \
		echo "venv already exists. Run 'make clean-venv' to recreate."; \
	fi

clean-venv:
	@if [ -d "$(VENV_DIR)" ]; then \
		rm -rf $(VENV_DIR); \
		echo "venv deleted."; \
	else \
		echo "No venv found to delete."; \
	fi

clean-cache:
	@echo "Removing __pycache__, *.pyc and *.pyo files..."
	@find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	@find . -type f -name "*.py[co]" -delete 2>/dev/null || true
	@echo "✅ Python cache cleaned."

install:
	@$(VENV_ACTIVATE) && pip install -r requirements.txt

lint:
	@$(VENV_ACTIVATE) && flake8 src

format:
	@$(VENV_ACTIVATE) && black src

typecheck:
	@$(VENV_ACTIVATE) && mypy src

run:
	@$(VENV_ACTIVATE) && python -m src.main

all: lint format typecheck
