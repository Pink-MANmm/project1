import time
from datetime import datetime

import pymongo
from scrapy import Selector
import requests
from Translate import translate

headers={
    'authority': 'ppinewsagency.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
proxies={
    'http':'http://127.0.0.1:19180',
    'https':'http://127.0.0.1:19180'
}

def get_data(response):
    Year = datetime.now().year
    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient["pakistanDB"]
    sel = Selector(response)
    selectors = sel.css('div.article-container > article')
    for selector in selectors:
        item = {}
        title=selector.css('div.article-content.clearfix > header.entry-header > h2.entry-title > a::text').extract_first()
        print(title)
        for keyword in ['China','china','Chinese','chinese', 'Mao Zedong', 'Xi Jinping', 'President Xi', 'Chinese nation','chinese nation','Hu Jintao','president Xi', 'Wen Jiaobo', 'Premier Wen','premier Wen','Li Keqiang','Premier Li','premier Li']:
            if keyword in title :
                Title=translate(title)
                if Title!='':
                    item['news_href'] = selector.css('div.article-content.clearfix > header.entry-header > h2.entry-title > a::attr(href)').extract_first()
                    item['news_title'] = Title
                    Mounth = sel.css('div.article-content.clearfix > div.below-entry-meta > span.posted-on > a > time.entry-date.published::text').extract_first()[0:3]
                    month = ''
                    if Mounth == 'Jan':
                        month = '01'
                    elif Mounth == 'Feb':
                        month = '02'
                    elif Mounth == 'Mar':
                        month = '03'
                    elif Mounth == 'Apr':
                        month = '04'
                    elif Mounth == 'May':
                        month = '05'
                    elif Mounth == 'Jun':
                        month = '06'
                    elif Mounth == 'Jul':
                        month = '07'
                    elif Mounth == 'Aug':
                        month = '08'
                    elif Mounth == 'Sep':
                        month = '09'
                    elif Mounth == 'Oct':
                        month = '10'
                    elif Mounth == 'Nov':
                        month = '11'
                    elif Mounth == 'Dec':
                        month = '12'
                    day=int(selector.css('div.article-content.clearfix > div.below-entry-meta > span.posted-on > a > time.entry-date.published::text').extract_first()[-8:-6])
                    if day<10:
                        day='0'+str(day)
                    else:
                        day=str(day)
                    item['news_date'] = selector.css('div.article-content.clearfix > div.below-entry-meta > span.posted-on > a > time.entry-date.published::text').extract_first()[-4:] + '/' + month + '/'+ day
                    print(item)
                    for i in range(11):
                        if dict(item)['news_date'][0:4] == str(Year - i):
                            href = []
                            for a in mydb[str(Year - i)].find():
                                href.append(a['news_href'])
                            if dict(item)['news_href'] in href:
                                pass
                            else:
                                mydb[str(Year - i)].insert_one(dict(item))
                    href = []
                    for i in mydb['total'].find():
                        href.append(i['news_href'])
                    if dict(item)['news_href'] in href:
                        pass
                    else:
                        mydb['total'].insert_one(dict(item))
    return None

for page in range(1, 10000):
    if page == 1:
        url = 'https://ppinewsagency.com/'
        headers['path']='/'
        print('1')
        response = requests.get(url=url, proxies=proxies, headers=headers,timeout=60,verify=False)
        print(response)
        if response.status_code==200:
            get_data(response)
        else:
            continue
    else:
        url = f'https://ppinewsagency.com/page/{page}/'
        headers['path'] = f'/page/{page}/'
        response = requests.get(url=url, proxies=proxies, headers=headers,timeout=60,verify=False)
        print(page)
        print(response)
        if response.status_code == 200:
            get_data(response)
        else:
            continue




