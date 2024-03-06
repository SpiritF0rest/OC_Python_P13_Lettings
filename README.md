# :desktop_computer: Lettings :desktop_computer:

Orange-county-letting’s is a start-up in the real estate rental industry. 

***
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Tests](#tests)
5. [Admin](#admin)
6. [Database](#database)
7. [Deployment](#deployment)

### :newspaper: General Info :newspaper:
***
It is an OpenClassrooms project whose goal is to scale an existing application using a modular architecture and deploy it.

### :briefcase: Technologies :briefcase:
*** 
- [Python](https://www.python.org/): Version ^3.11
- [Django](https://docs.djangoproject.com/en/5.0/): Version ^5.0
- [Python-dotenv](https://pypi.org/project/python-dotenv/): Version ^1.0.0
- [Sentry-sdk](https://pypi.org/project/sentry-sdk/1.35.0/): Version ^1.39.0
- [Whitenoise](https://pypi.org/project/whitenoise/): Version ^6.6.0
- [Sphinx](https://www.sphinx-doc.org/en/master/index.html): Version ^7.2.6
- [Sphinxcontrib-django](https://pypi.org/project/sphinxcontrib-django/): Version ^2.5
- [Pytest-django](https://pypi.org/project/pytest-django/): Version ^4.7.0
- [Flake8](https://pypi.org/project/flake8/): Version ^6.1.0
- [Coverage](https://pypi.org/project/coverage/): Version ^7.3.2
- [Poetry](https://python-poetry.org/): Version 1.7.1
- [Docker](https://docs.docker.com/get-docker/): Version 25.0.2

### :wrench: Installation :wrench:
***
Prerequisites: Python, Poetry, Sentry
***
In your directory for the project:

Clone repository from:
- [OC Lettings](https://github.com/SpiritF0rest/OC_Python_P13_Lettings)

#### :wrench: Virtual environment and modules :wrench:

```
To install modules:
$ poetry install

To active the virtual environment (Linux):
$ source $(poetry env info --path)/bin/activate

To active the virtual environment (Windows Powershell):
$ & ((poetry env info --path) + "\Scripts\activate.ps1")

To deactive the virtual environment: 
$ deactivate
```

#### :wrench: Dotenv :wrench:

```
Copy the .env.example in a .env file and fill with the correct data:

SENTRY_DSN : Expected URL
SECRET_KEY : Expected String like "very_strong_key"
ALLOWED_HOSTS : Expected String like "localhost, 127.0.0.1"
CSRF_TRUSTED_ORIGINS : Expected String like "https://site.onrender.com"
```

#### :wrench: Run :wrench:

```
$ python3 manage.py runserver
```
Now, you can use the app :tada:

### :newspaper: Tests :newspaper:
***
```
To test:
$ poetry run pytest

To generate Flake 8 report:
$ poetry run flake8

To see coverage:
$ poetry run coverage run -m pytest
$ poetry run coverage report
$ poetry run coverage html
```

### :lock: Admin :lock:
***
Go to http://localhost:8000/admin`
```
User: admin
Password: Abc1234!
```

### :wrench: Database :wrench:
***
```
$ cd /path/to/project

Open a shell session
$ sqlite3

Connect to the database
$ .open oc-lettings-site.sqlite3

Display tables
$ .tables

Display columns in profiles tables
$ pragma table_info(oc_lettings_site_profile);

Run request on profiles tables
$ select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';

Quit
$ .quit

```

### :wrench: Deployment :wrench:
***
Prerequisites: Docker Hub, CircleCI and Render accounts.
***
#### :wrench: Docker Hub :wrench:

In My Account, go to Security and retrieve your Access Token

#### :wrench: Render :wrench:

In project Environment, you can manage these variables.
```
ALLOWED_HOSTS: String like in .env
SECRET_KEY: Django Key like in .env
SENTRY_DSN: URL like in .env
CSRF_TRUSTED_ORIGINS: String like in .env
```

#### :wrench: Circle CI :wrench:

In project settings, go to Environment Variables and manage these variables.
```
ALLOWED_HOSTS: String like in .env
CSRF_TRUSTED_ORIGINS: String like in .env
DOCKERHUB_TOKEN: Your Docker Hub access token
DOCKERHUB_USERNAME: Your Docker Hub username
POETRY_CACHE_DIR: Path to cache directory
POETRY_VIRTUALENVS_IN_PROJECT: 1
RENDER_KEY: Deploy Hook (in render project settings)
RENDER_URL: Your render URL
SECRET_KEY: Django Key like in .env
SENTRY_DSN: URL like in .env
```

#### :wrench: Use :wrench:

Build, publish and deploy jobs are only executed when you push commit to master branch.

#### :wrench: Docker command (local) :wrench:
```
To build your local image:
$ docker build -t your-image-name --build-arg POETRY_CACHE_DIR=path/to/cache/dir .

To run this image (ALLOWED_HOSTS is a string contains hosts):
$ docker run --rm -e SECRET_KEY='django_secret_key' -e ALLOWED_HOSTS="localhost, 127.0.0.1, 0.0.0.0:8000" -p 8000:8000 your-image-name

```

:snake: Enjoy :snake:
