#!/usr/bin/env python
"""
WSGI config for festcms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))

os.environ['DJANGO_SETTINGS_MODULE'] = 'festcms.settings'


virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    # See: http://stackoverflow.com/questions/23418735/using-python-3-3-in-openshifts-book-example?noredirect=1#comment35908657_23418735
    # execfile(virtualenv, dict(__file__=virtualenv)) # for Python v2.7
    # exec(compile(open(virtualenv, 'rb').read(), virtualenv, 'exec'), dict(__file__=virtualenv)) # for Python v3.3
    # Multi-Line for Python v3.3:
    exec_namespace = dict(__file__=virtualenv)
    with open(virtualenv, 'rb') as exec_file:
        file_contents = exec_file.read()
    compiled_code = compile(file_contents, virtualenv, 'exec')
    exec(compiled_code, exec_namespace)
except IOError:
    pass


#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "festcms.settings")

application = get_wsgi_application()
