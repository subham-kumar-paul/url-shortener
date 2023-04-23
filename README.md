# Url Shortener

The goal of this project is to create a URL shortener website that allows users to shorten long URLs and track the clicks on the shortened URLs. Additionally, the website should provide an API that allows developers to integrate the URL shortening functionality into their applications.

Users can sign up and log in to the site to access their dashboard. The dashboard displays all the shortened URLs created by the user, along with their statistics, such as the total number of clicks and the date and time of the last click. The user can also edit or delete any of their links from the dashboard.

When a user creates a new shortened URL, they can optionally specify a custom alias to make it more memorable. The site will check if the alias is already in use and generate a unique one if necessary.

The site also provides an easy-to-use form for shortening URLs. When a user enters a long URL into the form, the site generates a shortened URL and displays it on the screen. The user can then copy the shortened URL and share it with others.

In addition to the user-facing features, the site also has a back-end database that stores all the links and their statistics. This allows the site to provide accurate and up-to-date statistics for each link.

The site is designed to be user-friendly and easy to use, with a modern and responsive interface that works well on both desktop and mobile devices. It is built using the Django framework and uses Celery for background tasks such as sending email notifications.








To run this, you need to have docker installed on your pc.
First build the docker-container by 
        $ docker-compose -f local.yml build
 
Once the build is done, run the following command
        $ docker-compose -f local.yml up
        
Open the site by visiting 'http://127.0.0.1:8000/'

While the container is up, open a new terminal and run the following commands:- 
        $ docker-compose -f local.yml run --rm django python manage.py makemigrations
        $ docker-compose -f local.yml run --rm django python manage.py migrate
        $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
        
Now, to use login through google you need to setup your google developer account and creating a new project here 'https://console.cloud.google.com/cloud-resource-manager'.
Name:- Url Shortener

Authorized JavaScript | origins URIs 1:- http://127.0.0.1:8000

Authorized redirect URIs | URIs1:- http://127.0.0.1:8000/accounts/google/login/callback/

Generate your Client ID and Client secret.

Go to 'http://127.0.0.1:8000/admin'
Find and go to 'Social Applications' under 'Social Accounts' in the right panel.
Click 'Add social Applications'
'Provider: Google'
'Name: Url Shortener'
'Client Id: *generated client id*'
'Secret Key: *generated client secret*'
Move 'http://127.0.0.1:8000' from 'Available Sites' to 'Chosen Sites'

Refer this video 'https://www.youtube.com/watch?v=Gk9tsLHMMsM'








[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy url_shortener

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd url_shortener
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

``` bash
cd url_shortener
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

``` bash
cd url_shortener
celery -A config.celery_app worker -B -l info
```

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
