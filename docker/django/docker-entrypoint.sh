#!/bin/sh

# Start cron in the background
service cron start

# Run Django management commands
# python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput

# Start Django server
python3 manage.py runserver 0.0.0.0:8000
