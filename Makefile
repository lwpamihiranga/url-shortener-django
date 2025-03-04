.DEFAULT_GOAL := run 

.PHONY:migrations migrate run
migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver