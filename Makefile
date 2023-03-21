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