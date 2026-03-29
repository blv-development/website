#!/bin/sh
set -e

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 blvd/manage.py makemigrations --check --dry-run
python3 blvd/manage.py collectstatic --noinput
python3 blvd/manage.py migrate --noinput
