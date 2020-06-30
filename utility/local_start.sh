#!/bin/sh

set -o errexit
# shellcheck disable=SC2039
set -o pipefail
set -o nounset
set -o xtrace

# collect static files
#python manage.py collectstatic --noinput

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
#daphne -b 0.0.0.0 -p 8000 --ws-protocol "graphql-ws" --proxy-headers config.asgi:application
#redis-server --daemonize yes
#python manage.py runworker channels
#python manage.py runserver 0.0.0.0:8000