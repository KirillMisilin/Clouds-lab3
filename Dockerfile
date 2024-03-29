# syntax=docker/dockerfile:1.4

FROM python:3 AS builder
EXPOSE 8000
WORKDIR /first_django
COPY requirements.txt /first_django
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /first_django
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

