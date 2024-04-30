install:
	poetry install

start:
	python manage.py runserver 0.0.0.0:8000

lint:
	poetry run flake8 .