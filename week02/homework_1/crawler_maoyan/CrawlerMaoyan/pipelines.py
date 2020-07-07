# -*- coding: utf-8 -*-
import csv
import pymysql
import pymysql.cursors

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
        print(item['title'])
        self.writer.writerow(item)
        return item


# def test_extract_dbinfo(**db_info):
#     print(db_info['host'])


# dbInfo = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'root',
#     'password': 'rootroot',
#     'db': 'test'
# }

# test_extract_dbinfo(**dbInfo)


class MySQLPipeline:

    def __init__(self, **db_info):
        self.db_host = db_info['host']
        self.db_port = db_info['port']
        self.db_user = db_info['user']
        self.db_password = db_info['password']
        self.db_name = db_info['db']
        print('MySQLPipeline instantiated...')

    @classmethod
    def from_crawler(cls, crawler):
        db_info = crawler.settings.get('DB_INFO')
        print('DB_INFO is: ')
        print(db_info)
        return cls(**db_info)

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            db=self.db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print('DB connection opened...')
        print(self.connection)

    def close_spider(self, spider):
        self.connection.close()
        print('DB connection closed...')

    def process_item(self, item, spider):
        print('This is the process_item() of MySQLPipeline...')
        print(item)
        title = item['title'][0].replace("'", r"\'")
        print(title)
        genre = item['genre']
        print(genre)
        release_date = item['release_date']
        print(release_date)

        try:
            with self.connection.cursor() as cursor:
                print(cursor)
                # Create a new record
                sql = f"INSERT INTO `{self.db_name}`.`maoyan_movie`(`movie_no`, `title`, `genre`, `release_date`) VALUES (NULL, '{title}', '{item['genre']}', '{item['release_date']}');"
                print(sql)
                cursor.execute(sql)

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                self.connection.commit()

            with self.connection.cursor() as cursor:
                print(cursor)
                # Read a single record
                sql = f"SELECT maoyan_movie.movie_no, maoyan_movie.title FROM maoyan_movie WHERE maoyan_movie.title = '{title}';"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
        finally:
            return item
