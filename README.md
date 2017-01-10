# Fest Management System

[![Join the chat at https://gitter.im/NIT-dgp/General](https://badges.gitter.im/gitterHQ/gitterHQ.github.io.svg)](https://gitter.im/NIT-dgp/General)

This is the Content management system of Ank 2016 - The Knowledge Fest of Maths N Tech club, NIT Durgapur. It is written in Django and uses basically a Bootstrap based UI.

## Prerequisites

### Database

Install sqlite3 for development

* Mac OS X: Mac ships with sqlite3 already installed
* Ubuntu/Debian: `sudo apt-get install sqlite3`
* Fedora/Red Hat/CentOS: `sudo yum install sqlite`

### python-pip

Install pip for python3

* Mac OS (via easy_install): `sudo easy_install pip` 
* Debian/Ubuntu: `sudo apt-get install python3-pip`
* Fedora/CentOS: `sudo yum install python-pip python-wheel`

## Deployment

1. Clone the repository with `git clone git@github.com:ghoshbishakh/festcms.git`
2. Enter the directory using `cd festcms`
3. Copy `festcms/settings.py.example` to `festcms/settings.py`
4. Enter any arbitary key in the `SECRET_KEY` field in `settings.py`
5. To setup mail server, enter the details in email testing section of `settings.py`
6. Ensure that you have python3 set as default. You can do this by `alias python=python3`
7. Run `pip install -r requirements.txt` to install all dependencies
8. Run migrations using `python manage.py migrate`
9. Run server with `python manage.py runserver`
10. Ok you are all set! Visit http://localhost:8000 in your browser

### Setting up feedback form
1. Create a `superuser` account with `python manage.py createsuperuser`, create your credentials.
2. Go to `http://localhost:8000/admin` and enter your credentials.
3. Create a new form in the forms section to your desire, by the name **feedback** and publish it.
4. You're done. You can now test the form at `http://localhost:8000/forms/feedback`.
5. You could check for submissions or make changes to the form via forms section in the admin panel.
6. You could create any other form in a similar way.

### Configuring the unified navbar
1. Login the admin panel and create entries in the Navbar Entries section as per your requirement.
2. Load and use the `navbar` tag if required in any of your custom pages.

> We use [django-forms-builder][1] for making custom forms available via admin section.
> A lot of stuff could be configured as mentioned [here][2] in `settings.py`.

[1]:https://github.com/stephenmcd/django-forms-builder
[2]:https://github.com/stephenmcd/django-forms-builder/blob/master/README.rst
