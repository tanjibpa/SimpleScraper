from scrapy_djangoitem import DjangoItem
from scrapy.item import Item, Field
from django.apps import apps

# DjangoModel = apps.get_app_config('scrapeapp').get_model('RedditLinks')
from scrapeapp.models import RedditLinks as DjangoModel


class ThescraperItem(DjangoItem):
    django_model = DjangoModel

