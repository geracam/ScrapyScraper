import scrapy
from charityscrape.categories import *

"""
goes into the search page and returns domains for each category.
there is no overall search page, you have to go through categories filtered 
by alphabetical order of charities. This returns urls for charities whose 
name starts with A, B, C, etc..

"""
class searchCategoriesSpider(scrapy.Spider):

	name = "searchcategoriesspider"
	allowed_domains = ["charitynavigator.org"]
	start_urls = [
		"http://www.charitynavigator.org/index.cfm?bay=search.alpha"
	]

	def parse(self, response):
		#for sel in response.xpath('//div'):
			categories = CharitySitesItem()
			categories['search_categories'] = response.xpath('//div[@id="maincontent2"]/p[1]/a/@href').extract()
			yield categories