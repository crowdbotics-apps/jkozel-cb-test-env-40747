"""
WSGI config for jkozel_cb_test_env_40747 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jkozel_cb_test_env_40747.settings')

application = get_wsgi_application()
