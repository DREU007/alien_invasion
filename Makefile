install:
	poetry install

alien_invasion:
	poetry run alien_invasion

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-remove:
	python3 -m pip uninstall alien_invasion

lint:
	poetry run flake8 alien_invasion

test:
	poetry run pytest