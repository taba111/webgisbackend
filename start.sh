#!/usr/bin/env bash
# exit on error
set -o errexit

# Set environment variables
export DJANGO_SETTINGS_MODULE=webgis.settings
export PYTHONPATH=/opt/render/project/src
export PORT=${PORT:-10000}
export DJANGO_DEBUG=True
export PYTHONUNBUFFERED=1

echo "Starting Gunicorn with DEBUG mode enabled..."
echo "PYTHONPATH: $PYTHONPATH"
echo "PORT: $PORT"

# Start Gunicorn with proper settings
exec gunicorn webgis.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --threads 2 \
    --timeout 0 \
    --log-level debug \
    --access-logfile - \
    --error-logfile - \
    --capture-output 