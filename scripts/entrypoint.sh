#!/bin/bash

# Apply database migrations
set -e # exit if errors happen anywhere
python manage.py collectstatic --noinput
python manage.py migrate

# Start Django development server with Watchdog
#watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- ./manage.py runserver 0.0.0.0:8000

uwsgi --http :8000 --master --enable-threads --module Kymstore.wsgi
