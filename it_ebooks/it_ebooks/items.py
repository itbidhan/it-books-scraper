# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ItEbooksItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    publisher = Field()
    url = Field()
    description = Field()
    download_link = Field()
    pass