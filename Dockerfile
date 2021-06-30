FROM python:3.9

RUN uname -a
RUN apt update && apt install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY requirements.txt /tmp/requirements.txt
COPY blog/ blog/

RUN pip install -r /tmp/requirements.txt
CMD ["python", "./blog/manage.py", "runserver", "0.0.0.0:8111"]

EXPOSE 8111

#docker run --rm -t -d -p 8001:8111
