BOT_NAME = 'extrabanca'

SPIDER_MODULES = ['extrabanca.spiders']
NEWSPIDER_MODULE = 'extrabanca.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'extrabanca.pipelines.ExtrabancaPipeline': 100,

}