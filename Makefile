MANAGE := poetry run python3 manage.py
PORT ?= 7000
WORKERS ?= 5
.PHONY: install start stop lint shell migrate build test test-coverage staticfiles

install:
	poetry install

start:
	poetry run gunicorn --daemon -w $(WORKERS) -b 0.0.0.0:$(PORT) task_manager.wsgi

stop:
	pkill -f '$(PORT) task_manager.wsgi'

lint:
	poetry run flake8 task_manager --exclude migrations

shell:
	${MANAGE} shell_plus --bpython

migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate

build:
	make migrate
	make staticfiles

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

staticfiles:
	${MANAGE} collectstatic --no-input
