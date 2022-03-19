#!/bin/sh

while ! nc -z db 5432; do
  sleep 0.1
done

python app/manage.py flush --no-input
python app/manage.py migrate
python app/manage.py collectstatic --noinput
exec "$@"