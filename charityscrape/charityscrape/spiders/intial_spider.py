import scrapy
from charityscrape.items import *
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


"""
These scrape info from domains. 
name of spiders must be unique.
start_urls is where the spiders start to crawl from.
parse() parses response data and extracts it.

We go into the charity navigator directory and extract 
all the individual pages' urls. Then goes to that url
and extracts the data we need. 

"""

class searchCategoriesSpider(scrapy.Spider):
	name = "initialspider"
	allowed_domains = ["http://www.charitynavigator.org/"]
	start_urls = ["http://www.charitynavigator.org/index.cfm?bay=search.alpha&" ,
				  "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=1",
				  "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=2",
				  "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=4",
				  "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=5",
				  "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=9",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=A",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=B",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=C",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=D",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=E",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=F",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=G",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=H",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=I",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=J",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=K",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=L",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=M",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=N",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=O",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=P",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=Q",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=R",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=S",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=T",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=U",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=V",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=W",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=X",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=Y",
				   "http://www.charitynavigator.org/index.cfm?bay=search.alpha&ltr=Z",
				  ]


	def parse(self, response):
		sel= Selector(response)
	 	xpathh = '//div[@id="maincontent"]/div[@id="maincontent2"]/a/@href'
	 	links = sel.xpath(xpathh).extract()



	 	for link in links:
			
	 		yield Request(url= link,  callback= self.parse_job, dont_filter=True)


	def parse_job(self, response):
		item = CharityscrapeItem()

		item['charity_Name'] = response.xpath('//div/h1[@class="charityname"]/text()').extract()
		item['homepage_Link'] = response.xpath('//div/p/a[2]/@href').extract()
		item['overall_starRating'] = response.xpath('//tr/td[@align="center"][1]/text()').extract()[0]
		item['charity_phoneNumber'] = response.xpath('//div/div/div/div[@class="rating"]/p[1]/text()[4]').extract()
		item['charity_address'] = response.xpath('//div/div/div/div[@class="rating"]/p/text()').extract()[0:3]
		item['transperancy_Stars'] = response.xpath('//td[@class="bottom"][2]/text()').extract()
		item['rated_similar_charities'] = response.xpath('//div/div/table[@class="summaryPage"][1]/tr/td/a/text()').extract()[0:4]
		item['popular_similar_charities'] = response.xpath('//div/div/table[@class="summaryPage"][1]/tr/td/a/text()').extract()[4:8]

		
		request = scrapy.Request(url =item['homepage_Link'][0], callback= self.parse_job2, dont_filter=True)

		request.meta['charity_twitterHandle'] = item

		yield request
		yield item

	def parse_job2(self, response):

		item = response.meta['charity_twitterHandle']
	

		item['charity_twitterHandle'] = response.xpath('//@href').re("https?://w?w?w?\.?twitter\.com/.*")

		yield item















