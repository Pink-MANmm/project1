# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from datetime import datetime

from itemadapter import ItemAdapter
import pymongo

class BaochinhphuspiderPipeline:
    def __init__(self):
        super().__init__()
        self.checkFile = "isRunning.txt"

    def open_spider(self, spider):
        self.Year=datetime.now().year
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017')
        self.mydb = self.myclient["yuenanDB"]
        f = open(self.checkFile, "w")  # 创建一个文件，代表爬虫在运行中
        f.close()

    def close_spider(self, spider):
        self.myclient.close()
        isFileExsit = os.path.isfile(self.checkFile)
        if isFileExsit:
            os.remove(self.checkFile)

    def process_item(self, item, spider):
        print(item)
        for i in range(11):
            if dict(item)['news_date'][0:4] == str(self.Year-i):
                href = []
                for a in self.mydb[str(self.Year-i)].find():
                    href.append(a['news_href'])
                if dict(item)['news_href'] in href:
                    pass
                else:
                    self.mydb[str(self.Year-i)].insert_one(dict(item))
        href = []
        for i in self.mydb['total'].find():
            href.append(i['news_href'])
        if dict(item)['news_href'] in href:
            pass
        else:
            self.mydb['total'].insert_one(dict(item))
        return item

class YuenanspiderPipeline:
    def __init__(self):
        super().__init__()
        self.checkFile = "isRunning.txt"

    def open_spider(self, spider):
        self.Year = datetime.now().year
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017')
        self.mydb = self.myclient["yuenanDB"]
        f = open(self.checkFile, "w")  # 创建一个文件，代表爬虫在运行中
        f.close()

    def close_spider(self, spider):
        self.myclient.close()
        isFileExsit = os.path.isfile(self.checkFile)
        if isFileExsit:
            os.remove(self.checkFile)

    def process_item(self, item, spider):
        for i in range(11):
            if dict(item)['news_date'][0:4] == str(self.Year - i):
                href = []
                for a in self.mydb[str(self.Year - i)].find():
                    href.append(a['news_href'])
                if dict(item)['news_href'] in href:
                    pass
                else:
                    self.mydb[str(self.Year - i)].insert_one(dict(item))
        href = []
        for i in self.mydb['total'].find():
            href.append(i['news_href'])
        if dict(item)['news_href'] in href:
            pass
        else:
            self.mydb['total'].insert_one(dict(item))
        return item

class YinduspiderPipeline:
    def __init__(self):
        super().__init__()
        self.checkFile = "isRunning.txt"

    def open_spider(self, spider):
        self.Year = datetime.now().year
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017')
        self.mydb = self.myclient["yinduDB"]
        f = open(self.checkFile, "w")  # 创建一个文件，代表爬虫在运行中
        f.close()

    def close_spider(self, spider):
        self.myclient.close()
        isFileExsit = os.path.isfile(self.checkFile)
        if isFileExsit:
            os.remove(self.checkFile)

    def process_item(self, item, spider):
        for i in range(11):
            if dict(item)['news_date'][0:4] == str(self.Year - i):
                href = []
                for a in self.mydb[str(self.Year - i)].find():
                    href.append(a['news_href'])
                if dict(item)['news_href'] in href:
                    pass
                else:
                    self.mydb[str(self.Year - i)].insert_one(dict(item))
        href = []
        for i in self.mydb['total'].find():
            href.append(i['news_href'])
        if dict(item)['news_href'] in href:
            pass
        else:
            self.mydb['total'].insert_one(dict(item))
        return item

class PakistanspiderPipeline:
    def __init__(self):
        super().__init__()
        self.checkFile = "isRunning.txt"

    def open_spider(self, spider):
        self.Year = datetime.now().year
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017')
        self.mydb = self.myclient["pakistanDB"]
        f = open(self.checkFile, "w")  # 创建一个文件，代表爬虫在运行中
        f.close()

    def close_spider(self, spider):
        self.myclient.close()
        isFileExsit = os.path.isfile(self.checkFile)
        if isFileExsit:
            os.remove(self.checkFile)

    def process_item(self, item, spider):
        for i in range(11):
            if dict(item)['news_date'][0:4] == str(self.Year - i):
                href = []
                for a in self.mydb[str(self.Year - i)].find():
                    href.append(a['news_href'])
                if dict(item)['news_href'] in href:
                    pass
                else:
                    self.mydb[str(self.Year - i)].insert_one(dict(item))
        href = []
        for i in self.mydb['total'].find():
            href.append(i['news_href'])
        if dict(item)['news_href'] in href:
            pass
        else:
            self.mydb['total'].insert_one(dict(item))
        return item