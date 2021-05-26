# Config Nginx.

upstream django {
	server unix:/tmp/gunicorn.sock fail_timeout=0;
}
server {
	listen 80;
	listen [::]:80;
	server_name 127.0.0.1 sport.com;

	location = /favicon.ico { access_log off; log_not_found off; }

	location /static/ {
		root /home/pds/wks/git/django_01/static_content;
	}

	location / {
		proxy_pass http://django;
	}
}

# Запуск gunicorn на port - 127.0.0.1:8080
gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000

# Запуск gunicorn на unix:/tmp/gunicorn.sock
gunicorn -w 4 -b unix:/tmp/gunicorn.sock --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000
