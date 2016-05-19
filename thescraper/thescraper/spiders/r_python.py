# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
# from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from thescraper.items import ThescraperItem


class RPythonSpider(CrawlSpider):
    name = "r_python"
    allowed_domains = ["reddit.com"]
    start_urls = (
        'https://www.reddit.com/r/python',
    )
    # rules = Rule(LinkExtractor(allow=['r/python/\?count=\d*&after=\w*']),
    #            callback='parse_item',
    #            follow=True)

    reddit_div_xpath = '//div[@data-subreddit="Python"]'
    item_fields = {
        'title': '//div[@class="entry unvoted"]/p[@class="title"]/a/text()',
        'link': '//div[@class="entry unvoted"]/p[@class="title"]/a/@href',
        'pub_date': '//div[@class="entry unvoted"]/p[@class="tagline"]/time/@datetime',
        'data_fullname': '//div/@data-fullname'
    }

    def parse(self, response):
        selector = Selector(response)

        titles = response.xpath(self.item_fields['title'])
        links = response.xpath(self.item_fields['link'])
        pub_dates = response.xpath(self.item_fields['pub_date'])
        data_fullname = response.xpath(self.item_fields['data_fullname'])

        for i in range(len(titles)):
            item = ThescraperItem()
            item['title_text'] = titles[i].extract()
            item['link'] = links[i].extract()
            item['pub_date'] = pub_dates[i].extract()
            item['data_fullname'] = data_fullname[i].extract()
            yield item

            


        
        
