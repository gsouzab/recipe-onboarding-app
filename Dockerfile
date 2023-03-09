FROM python:3.9-alpine3.16

LABEL maintainer="gabriel.souza@travelperk.com"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        app

EXPOSE 8080
USER app
