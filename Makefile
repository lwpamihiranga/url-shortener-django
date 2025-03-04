.DEFAULT_GOAL := run 

.PHONY:migrations migrate run test
migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver

test:
	python manage.py test