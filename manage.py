#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import os
import json
import ee

# Read credentials from environment variable
credentials_str = os.environ['EE_CREDENTIALS']
credentials = json.loads(credentials_str)

# Save to a temp file (needed for ee.ServiceAccountCredentials)
with open("earthengine-credentials.json", "w") as f:
    json.dump(credentials, f)

# Authenticate
ee.Initialize()
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sentinel_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
