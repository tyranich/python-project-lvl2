install:
	poetry install

force-inst:
	python3 -m pip install --force-reinstall

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run --username ' ' --password ' '

package-inst:
	python3 -m pip install --user dist/*.whl

patch:
	poetry install
	poetry build
	poetry publish --dry-run --username ' ' --password ' '

lint:
	poetry run flake8 gendiff
0
test:
	poetry run pytest -vv

test-cov:
	poetry run pytest --cov=gendiff

test-cov-xml:
	poetry run pytest --cov=gendiff --cov-report xml tests/

test-cov-html:
	poetry run pytest --cov=gendiff --cov-report html tests/