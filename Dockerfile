FROM python:3.9-slim

# install sql server odbc driver
RUN apt-get update && apt-get install -y \
    curl apt-transport-https gnupg2 debconf-utils build-essential

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry install
