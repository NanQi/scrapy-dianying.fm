from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from dianying.items import DianyingItem

class dianyingSpider(CrawlSpider):
    name = "dianying"
    download_delay = 2
    allowed_domains = ["dianying.fm"]
    start_urls = [
        "http://www.dianying.fm/collection",
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=('/collection')), callback='parse_1', follow=True),
        Rule(SgmlLinkExtractor(allow=('/collection/[0-9]+')), callback='parse_1', follow=True),
        Rule(SgmlLinkExtractor(allow=('/movie/.+')), callback='parse_1', follow=True),
    ]

    def parse_1(self, response):

        item = DianyingItem()
        item['title'] = response.css('title::text').extract_first()
        item['url'] = response.url

        return item

