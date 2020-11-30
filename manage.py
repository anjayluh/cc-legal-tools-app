#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if "DATABASE_URL" in os.environ:
        # Dokku or similar
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cc_licenses.settings.deploy")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cc_licenses.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
