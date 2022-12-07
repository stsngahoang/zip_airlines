FROM python:3.9-slim-buster

LABEL maintainer="nga.hoang@saigontechology.com"
# Install OS package
RUN mkdir -p /app && \
    apt-get update -y && \
    apt-get install -y build-essential python3-dev \
    libpq-dev libsm6 libxext6 libxrender-dev libglib2.0-0 python-psycopg2 \
    ffmpeg

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

ARG BUILD_ENV

WORKDIR /app/
COPY ./requirements requirements
RUN python3 -m pip install -r requirements/${BUILD_ENV:-dev}.txt --no-cache-dir
COPY src/ .

COPY ./bin/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh

RUN exec "$0"
