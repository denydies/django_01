MANAGE = python src/manage.py
PROJECT_DIR=$(shell pwd)
WSGI_PORT=8000
RUN_COMMAND = gunicorn-run

run:
	 cd src && python manage.py runserver 0.0.0.0:8000


make-migrate:
	python src/manage.py makemigrations


migrate:
	python src/manage.py migrate


lint:
	flake8 ./src

check:
	python src/manage.py check

check-migrate:
	python src/manage.py makemigrations --check --dry-run

shell_plus:
	python src/manage.py shell_plus --print-sql

celery:
	 cd src && celery -A core worker -l info

celerybeat:
	 cd src && celery -A core beat -l info

#
#celery_autoscale:
#	cd core &&celery -A core worker --autoscale=4,2 -l info

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/src core.wsgi --timeout 30 --log-level debug --max-requests 10000

collect-static:
	python src/manage.py collectstatic

gunicorn-run-sock:
	gunicorn -w 4 -b unix:/tmp/gunicorn.sock --chdir $(PROJECT_DIR)/src core.wsgi --timeout 30 --log-level debug --max-requests 10000

pytest:
	cd src && pytest

test-all-project:
	cd src && pytest --cov=sport_blog --cov-report=html --cov-fail-under=59



# DOCKER COMMANDS
ps:
	docker-compose ps

docker-run-dev:
	$(eval  RUN_COMMAND=run)
	docker-compose up -d --build
	make copy-static

docker-run-production:
	$(eval RUN_COMMAND=gunicorn-run)
	docker-compose up -d --build
	make copy-static

docker-down:
	docker-compose down

docker-up:
	docker-compose up

copy-static:
	docker exec -it sport_blog-backend python ./src/manage.py collectstatic --noinput
	docker cp sport_blog-backend:/tmp/static_content/static /tmp/static
	docker cp /tmp/static nginx:/etc/nginx
#
#docker-runserver-breakpoint:
#	docker exec -it sport_blog-backend $(MANAGE) runserver 0.0.0.0:9000
