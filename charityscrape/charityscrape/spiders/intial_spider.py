import scrapy
from charityscrape.items import *

"""
These scrape info from domains. 
name of spiders must be unique.
start_urls is where the spiders start to crawl from.
parse() parses response data and extracts it.

"""
class InitialSpider(scrapy.Spider):

	name = "initialspider"
	allowed_domains = ["charitynavigator.org"]
	start_urls = [
		"http://www.charitynavigator.org/index.cfm?bay=search.alpha"
	]

	def parse(self, response):
		#for sel in response.xpath('//div'):
			item = CharityscrapeItem()
			item['charity_Name'] = response.xpath('//div/h1[@class="charityname"]/text()').extract()
			item['homepage_Link'] = response.xpath('//div/p/a[2]/@href').extract()
			item['overall_starRating'] = response.xpath('//tr/td[@align="center"][1]/text()').extract()[0]
			item['charity_phoneNumber'] = response.xpath('//div/div/div/div[@class="rating"]/p[1]/text()[4]').extract()
			item['charity_address'] = response.xpath('//div/div/div/div[@class="rating"]/p/text()').extract()[0:3]
			item['transperancy_Stars'] = response.xpath('//td[@class="bottom"][2]/text()').extract()
			item['rated_similar_charities'] = response.xpath('//div/div/table[@class="summaryPage"][1]/tr/td/a/text()').extract()[0:4]
			item['popular_similar_charities'] = response.xpath('//div/div/table[@class="summaryPage"][1]/tr/td/a/text()').extract()[4:8]
			item['charity_revenueFYE'] = response.xpath('//div[@id="summary"]/div/div/div[@class="rating"]/table/tr[13]/td[2]/strong/text()').extract()
			yield item