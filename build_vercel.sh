#!/usr/bin/env bash
set -o errexit

# Force install requirements to bypass PEP 668 restrictions
pip install -r requirements.txt --break-system-packages

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py seed_universities
