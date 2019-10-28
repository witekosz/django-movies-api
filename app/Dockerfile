# python:3-7-alpine causes error with django
FROM python:3.6-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && pip install -r requirements.txt \
    && apk del build-deps

RUN adduser -D user_api
COPY . /usr/src/app/
