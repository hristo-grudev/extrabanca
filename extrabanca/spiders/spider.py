import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import ExtrabancaItem
from itemloaders.processors import TakeFirst


class ExtrabancaSpider(scrapy.Spider):
	name = 'extrabanca'
	start_urls = ['https://www.extrabanca.com/extrapeople/eventiecuriosita/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="reading-link"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="next page-numbers"]/@href').getall()
		print(next_page)
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//div[@class="entry-content-wrap"]/h3/text()').get()
		description = response.xpath('//div[@class="entry-content clearfix"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=ExtrabancaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
