import scrapy
from charityscrape.spiders.searchcategories import *
from charityscrape.urls import *

"""
returns urls for summary pages of every charity 

"""
class searchCategoriesSpider(scrapy.Spider):

	name = "charityurlspider"
	allowed_domains = ["charitynavigator.org"]
	start_urls=[]
	#for i in categories['search']:
	#	start_urls.append(i)

	def parse(self, response):
		#for sel in response.xpath('//div'):
			urls = CharityURLItem()
			urls['charity_url'] = response.xpath('//div[@id="maincontent"]/div[@id="maincontent2"]/a/@href').extract()
			yield categories