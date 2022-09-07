#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dci.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if "test" in sys.argv:
        from coverage import Coverage

        cov = Coverage()
        cov.erase()
        cov.start()

    execute_from_command_line(sys.argv)

    if "test" in sys.argv:
        cov.stop()
        cov.combine(strict=True)
        cov.save()
        covered = cov.report()
        if covered < 100:
            sys.exit(1)


if __name__ == "__main__":
    main()
