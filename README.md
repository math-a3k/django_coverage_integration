# django_coverage_integration

This is sample repo to reproduce the problem of integrating coverage.py into Django's manage.py when running tests in parallel.

## Steps to reproduce

- Clone the repo
- ``python -m venv .env && source .env/bin/activate``
- ``pip install -r requirements.txt``
- ``python manage.py test --parallel``
- Note that the generate ``.coverage.[something]``
- Note ``coverage`` run html fails
- ``coverage combine`` works (produces ``.coverage``)
