startserver:
	poetry run python manage.py runserver
	
install:
	poetry install
	
selfcheck:
	poetry check
	
makemigrate:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate
	
test:
	poetry run python manage.py test
	
lint:
	poetry run flake8 task_manager

check: selfcheck test lint

makemessages:
	poetry run django-admin makemessages -l ru
	
compilemessages:
	poetry run django-admin compilemessages --ignore .venv