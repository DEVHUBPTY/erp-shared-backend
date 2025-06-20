.PHONY: help install install-dev build clean test lint format docs publish example

help: ## Mostrar esta ayuda
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Instalar el paquete en modo desarrollo
	poetry install

install-dev: ## Instalar con dependencias de desarrollo
	poetry install --with dev

build: ## Construir el paquete
	poetry build

clean: ## Limpiar archivos de construcción
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .coverage htmlcov/

test: ## Ejecutar tests
	poetry run pytest

test-cov: ## Ejecutar tests con cobertura
	poetry run pytest --cov=shared --cov-report=html --cov-report=term-missing

lint: ## Ejecutar linters
	poetry run flake8 shared/
	poetry run mypy shared/

format: ## Formatear código
	poetry run black shared/
	poetry run isort shared/

docs: ## Generar documentación
	poetry run mkdocs build

publish: ## Publicar en PyPI (requiere configuración previa)
	poetry publish

example: ## Ejecutar ejemplo de uso
	python3 examples/basic_usage.py

check: ## Verificar que el paquete se puede importar
	python3 -c "import shared; print(f'Paquete importado: {shared.__version__}')"

all: clean install-dev format lint test build ## Ejecutar todo el pipeline de desarrollo 