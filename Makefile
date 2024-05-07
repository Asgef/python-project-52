MANAGE := poetry run python3 manage.py


install:
	poetry install

start:
	${MANAGE} runserver 0.0.0.0:8000

lint:
	poetry run flake8 task_manager --exclude migrations

shell:
	${MANAGE} shell_plus --bpython

migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate

test:
	poetry run python3 manage.py test
