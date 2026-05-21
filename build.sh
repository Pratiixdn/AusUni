#!/usr/bin/env bash
set -o errexit

# pip install is handled by Vercel automatically if requirements.txt is present
# but if you are running this as a custom build command:
# pip install -r requirements.txt --break-system-packages
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py seed_universities