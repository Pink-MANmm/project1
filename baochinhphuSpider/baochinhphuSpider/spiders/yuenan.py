import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse

from Translate import translate
from baochinhphuSpider.items import yuenanspiderItem


class YuenanSpider(scrapy.Spider):
    name = 'yuenan'
    allowed_domains = ['baochinhphu.vn']
    custom_settings = {
        #'LOG_LEVEL': 'INFO',
        'ITEM_PIPELINES': {'baochinhphuSpider.pipelines.YuenanspiderPipeline': 400}
    }
    start_urls = ['http://baochinhphu.vn/']

    def start_requests(self):
        for page in range(1, 1000):
            url = f'https://baochinhphu.vn/timelinelist/102442/{page}.htm'
            yield scrapy.Request(url=url)

    def parse(self, response: HtmlResponse):
        sel = Selector(response)
        selectors = sel.css('body > div.box-stream-item')
        for selector in selectors:
            item = yuenanspiderItem()
            title=translate(selector.css('div.box-stream-content > h2 > a::text').extract_first())
            for keyword in ['中国','中华','毛泽东','习近平','习主席','中华民族','中越','越中','中方','胡锦涛','温家宝','李克强']:
                if keyword in title:
                    item['news_title'] = title
                    item['news_date'] = selector.css('div.box-stream-content > span::text').extract_first()[6:10] + '/' + selector.css(
                        'div.box-stream-content > span::text').extract_first()[3:5] + '/' + selector.css(
                        'div.box-stream-content > span::text').extract_first()[0:2] + '/' + selector.css(
                        'div.box-stream-content > span::text').extract_first()[11:16]
                    item['news_href'] = selector.css('div.box-stream-content > h2 > a::attr(href)').extract_first()
                    yield item
                    break
