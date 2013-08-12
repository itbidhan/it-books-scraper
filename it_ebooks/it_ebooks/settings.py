# Scrapy settings for it_ebooks project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'it_ebooks'

SPIDER_MODULES = ['it_ebooks.spiders']
NEWSPIDER_MODULE = 'it_ebooks.spiders'

HTTPCACHE_ENABLED = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'it_ebooks (+http://www.yourdomain.com)'
