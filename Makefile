install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff
test:
    poetry run pytest -vv

test-cov:
	poetry run pytest --cov=gendiff

test-cov-xml:
	poetry run pytest --cov=gendiff --cov-report xml tests/

test-cov-html:
	poetry run pytest --cov=gendiff --cov-report html tests/

.PHONY: install test lint selfcheck check build