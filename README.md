# Fest Management System

[![Join the chat at https://gitter.im/NIT-dgp/General](https://badges.gitter.im/gitterHQ/gitterHQ.github.io.svg)](https://gitter.im/NIT-dgp/General) [![Build Status](https://travis-ci.org/NIT-dgp/festcms.svg?branch=master)](https://travis-ci.org/NIT-dgp/festcms) [![codecov](https://codecov.io/gh/NIT-dgp/festcms/branch/master/graph/badge.svg)](https://codecov.io/gh/NIT-dgp/festcms)

This is a generic Content management system made specifically for the purpose of handling the websites of college fests. It is written in Django and uses basically a Bootstrap based UI.

## Prerequisites

### Database

Install sqlite3 for development

* Windows: Steps : http://www.sqlitetutorial.net/download-install-sqlite/
* Mac OS X: Mac ships with sqlite3 already installed
* Ubuntu/Debian: `sudo apt-get install sqlite3`
* Fedora/Red Hat/CentOS: `sudo yum install sqlite`

### python-pip

Install pip for python3

* Windows: pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4
* Mac OS (via easy_install): `sudo easy_install pip`
* Debian/Ubuntu: `sudo apt-get install python3-pip`
* Fedora/CentOS: `sudo yum install python-pip python-wheel`

## Virtual Environment Setup
### Windows
1. Setup virtual environment with `pip install virtualenvwrapper-win`
2. Then create a virtual environment for your project: `mkvirtualenv nameofyourproject`
3. The virtual environment will be activated automatically and you’ll see “(nameofyourproject)” next to the command prompt to designate that. 
4. If you start a new command prompt, you’ll need to activate the environment again using: `workon nameofproject` .

### Linux
1. Virtualenv is available on PyPI, we can install it with the pip command: `pip install virtualenv`
2. Then create a virtual environment for your project: `virtualenv --python=python3 nameofproject`
3. Log into the virtualenv created: `source nameofproject/bin/activate`

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

### How to send Newsletters
1. Login the admin panel and click on the Newsletters section.
2. Create a new newsletter to your liking and save it.
3. Now in the Newsletter section presented, mark the letters to be sent.
4. Choose the action **Send email** from the **Actions menu** and click **Go**.
5. This sends the marked Newsletters to subscribed users.

### Setting up email templates and how to use them
1. Create HTML(`.html`) and text(`.txt`) based templates for mail with the context as per your requirements.
2. Place both the HTML and text based files in `festflow/templates/email_extras` directory.
3. Now these templates could be used anywhere within the application by using the `send_mail_template`
method of `email_extras.utils` package.
Eg. Suppose we have `example_mail.html` and `example_mail.txt` as our text based and HTML based templates
with some context `ctx`, attachments `atch` and headers `headers`, then we could do the following to use
the template system.

```
from email_extras.utils import send_mail_template

send_mail_template("Subject", 'example_mail', from_address, to_address,
    fail_silently=False, attachments=atch, context=ctx, headers=headers)
```

> We use [django-email-extras][3] to send template based mails. The email templates should be placed in
> `festflow/templates/email-extras/`.
> PGP encrypted mails could also be sent via the **django-email-extras** module.
> For more information on how to configure PGP encryption module, please refer [here][4].

> We use [django-forms-builder][1] for making custom forms available via admin section.
> A lot of stuff could be configured as mentioned [here][2] in `settings.py`.

[1]:https://github.com/stephenmcd/django-forms-builder
[2]:https://github.com/stephenmcd/django-forms-builder/blob/master/README.rst
[3]:https://github.com/stephenmcd/django-email-extras
[4]:https://github.com/stephenmcd/django-email-extras#configuration
