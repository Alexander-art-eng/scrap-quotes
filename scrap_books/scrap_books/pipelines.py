# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapBooksPipeline(object):
    def __init__(self):
        pass

    def create_connection(self):
        self.connection = sqlite3.connect('quotes.db')
        self.cursor = self.connection.cursor()
        
    def create_tables(self):
        self.cursor.execute("""
            craete table if not exists quotes(
            title text,
            author text,
            tags text, 
            )
        """)

    def process_item(self, item, spider):
        return item
