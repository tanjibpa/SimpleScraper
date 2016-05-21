# -*- coding: utf-8 -*-

# Scrapy settings for thescraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

# import sys
# sys.path.insert(0, '/home/tanjib/PycharmProjects/SimpleScraper/scraper')

# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'scraper.settings'

# import django
# django.setup()

BOT_NAME = 'thescraper'

SPIDER_MODULES = ['thescraper.spiders']
NEWSPIDER_MODULE = 'thescraper.spiders'

ITEM_PIPELINES = {
	'thescraper.thescraper.pipelines.ThescraperPipeline': 0
}
# TO crawl from scrapy (thescraper) directory 
# ITEM_PIPELINES = {
# 	'thescraper.pipelines.ThescraperPipeline': 0
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'thescraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
