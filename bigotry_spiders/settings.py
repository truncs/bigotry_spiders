# Scrapy settings for bigotry_spiders project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'bigotry_spiders'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['bigotry_spiders.spiders']
NEWSPIDER_MODULE = 'bigotry_spiders.spiders'
DEFAULT_ITEM_CLASS = 'bigotry_spiders.items.BigotrySpidersItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

