# Pull base image
FROM python:3.10.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
# Unistall django rest framework
# RUN pipenv uninstall djangorestframework

# Copy project
COPY . /code/