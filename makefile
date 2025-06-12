# Use bash shell
SHELL := /bin/bash

# Variables
PYTHON = python
VENV_ACTIVATE = source venv/Scripts/activate

# Targets

.PHONY: help venv install lint format typecheck test all

help:
	@echo "Available commands:"
	@echo "  make venv        - Create virtual environment"
	@echo "  make install     - Install requirements"
	@echo "  make lint        - Run flake8 linter"
	@echo "  make format      - Format code with Black"
	@echo "  make typecheck   - Run mypy type checker"
	@echo "  make test        - Run tests (if pytest is added)"
	@echo "  make all         - Run lint, format, typecheck"

venv:
	$(PYTHON) -m venv venv

install:
	$(VENV_ACTIVATE) && pip install -r requirements.txt

lint:
	$(VENV_ACTIVATE) && flake8 src

format:
	$(VENV_ACTIVATE) && black src

typecheck:
	$(VENV_ACTIVATE) && mypy src

test:
	$(VENV_ACTIVATE) && pytest tests

all: lint format typecheck
