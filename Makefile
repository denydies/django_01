#MANAGE = python blog/manage.py
PROJECT_DIR=$(shell pwd)
WSGI_PORT=8080

run:
	 cd blog && python manage.py runserver 0.0.0.0:8000


make-migrate:
	python blog/manage.py makemigrations


migrate:
	python blog/manage.py migrate


lint:
	flake8 ./blog

check:
	python blog/manage.py check

check-migrate:
	python blog/manage.py makemigrations --check --dry-run

shell_plus:
	python blog/manage.py shell_plus --print-sql

#celery:
	# celery -A blog worker -l info
#
#celery_autoscale:
#		celery -A blog worker --autoscale=4,2 -l info

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000

collect-static:
	python blog/manage.py collectstatic

gunicorn-run-sock:
	gunicorn -w 4 -b unix:/tmp/gunicorn.sock --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000