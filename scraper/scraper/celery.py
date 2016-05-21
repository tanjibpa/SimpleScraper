from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from scrapy.crawler import Crawler
from scrapy import signals
from scrapy.settings import Settings
from twisted.internet import reactor
from billiard import Process
from scrapy.utils.project import get_project_settings
from thescraper.thescraper.spiders.r_python import RPythonSpider

logger = get_task_logger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')
app = Celery('scraper')
settings = Settings()
os.environ['SCRAPY_SETTINGS_MODULE'] = 'thescraper.thescraper.settings'
settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
settings.setmodule(settings_module_path, priority='project')

app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

class CrawlerScript(Process):
	def __init__(self, spider):
		Process.__init__(self)
		# settings = get_project_settings()
		self.crawler = Crawler(spider, settings)
		# self.crawler.configure()
		self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
		self.spider = spider

	def run(self):
		self.crawler.crawl()
		# self.crawler.start()
		reactor.run()

@periodic_task(run_every=(crontab(minute='*/1')),
	name="task_crawl_r_python",
	ignore_result=True)
def task_crawl_r_python():
	spider = RPythonSpider()
	crawler = CrawlerScript(spider)
	crawler.start()
	crawler.join()
	logger.info("Crawled successfully!")

