#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input

memcached \
    --user=${MEMCACHED_USER:-memcached} \
    --memory-limit=${MEMCACHED_MEMORY:-64} \
    --conn-limit=${MEMCACHED_CONNECTIONS:-1024} \
    --threads=${MEMCACHED_THREADS:-4} \
    --max-reqs-per-event=${MEMCACHED_REQUESTS_PER_EVENT:-20} \
    --daemon

gunicorn \
    --bind 0.0.0.0:8080 \
    --workers=${GUNICORN_WORKERS:-3} \
    --threads=${GUNICORN_THREADS:-1} \
    --worker-tmp-dir=${GUNICORN_TMP_DIR:-/dev/shm} \
    mysite.wsgi:application
