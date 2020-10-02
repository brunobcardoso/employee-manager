FROM python:3.7-alpine3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

RUN apk add --no-cache --virtual .build-deps postgresql-dev gcc musl-dev  \
    && apk add --no-cache libpq git \
    && pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --system --ignore-pipfile --deploy --dev \
    && apk del --no-cache .build-deps