from scrapy.contrib.spidermiddleware.depth import DepthMiddleware

class MyDepthMiddleware(DepthMiddleware):
    def process_spider_output(self, response, result, spider):
        return super(MyDepthMiddleware, self).process_spider_output(response, result, spider)

