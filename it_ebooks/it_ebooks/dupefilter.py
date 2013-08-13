__author__ = 'scotm'

from scrapy.dupefilter import RFPDupeFilter

class MyDupeFilter(RFPDupeFilter):
    def request_seen(self, request):
        if 'www.' in request.url:
            request.url = request.url.replace('www.','')
        return super(MyDupeFilter, self).request_seen(request)

