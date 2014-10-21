# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.charity_names_seen = set()

    def process_item(self, item, spider):
        if item['charity_Name'][0] in self.charity_names_seen and len(item['charity_twitterHandle'])==0:


            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.charity_names_seen.add(item['charity_Name'][0])
            return item