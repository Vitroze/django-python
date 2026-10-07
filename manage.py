#!/usr/bin/env python
"""Utilitaire en ligne de commande de Django (python manage.py runserver)."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        sys.argv.append("runserver")

    main()
