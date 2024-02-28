Deployment
==========

Prerequisites
-------------
Docker Hub, CircleCi and Render accounts.

Docker Hub
----------
In **My Account**, go to Security and retrieve your Access Token

Render
------

In project Environment, you can manage these variables.

- ALLOWED_HOSTS: String like in .env
- SECRET_KEY: Django Key like in .env
- SENTRY_DSN: URL like in .env
- CSRF_TRUSTED_ORIGINS:  String like in .env

Circle CI
---------

In project settings, go to Environment Variables and manage these variables.

- ALLOWED_HOSTS: String like in .env
- CSRF_TRUSTED_ORIGINS:  String like in .env
- DOCKERHUB_TOKEN: Your Docker Hub access token
- DOCKERHUB_USERNAME: Your Docker Hub username
- POETRY_CACHE_DIR: Path to cache directory
- POETRY_VIRTUALENVS_IN_PROJECT: 1
- RENDER_KEY: Deploy Hook (in render project settings)
- RENDER_URL: Your render URL
- SECRET_KEY: Django Key like in .env
- SENTRY_DSN: URL like in .env

Use
---
Build, publish and deploy jobs are only executed when you push commit to master branch.

Docker command (local)
----------------------

To build your local image:
    :code:`docker build -t your-image-name --build-arg POETRY_CACHE_DIR=path/to/cache/dir .`

To run this image (ALLOWED_HOSTS is a string contains hosts):
    :code:`docker run --rm -e SECRET_KEY='django_secret_key' -e ALLOWED_HOSTS="localhost, 127.0.0.1, 0.0.0.0:8000" -p 8000:8000 your-image-name`

Pipeline workflow
-----------------

build-and-publish : build Docker image and publish it to Docker Hub

deploy : deploy to render with new Docker image using deploy hook
