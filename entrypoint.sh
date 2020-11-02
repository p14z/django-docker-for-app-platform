#!/bin/sh

cd mysite

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages

gunicorn --bind 0.0.0.0:8080 --workers 3 mysite.wsgi:application
