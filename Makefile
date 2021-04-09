run:
	 cd blog && python manage.py runserver


make-migrate:
	python blog/manage.py makemigrations


migrate:
	python blog/manage.py migrate


lint:
	flake8 .