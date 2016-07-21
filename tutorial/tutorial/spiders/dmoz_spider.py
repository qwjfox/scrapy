import scrapy
import string

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python",
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="cat-item"]/a/@href'):
            url = response.urljoin(href.extract())
            item = DmozItem()
            item['main_url'] = url
            request = scrapy.Request(url, callback=self.parse_dir_contents)
            request.meta['item'] = item
            yield request

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div[@class="title-and-desc"]'):
            item = response.meta['item']
            #item['html'] = response.body
            item['title'] = sel.xpath('normalize-space(a/div[@class="site-title"]/text())').extract()
            item['link'] = sel.xpath('normalize-space(a/@href)').extract()
            item['desc'] = sel.xpath('normalize-space(div[@class="site-descr "]/text())').extract()
            yield item
