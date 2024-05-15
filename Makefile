MANAGE := poetry run python3 manage.py


install:
	poetry install

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:8000 task_manager.wsgi

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
