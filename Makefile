.PHONY: install format lint type test check build scan

install:
	python -m pip install -e '.[dev]'

format:
	ruff format src tests
	ruff check --fix src tests

lint:
	ruff format --check src tests
	ruff check src tests

type:
	mypy src

test:
	pytest

check: lint type test

build:
	python -m build

scan:
	agentguard scan src --fail-on medium
