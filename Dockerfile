FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && pip install -r requirements.txt \
    && apk del build-deps

COPY . /app/

RUN python manage.py collectstatic --noinput \
    && python manage.py migrate --noinput

RUN adduser -D user_api
USER user_api

CMD gunicorn django_movies_api.wsgi:application --bind 0.0.0.0:$PORT
