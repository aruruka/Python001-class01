# -*- coding: utf-8 -*-
import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlermaoyanPipeline:
    def open_spider(self, spider):
        columns = ['title', 'genre', 'release_date']
        file_name = 'maoyan.csv'
        # newline为空，写入时不会出现空行
        self.file = open(f'{file_name}', 'w',
                         newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, columns)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # 可以增加判断去重的条件
        self.writer.writerow(item)
        return item
