# Fest Management System

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
4. Enter any arbitary key in the `SECRET_KEY` field in settings.py
5. Ensure that you have python3 set as default. You can do this by `alias python=python3`
6. Run `pip install -r requirements.txt` to install all dependencies
7. Run migrations using `python manage.py migrate`
8. Run server with `python manage.py runserver`
9. Ok you are all set! Visit http://localhost:8000 in your browser
