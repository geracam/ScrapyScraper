# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CharityscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    charity_Name = scrapy.Field();
    homepage_Link = scrapy.Field();
    overall_starRating = scrapy.Field();
    charity_phoneNumber = scrapy.Field();
    agent_contactEmail = scrapy.Field();
    charity_address = scrapy.Field();
    transperancy_Stars = scrapy.Field();
    rated_similar_charities = scrapy.Field();
    popular_similar_charities = scrapy.Field();
    

"""charity_EIN = scrapy.Field();
    CN_pageLink = scrapy.Field();
    
    
    finance_starRating = scrapy.Field();
    
    
    charity_FYE = scrapy.Field();
    NTEE_description = scrapy.Field();
    charity_twitterHandle = scrapy.Field();
"""
