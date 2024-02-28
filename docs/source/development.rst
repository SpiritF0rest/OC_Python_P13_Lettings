Development
===========

Technologies
------------

- Python https://www.python.org/ : Version ^3.11
- Django https://docs.djangoproject.com/en/5.0/ : Version ^5.0
- Python-dotenv https://pypi.org/project/python-dotenv/ : Version ^1.0.0
- Sentry-sdk https://pypi.org/project/sentry-sdk/1.35.0/ : Version ^1.39.0
- Whitenoise https://pypi.org/project/whitenoise/ : Version ^6.6.0
- Sphinx https://www.sphinx-doc.org/en/master/index.html : Version ^7.2.6
- Sphinxcontrib-django https://pypi.org/project/sphinxcontrib-django/ : Version ^2.5
- Pytest-django https://pypi.org/project/pytest-django/ : Version ^4.7.0
- Flake8 https://pypi.org/project/flake8/ : Version ^6.1.0
- Coverage https://pypi.org/project/coverage/ : Version ^7.3.2
- Poetry https://python-poetry.org/ : Version 1.7.1
- Docker https://docs.docker.com/get-docker/ : Version 25.0.2

Installation
------------
Prerequisites: Python, Poetry, Sentry

In your directory for the project:

Clone repository from:
    https://github.com/SpiritF0rest/OC_Python_P13_Lettings

Virtual environment and modules
-------------------------------

To install modules:
    :code:`poetry install`

To active the virtual environment (Linux):
    :code:`source $(poetry env info --path)/bin/activate`

To active the virtual environment (Windows Powershell):
    :code:`& ((poetry env info --path) + "\Scripts\activate.ps1")`

To deactive the virtual environment:
    :code:`deactivate`

Dotenv
------
Copy the .env.example in a .env file and fill with the correct data.

- SENTRY_DSN: Expected URL
- SECRET_KEY: Expected String like
    :code:`"very_strong_key"`
- ALLOWED_HOSTS: Expected String like
    :code:`"localhost, 127.0.0.1"`
- CSRF_TRUSTED_ORIGINS: Expected String like
    :code:`"https://site.onrender.com"`

Run
---
:code:`python3 manage.py runserver`

Tests
-----
To test:
    :code:`poetry run pytest`

To generate Flake 8 report:
    :code:`poetry run flake8`

To see coverage:
    :code:`poetry run coverage run -m pytest`
    :code:`poetry run coverage report`
    :code:`poetry run coverage html`

Admin panel
-----------

Go to http://localhost:8000/admin
    - User: admin
    - Password: Abc1234!
