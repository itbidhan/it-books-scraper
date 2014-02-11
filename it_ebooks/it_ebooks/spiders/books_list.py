from urlparse import urljoin

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from it_ebooks.items import ItEbooksItem


class BooksListSpider(CrawlSpider):
    name = 'books_list'
    allowed_domains = ['it-ebooks.info']
    start_urls = ['http://www.it-ebooks.info/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/book/'), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=r'/publisher/'), follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = ItEbooksItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        i['name'] = hxs.select('//h1[@itemprop="name"]/text()').extract()[0]
        i['publisher'] = hxs.select('//a[@itemprop="publisher"]/text()').extract()[0]
        i['url'] = response.url
        i['description'] = "\n".join(hxs.select('//span[@itemprop="description"]/text()').extract())
        i['download_link'] = urljoin(response.url,hxs.select('//a[@id="dl" or contains(@href,"filepi.com")]/@href').extract()[0])
        return i