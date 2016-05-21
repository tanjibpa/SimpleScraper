from __future__ import absolute_import

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraper.settings'

import django
django.setup()

from .celery import app as celery_app