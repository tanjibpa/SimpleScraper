from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from scrapy.crawler import CrawlerProcess
from spiders.r_python import RPythonSpider

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/1')),
	name="task_crawl_r_python",
	ignore_result=True)
def task_crawl_r_python():
	process = CrawlerProcess()
	process.crawl(RPythonSpider)
	process.start()
	logger.info("Crawled successfully!")
