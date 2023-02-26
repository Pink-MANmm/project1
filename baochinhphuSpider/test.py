from scrapy import Selector
import requests

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'mediav=%7B%22eid%22%3A%22753539%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22hH%40d4%3F1Xt%5D9T%5BY%C3%98xI1%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22hH%40d4%3F1Xt%5D9T%5BY%25D8xI1%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A1%7D; mediav=%7B%22eid%22%3A%221165969%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22hH%40d4%3F1Xt%5D9T%5BY%C3%98xI1%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22hH%40d4%3F1Xt%5D9T%5BY%25D8xI1%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A0%7D; acw_tc=2f624a7816678909337856498e11783029d6dc30b02bdf257ef2626e757264; Hm_lvt_bbecf92f3d6d796da2e4bc87f6276ef6=1667890934; Hm_lvt_e67f6679c9ce7c6a98ef564103252111=1667890934; Hm_lvt_86170f2189044d10f0400bf3592d6a21=1667890934; UM_distinctid=184560bf2e46ea-0f381c57e32927-26021e51-144000-184560bf2e5d7b; CNZZDATA1281132515=611911836-1667890357-https%253A%252F%252Fcn.bing.com%252F%7C1667890357; gr_user_id=76757913-2c6c-4630-be18-7d1979698937; 87fba0d27ee03db1_gr_session_id=d2b923a1-bc61-4cb9-838c-950b52fffb73; 87fba0d27ee03db1_gr_session_id_d2b923a1-bc61-4cb9-838c-950b52fffb73=true; hy_data_2020_id=184560bf49e918-06b344441a3c45-26021e51-1327104-184560bf49fc34; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22184560bf49e918-06b344441a3c45-26021e51-1327104-184560bf49fc34%22%2C%22site_id%22%3A651%2C%22user_company%22%3A641%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22184560bf49e918-06b344441a3c45-26021e51-1327104-184560bf49fc34%22%7D; sajssdk_2020_cross_new_user=1; DeviceId=550f92c7bd4c4fc37724e8affd9aabcf; Qx-Normal-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJGWUctSldUIiwiZXhwIjoxNjc1NjY2OTY1LCJpYXQiOjE2Njc4OTA5NjUsInRva2VuIjoiQkFEODI3OEMxMEU4RTRGNURGRjhDMTc0MjAyNkQ3QzhCN0YxMDM1NTMxOUEwNTVBNUREMEJBNzhDNThEODQ5MUZCQzMyNTMzNzNCNDI3RTEwNkVGNEZEQjZFQzEwQkE1RkUwMzQyMjVFRkM1MTAyMTlGNjk0NTQ5MUZCMzkyNzJCNEEzRENCOTM5RjQ2OEY0OTE4Njg4QTZFQzQ0QzI2NjU2MEU1ODE2Q0JGRTg0RjI0N0JDMzYyRUFCODQyOTU3OEI3NTAwMkYxMUNFNDBCNzQ2N0E2MDNFOEI4NDQ2MDIyRkI4NjcyREQ3MEE1NjRFNzE0M0FEOTkxRUVDRTg4NERDODNCNEQyQ0VGNDVFMUQ3MDA0RTI3RUE1QzQxNDdCQ0NERkM1QjMxNjk3OTIzNTdCMDgwMENBOEI1QzlCRkY2QTA0RDhEQ0UxMkQ1NzI5MUY4NTE5MjM0N0M5RDlDODIwQkU4QUNERDJEN0E0RDNDRTM2MUU2NjA4NUIwMDZFNEE0QzE0MzJEOTQ3OEQ4MzgwQTFEOUU4RTdBMkI4MUQzRDYyQjY1MjgwQkI1OTUyRkEwOTQ1RDhGNzIzMDYzQyJ9.oFVBW8Rf0AcEFWTnw5lt5GBF6qYQUCzdqjckaAN8HpM; Qs_lvt_447343=1667890934%2C1667890971; mediav=%7B%22eid%22%3A%22753539%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22hH%40d4%3F1Xt%5D9T%5BY%C3%98xI1%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22hH%40d4%3F1Xt%5D9T%5BY%25D8xI1%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A0%7D; Qs_lvt_455351=1667891194; Qs_pv_455351=2977267881489547000%2C1273784845103085300; Hm_lpvt_86170f2189044d10f0400bf3592d6a21=1667891515; Hm_lpvt_bbecf92f3d6d796da2e4bc87f6276ef6=1667891515; Hm_lpvt_e67f6679c9ce7c6a98ef564103252111=1667891515; Qs_pv_447343=856269813880444500%2C2501576057980796000%2C279592458054885440%2C447037990009019100%2C1024594729650606300; referrer=; promotionSource=https://www.fanyigou.com/trans/translate/readDoc.html?tid=43357910&source=fygNatural; SERVERID=bc496a11d574353da139d018cd7e8110|1667891515|1667890933',
    'Host': 'www.fanyigou.com',
    'If-Modified-Since': 'Fri, 04 Nov 2022 04:01:38 GMT',
    'Referer': 'https://www.fanyigou.com/trans/totran.html',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
response=requests.get(url="https://www.fanyigou.com/trans/translate/readDoc.html?tid=43357910",headers=headers)
sel = Selector(response)
print(sel)
selectors = sel.css('div')
print(selectors)
for selector in selectors:
    print(selector.css('img::attr(src)').extract_first())
