import json
import operator
import os
import re
import random
from datetime import datetime

import numpy as np
import pandas as pd

import jieba as jieba

from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')

#获取对应国家的总数据条数
def dbLength(Country):
    return len(client[Country].list_collection_names(session=None))-1

#获取对应国家的前80个高频词
def getWordsdata(countryData):
    stopwords=[i.strip() for i in open('stopwords-master/hit_stopwords.txt',encoding='UTF-8').readlines()]
    Data=[]
    cut_list=[]
    for i in countryData['title']:
        Data+=jieba.lcut(''.join(re.findall('[\u4e00-\u9fa5]', i)))
    uniqueData = np.unique(Data)
    for words in uniqueData:
        if len(words) > 1 and (words not in ['中国','越南','总理']):
            if words not in stopwords:
                cut_list.append(words)
    res=[]
    for word in cut_list:
        num=0
        for sameWord in Data:
            if sameWord==word:
                num+=1
        res.append({'name':word,'value':num})
    res.sort(key=operator.itemgetter('value'),reverse=True)
    return res[0:80]

#获取对应国家所有根据时间排序的详细数据（包括时间、标题、连接）以及前80个高频词
def tableData(Country):
    db = client[Country]
    mycol=db['total']
    data=mycol.find().sort('news_date',-1)
    date=[]
    title=[]
    href=[]
    for info in data:
        date.append(info['news_date'])
        title.append(info['news_title'])
        href.append(info['news_href'])
    Data={'date':date,'title':title,'href':href}
    wordsData = getWordsdata(Data)
    return [Data, wordsData]

#获取对应国家指定年份的详细数据以及前80个高频词
def getYeardata(year,Country):
    db = client[Country]
    mycol = db[year]
    data = mycol.find().sort('news_date', -1)
    date = []
    title = []
    href = []
    for info in data:
        date.append(info['news_date'])
        title.append(info['news_title'])
        href.append(info['news_href'])
    Data={'date':date,'title':title,'href':href}
    wordsData=getWordsdata(Data)
    return [Data,wordsData]

#将热词变化的热词数据初始化为空
def wordsChange_Init():
    with open('./static/json/life-expectancy-table.json', 'w') as r:
        json.dump([], r)
    return None

#热词变化功能
def wordsChange(Country):
    db = client[Country]
    stopwords = [i.strip() for i in open('stopwords-master/hit_stopwords.txt', encoding='UTF-8').readlines()]
    #获取对应国家指定年份的前11个高频词
    def yearWords(dbData,year):
        Data = []
        cut_list = []
        for i in list(dbData):
            Data += jieba.lcut(''.join(re.findall('[\u4e00-\u9fa5]', i)))
        uniqueData = np.unique(Data)
        for words in uniqueData:
            if len(words) > 1 and (words not in ['中国','越南','总理']):
                if words not in stopwords:
                    cut_list.append(words)
        res = []
        for word in cut_list:
            num = 0
            for sameWord in Data:
                if sameWord == word:
                    num += 1
            res.append([num,word,year])
        res.sort(key=lambda x:x[0], reverse=True)
        return res[0:11]
    
    #获取对应国家所有年份的前11个高频词
    res=[]
    for i in range(len(db.list_collection_names(session=None))-1):
        dbData=db[str(datetime.now().year-i)].distinct('news_title')
        words=yearWords(dbData,datetime.now().year-i)
        res+=words

    # 写入json文件
    def write_json_data(dict): 
        with open('./static/json/life-expectancy-table.json', 'w') as r:
            json.dump(dict, r)

    res = list(reversed(res))
    write_json_data(res)
    return  res

#情感判断功能
def mood_data(Country):
    def select_year():  # 从数据库中获取数据并清洗
        db = client[Country]
        mycol=db['total']
        data = mycol.find().sort('news_date', -1)
        date = []
        title = []
        for info in data:
            date.append(info['news_date'])
            title.append(info['news_title'])
        Data = {'news_date': date, 'news_title': title}
        data = pd.DataFrame(Data)
        news = {}
        i = 1
        while i <= len(db.list_collection_names(session=None))-1:
            temp = data[data["news_date"].map(lambda x: x[:4] == str(datetime.now().year-i+1))]  # 将时间处理为只有年份和月份
            news[datetime.now().year-i+1] = list(temp["news_title"])
            i += 1
        return news  # ,type(news)

    def mood_judge(titles):  # 情感分数判断
        with open("./static/txt/not.txt", "r", encoding='utf-8') as nt, open("./static/txt/negative.txt", "r", encoding='utf-8') as ng, open(
                "./static/txt/positive.txt", "r", encoding='utf-8') as ps:
            f_nt = nt.read()
            f_ng = ng.read()
            f_ps = ps.read()

        f_nt = f_nt.split("\n")
        f_ng = f_ng.split("\n")
        f_ps = f_ps.split("\n")
        # print(f_ng,f_nt,f_ps)

        score = 0  # 用来情感总分
        rec = {}  # 用来记录单个词条的情感分数
        for title in titles:
            words = jieba.cut(title)

            temp = 0  # 记录这一个词条的分数
            pos, neg = 0, 0  # 积极分数和消极分数
            nt = 0  # 记录反转词汇的数量，奇数就给结果×-1，偶数不变
            # print(i)
            for word in words:
                if word in f_ps:
                    pos += 2
                if word in f_ng:
                    neg -= 2
                #                 print(word)
                if word in f_nt:
                    nt += 1

            temp = pos + neg
            if nt % 2 == 0:
                pass
            else:
                temp *= -1
            rec[title] = temp

        score = sum(rec.values())
        neg_ttl, pos_ttl = 0, 0  # 分开统计积极分数和消极分数
        for i in rec.values():
            if i >= 0:
                pos_ttl += i
            else:
                neg_ttl += i
        # print(rec,score)
        # rec记录了每个词条的情感得分，有需要可以return,此处不需要所以不return
        # print(rec,"kjkjljkl")
        # print(neg_ttl,"====",pos_ttl,"asdkjhaskdjhakjsd")
        return neg_ttl, pos_ttl, score

    def last():
        date = []
        mood_score = []
        neg_ttl = []
        pos_ttl = []
        mood = {"date": 'date', "href": [], "title": 'mood_score', 'positive': "neg_ttl", 'negetive': "pos_ttl"}

        year_range = select_year()  # 获取年份相关数据
        for news_date, news_title in year_range.items():
            date.append(str(news_date))
            neg, pos, score = mood_judge(news_title)
            pos_ttl.append(pos)
            neg_ttl.append(neg)
            # mood_score.append(mood_judge(news_title))
            # print(mood_judge(news_title))

        date.reverse()

        pos_ttl.reverse()
        neg_ttl.reverse()
        i = 0
        while i < len(pos_ttl):
            mood_score.append(pos_ttl[i] + neg_ttl[i])
            i += 1
        mood['date'] = date
        mood['title'] = mood_score
        mood["negetive"] = neg_ttl
        mood["positive"] = pos_ttl
        return mood
    return last()