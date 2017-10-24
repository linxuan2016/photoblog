"""
WSGI config for photoblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ["SECRET_KEY"] = "mimilandyqynitt559$k+@^8us-zl#d*+u$8r-(jd+^^jj2qkbtt)4nevlphotoblog"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photoblog.settings")

application = get_wsgi_application()
