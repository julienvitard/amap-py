#!/usr/bin/env python
import os
import sys

# ensure Python3 don't write any __pycache__ into current directory
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amapy.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
