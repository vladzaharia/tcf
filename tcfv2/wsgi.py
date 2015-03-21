"""
WSGI config for tcfv2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tcfv2.settings")

sys.path.append('/srv/www/ubctcf.com/tcfv2')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
