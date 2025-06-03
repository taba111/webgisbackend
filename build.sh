#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Load initial data
python manage.py loaddata data.json

# Collect static files
python manage.py collectstatic --no-input 