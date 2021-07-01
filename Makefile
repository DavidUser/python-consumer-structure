# Local
RUNNER ?= PYTHONPATH=./src poetry run
MODULES ?= src tests

black:
	$(RUNNER) black $(MODULES)

black-check:
	$(RUNNER) black --check $(MODULES)

flake8:
	$(RUNNER) flake8 $(MODULES)

mypy:
	$(RUNNER) mypy --ignore-missing-imports --strict-optional $(MODULES)

lint: black-check flake8 mypy

test: requirements
	$(RUNNER) pytest --tb=native tests

watch-tests: requirements
	find . -name '*.py' | entr poetry run pytest --tb=short -vv

requirements:
	poetry install

.PHONY: requirements
