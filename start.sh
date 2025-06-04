#!/usr/bin/env bash
# exit on error
set -o errexit

# Start Gunicorn
gunicorn webgis.wsgi:application --bind 0.0.0.0:$PORT 