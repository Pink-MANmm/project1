import time
from datetime import datetime

import brotli
import pymongo
from scrapy import Selector
import requests
from Translate import translate

headers1={
    'authority': 'timesofindia.indiatimes.com',
    'method': 'GET',
    'path': '/world/china',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_ga=GA1.2.1494419517.1658487004; tp-deviceid=2c36a0e9db8d4b200462359ef4b7a39e; tp-deviceid-legacy=2c36a0e9db8d4b200462359ef4b7a39e; _grx=1ab40262-0834-4009-8516-9299faf34fab; _iibeat_session=56ada93a-bfba-48b7-977f-a95a762213e3; _col_uuid=66203a0d-1fe4-4c90-81e0-24716c092a4f-619o; _pbjs_userid_consent_data=3524755945110770; _gcl_au=1.1.932336611.1658638402; _fbp=fb.1.1658638402838.910352483; deviceid=1p7cw5zg65wamhc6fvi889fbj; lgc_deviceid=1p7cw5zg65wamhc6fvi889fbj; geostate=MH; _rtbpbjs_userid_consent_data=3524755945110770; geo_region=; _pubcid=3072535f-d619-4aa8-b01f-16396f2006a6; vmpbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-26T05%3A41%3A03%22%7D; _gid=GA1.2.2090124752.1658977685; geo_continent=AS; geo_country=HK; mdeviceid=b5575967495c62a8dbad1800c7792a2c; __gads=ID=1ea2cab0d237bec0:T=1658487009:S=ALNI_MbkGoKgU3lkarEugfBMz3NiGDTD9A; pbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-28T03%3A29%3A11%22%7D; _iibeat_vt=20220622,20220623,20220624,20220626,20220628,20220629; _grxs=909c1375-b43b-4d41-bfef-133df60bc9cb; __aaxsc=2; currencyCode=USD; __gpi=UID=000007f62ce37672:T=1658487009:RT=1659057205:S=ALNI_MbcD2vpk2CVqV17vSezz1USI5p-zQ; hbmp_cap_h=eyJzb3Zybl9ta3AiOjF9; hbmp_cap_d=eyJzb3Zybl9ta3AiOjF9; _gat=1; aasd=42%7C1659058176383; cto_bundle=y5DBjF9URFkzc2xocHZjeWlNJTJCRHlkZ2VHQ3UybHJSdDBUMGJzMzY3YnlNYmpRTzVNVFRtJTJCNUV4bkRHWWR1VmF0VFA0NW9FaFlkTDNwZFBuVDhoajAwQkpwYiUyQllGNmNBdnlWd3cybkJmYWIzR1p4eG91dUVJOEc4SmN5a2RkVmowS2JUeSUyRlBXMjhIRUZHTnklMkZTVkxPUVpjeTBBJTNEJTNE; cto_bidid=eDaHU19IdEVnTDJ6UkdMdSUyQnlDSll6VXJTJTJCayUyQjVKNGQ3SUl1cjJIc1ZrbXZTalFIMEhkU2xjbk9rcHh2c1pFOWUxJTJGOTlQTlA5R1NkdjR5RXVISnNTSDV6T0kwQ1R2dHYxZ3B5c3VtalV1WXglMkJKbExYQ1haUzVnRmdvNnBzMG9qR2VmdVA',
    'if-modified-since': 'Fri, 29 Jul 2022 01:27:24 GMT',
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
headers2={
    'authority': 'timesofindia.indiatimes.com',
    'method': 'GET',
    'path': '/world/china/2',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_ga=GA1.2.1494419517.1658487004; tp-deviceid=2c36a0e9db8d4b200462359ef4b7a39e; tp-deviceid-legacy=2c36a0e9db8d4b200462359ef4b7a39e; _grx=1ab40262-0834-4009-8516-9299faf34fab; _iibeat_session=56ada93a-bfba-48b7-977f-a95a762213e3; _col_uuid=66203a0d-1fe4-4c90-81e0-24716c092a4f-619o; _pbjs_userid_consent_data=3524755945110770; _gcl_au=1.1.932336611.1658638402; _fbp=fb.1.1658638402838.910352483; deviceid=1p7cw5zg65wamhc6fvi889fbj; lgc_deviceid=1p7cw5zg65wamhc6fvi889fbj; geostate=MH; _rtbpbjs_userid_consent_data=3524755945110770; geo_region=; _pubcid=3072535f-d619-4aa8-b01f-16396f2006a6; vmpbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-26T05%3A41%3A03%22%7D; _gid=GA1.2.2090124752.1658977685; geo_continent=AS; geo_country=HK; mdeviceid=b5575967495c62a8dbad1800c7792a2c; __gads=ID=1ea2cab0d237bec0:T=1658487009:S=ALNI_MbkGoKgU3lkarEugfBMz3NiGDTD9A; pbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-28T03%3A29%3A11%22%7D; _iibeat_vt=20220622,20220623,20220624,20220626,20220628,20220629; _grxs=909c1375-b43b-4d41-bfef-133df60bc9cb; __aaxsc=2; currencyCode=USD; __gpi=UID=000007f62ce37672:T=1658487009:RT=1659057205:S=ALNI_MbcD2vpk2CVqV17vSezz1USI5p-zQ; cto_bundle=GAOPEF9URFkzc2xocHZjeWlNJTJCRHlkZ2VHQ2hrWSUyQmJkeiUyRnhQV1dGcnAzb2hDR3Z1SmoxUksxbW9wNzFwcVl3QVNCWUcxQnpKNnVBNHBFbHRRRXFuMDUyVE1qVnBpJTJCOG9TOUhNeDBmYnZoVlRTcGZCMDNuM0pDRk0lMkJTRlkyMlllYThVd1QlMkZ5T09idlpvQ2FjN1BhR0p3VG04THclM0QlM0Q; cto_bidid=Ou8kQ19IdEVnTDJ6UkdMdSUyQnlDSll6VXJTJTJCayUyQjVKNGQ3SUl1cjJIc1ZrbXZTalFIMEhkU2xjbk9rcHh2c1pFOWUxJTJGOTlQTlA5R1NkdjR5RXVISnNTSDV6T0l3WU9CWVFobjlzU05LdUtWUEEwOW5jSjJSMkI4Rlp2U0FWN0Z3cE5HJTJCZTE; _gat=1; aasd=26%7C1659057202008',
    'if-modified-since': 'Fri, 29 Jul 2022 01:00:00 GMT',
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
headers3={
    'authority': 'timesofindia.indiatimes.com',
    'method': 'GET',
    'path': '/world/china/debris-from-a-chinese-space-rocket-is-crashing-toward-earth/articleshow/93162293.cms',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.2.1494419517.1658487004; tp-deviceid=2c36a0e9db8d4b200462359ef4b7a39e; tp-deviceid-legacy=2c36a0e9db8d4b200462359ef4b7a39e; _grx=1ab40262-0834-4009-8516-9299faf34fab; _iibeat_session=56ada93a-bfba-48b7-977f-a95a762213e3; _col_uuid=66203a0d-1fe4-4c90-81e0-24716c092a4f-619o; _pbjs_userid_consent_data=3524755945110770; _gcl_au=1.1.932336611.1658638402; _fbp=fb.1.1658638402838.910352483; deviceid=1p7cw5zg65wamhc6fvi889fbj; lgc_deviceid=1p7cw5zg65wamhc6fvi889fbj; geostate=MH; _rtbpbjs_userid_consent_data=3524755945110770; geo_region=; _pubcid=3072535f-d619-4aa8-b01f-16396f2006a6; vmpbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-26T05%3A41%3A03%22%7D; _gid=GA1.2.2090124752.1658977685; geo_continent=AS; geo_country=HK; pbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-28T03%3A29%3A11%22%7D; _iibeat_vt=20220622,20220623,20220624,20220626,20220628,20220629; __aaxsc=2; currencyCode=USD; __gpi=UID=000007f62ce37672:T=1658487009:RT=1659057205:S=ALNI_MbcD2vpk2CVqV17vSezz1USI5p-zQ; hbmp_cap_d=eyJzb3Zybl9ta3AiOjEsImFteCI6MX0=; _grxs=6c0ac652-7f8d-4622-a047-bcb716f6dd19; mdeviceid=b5575967495c62a8dbad1800c7792a2c; AMP_TOKEN=%24NOT_FOUND; grxgeostate=Hong%20Kong; geolocation=Hong%20Kong; ak_bmsc=0841F9CE66EFBE491339ADA86317C086~000000000000000000000000000000~YAAQpEYRYAom9R6CAQAARt9ESBAkgfnXnKSKQrwpgIPtOrP942j3tgbl1usyJeRg3X48gcJXO1fBF+T1b318U1fbYAo11bvtO7wbfHy2+g8+nWZ/nNzvZ5REc4e2Aq+oOcSfhpvT9Bn5VdYh1t/uZfYQtpnRltM5ry77ODls7jtAOrAvt1DLD8+iGJZ9Pg18Ig7L1oldMfTXvTUtAy3T9TprB7r+437yZIyGqD+csBpDh5FSeY+nPoCYfvhYBFQ6NkultcA9VsNnQrbC/z2SibR5ypCG80rSbya0J5axe0d7gfcgoBhsxG2bkHOLYLj1MppsuRP5BF8YA6UkTuOphzXu6HsP1lLhDmGa7OHTUg8oP7LoA4pDLCyYREwRSTa5iKaMIydT51B0d1Qs5Wo=; ucf_uid=cadb37ea-ea55-4301-952b-c7f138f20d5f; __gads=ID=1ea2cab0d237bec0:T=1658487009:S=ALNI_MbkGoKgU3lkarEugfBMz3NiGDTD9A; minitvClose=1; cto_bidid=51p4D19IdEVnTDJ6UkdMdSUyQnlDSll6VXJTJTJCayUyQjVKNGQ3SUl1cjJIc1ZrbXZTalFIMEhkU2xjbk9rcHh2c1pFOWUxJTJGOTlQTlA5R1NkdjR5RXVISnNTSDV6T0kwNGZ2ZG5FalI2Uk9tYm0lMkJJbjFIVUZ3S1hrUEVNY1c4T3lxbHBweTlkeXg; bm_sv=E4B06D1750160E6556BD78DA91C1D168~YAAQj0YRYBLTCCOCAQAAL29qSBCuadEDDqYe4E64IcFcyBLsgtxmLurXe4M3Hqmb8i6ev9Ereo8/28i2yxYIg2b3juSpg9/NxMow221TCjJC+bI47JLshruHOc48sfvWUjYmfKdaFkitKSYUJcYqMNTNmKIKProhRXa+nKeq1Zj4WANZnA91Hg4DwSln9eKvhqSZ6Sv2BCOHzi1tQFTg57xbc9FevPGECUNZrDbwChOLKAm27Y+l2GDULnpiqPuUIuQqfA==~1; aasd=42%7C1659072075777; cto_bundle=aTSsIF9URFkzc2xocHZjeWlNJTJCRHlkZ2VHQ3J4eVh4dlFVR1htNTZydDdJaGNRN0dTcHg3WW56eWM3ZWFnRFZBRVlFcEZ0QnFiMkRqR21rMXozTkpubzFkQmRRbXRjOWxRUkNFRSUyRldnQzBiT3hLbm5XMkNvWXFGbDhpSUJFMXNXVlZsVW9UY1VnMWw4eXlVZWUybk9QMmFuV1lRJTNEJTNE; PlRef=18981847; _gat=1',
    'referer': 'https://timesofindia.indiatimes.com/world/china',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
headers={
    'authority': 'timesofindia.indiatimes.com',
    'method': 'GET',
    'path': '/world/china/3',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.2.1494419517.1658487004; tp-deviceid=2c36a0e9db8d4b200462359ef4b7a39e; tp-deviceid-legacy=2c36a0e9db8d4b200462359ef4b7a39e; _grx=1ab40262-0834-4009-8516-9299faf34fab; _iibeat_session=56ada93a-bfba-48b7-977f-a95a762213e3; _col_uuid=66203a0d-1fe4-4c90-81e0-24716c092a4f-619o; _pbjs_userid_consent_data=3524755945110770; _gcl_au=1.1.932336611.1658638402; _fbp=fb.1.1658638402838.910352483; deviceid=1p7cw5zg65wamhc6fvi889fbj; lgc_deviceid=1p7cw5zg65wamhc6fvi889fbj; geostate=MH; _rtbpbjs_userid_consent_data=3524755945110770; geo_region=; _pubcid=3072535f-d619-4aa8-b01f-16396f2006a6; vmpbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-26T05%3A41%3A03%22%7D; _gid=GA1.2.2090124752.1658977685; geo_continent=AS; geo_country=HK; mdeviceid=b5575967495c62a8dbad1800c7792a2c; __gads=ID=1ea2cab0d237bec0:T=1658487009:S=ALNI_MbkGoKgU3lkarEugfBMz3NiGDTD9A; pbjs-unifiedid=%7B%22TDID%22%3A%222fe93176-2f7b-4d9f-86e4-603033f8ed87%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-06-28T03%3A29%3A11%22%7D; _iibeat_vt=20220622,20220623,20220624,20220626,20220628,20220629; _grxs=909c1375-b43b-4d41-bfef-133df60bc9cb; __aaxsc=2; currencyCode=USD; __gpi=UID=000007f62ce37672:T=1658487009:RT=1659057205:S=ALNI_MbcD2vpk2CVqV17vSezz1USI5p-zQ; _gat=1; aasd=7%7C1659058176383; cto_bundle=TEoN619URFkzc2xocHZjeWlNJTJCRHlkZ2VHQ2p5YWtzVjdycXY2S0xURWNWODBQblRBNWpZWG5aOGlxYVROT01CNDdmWld5c1pVJTJGWkNhQUltZUw2dndHeklkMExMOW9GMUxqa2VsQk5mU2NzOEVreExsM0lkWVhSbW5BZGQlMkJnJTJGVFFxTUlFaXdXN1hDS2JCYW5BWnFvdFZNNnVVZyUzRCUzRA; cto_bidid=LzdtQF9IdEVnTDJ6UkdMdSUyQnlDSll6VXJTJTJCayUyQjVKNGQ3SUl1cjJIc1ZrbXZTalFIMEhkU2xjbk9rcHh2c1pFOWUxJTJGOTlQTlA5R1NkdjR5RXVISnNTSDV6T0klMkJlUWVlNnBNS0luSmJmTTNqcGVyQUppUSUyRjhjeGhZcmRTZ3AlMkZVQzM4REQw',
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

def get_data(response,item):
    Year = datetime.now().year
    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient["yinduDB"]
    sel = Selector(response)
    title=sel.css('h1._1Y-96 > span::text').extract_first()
    print(title)
    if title!=None:
        Title = translate(title)
        if Title!='':
            item['news_title'] = Title
            if sel.css('div.yYIu-.byline > span::text').extract_first()[-23]!=' ':
                Mounth = sel.css('div.yYIu-.byline > span::text').extract_first()[-23:-20]
            else:
                Mounth = sel.css('div.yYIu-.byline > span::text').extract_first()[-22:-19]
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
            day=int(sel.css('div.yYIu-.byline > span::text').extract_first()[-19:-17])
            if day<10:
                day='0'+str(day)
            else:
                day=str(day)
            item['news_date'] = sel.css('div.yYIu-.byline > span::text').extract_first()[-15:-11] + '/' + month + '/'+ day+'/'+sel.css('div.yYIu-.byline > span::text').extract_first()[-9:-4]
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

for page in range(1, 1000):
    print(page)
    if page == 1:
        url = 'https://timesofindia.indiatimes.com/world/china'
        response = requests.get(url=url, proxies=proxies, headers=headers1,timeout=60)
        if response.status_code==200:
            sel = Selector(response)
            selectors = sel.css('div#c_articlelist_stories_2 > ul.list5.clearfix > li')
            for selector in selectors:
                item={}
                item['news_href']=selector.css('span > a::attr(href)').extract_first()
                if item['news_href']!=None:
                    headers['path']=item['news_href']
                    headers['referer']=url
                    response = requests.get(url='https://timesofindia.indiatimes.com'+str(item['news_href']), proxies=proxies, headers=headers3,timeout=60)
                    get_data(response,item)
        else:
            continue
    elif page==2:
        url = 'https://timesofindia.indiatimes.com/world/china/2'
        response = requests.get(url=url, proxies=proxies, headers=headers2,timeout=60)
        if response.status_code==200:
            sel = Selector(response)
            selectors = sel.css('div#c_articlelist_stories_2 > ul.list5.clearfix > li')
            for selector in selectors:
                item = {}
                item['news_href'] = selector.css('span > a::attr(href)').extract_first()
                if item['news_href'] != None:
                    headers['path'] = item['news_href']
                    headers['referer'] = url
                    response = requests.get(url='https://timesofindia.indiatimes.com' + str(item['news_href']),proxies=proxies, headers=headers3,timeout=60)
                    get_data(response, item)
        else:
            continue
    else:
        url = f'https://timesofindia.indiatimes.com/world/china/{page}'
        headers['path']=f'/world/china/{page}'
        response = requests.get(url=url, proxies=proxies, headers=headers,timeout=60)
        if response.status_code==200:
            sel = Selector(response)
            selectors = sel.css('div#c_articlelist_stories_2 > ul.list5.clearfix > li')
            for selector in selectors:
                item = {}
                item['news_href'] = selector.css('span > a::attr(href)').extract_first()
                if item['news_href'] != None:
                    headers['path'] = item['news_href']
                    headers['referer'] = url
                    response = requests.get(url='https://timesofindia.indiatimes.com' + str(item['news_href']),proxies=proxies, headers=headers3,timeout=60)
                    get_data(response, item)
        else:
            continue
    time.sleep(5)