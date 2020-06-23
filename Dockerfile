FROM python:3.8.3-alpine3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps postgresql-dev gcc musl-dev  \
    && apk add --no-cache libpq git \
    && pip install pipenv==2018.11.26 \
    && pipenv install --system --deploy --dev \
    && apk del --no-cache .build-deps