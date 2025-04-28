#!/bin/sh

# Reset the database by clearing all data (use with caution)
# python manage.py flush --no-input

# Install required packages
pip install -r requirements.txt

# Collect static files, clearing old ones
python manage.py collectstatic --no-input --clear

# Apply database migrations
python manage.py migrate