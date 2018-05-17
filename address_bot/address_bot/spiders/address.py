import scrapy
from scrapy.spiders import BaseSpider
from address_bot.items import AddressBotItem
from scrapy.exceptions import DropItem
from scrapy.conf import settings

# class AddressSpider(scrapy.Spider):
#     name = "address"

#     def start_requests(self):
#         urls = [
#             'http://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         download_url = 'http://www.post.japanpost.jp/zipcode/dl/'
#         page = response.url.split("/")[-2]
#         zip = response.css('tr.arrange-c td a::attr(href)')
#         for href in response.css('tr.arrange-c td a').xpath('@href').extract():
#             if('all' in href):
#                 yield AddressBotItem(file_urls = [download_url + href])


class AddressSpider(scrapy.Spider):
    name = "address"
    allowed_domains = ["http://www.post.japanpost.jp/index.html"]
    start_urls = [
        "http://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html",
    ]

    def parse(self, response):
        download_url = 'http://www.post.japanpost.jp/zipcode/dl/'
        page = response.url.split("/")[-2]
        zip = response.css('tr.arrange-c td a::attr(href)')
        for href in response.css('tr.arrange-c td a').xpath('@href').extract():
            if('all' in href):
                item = AddressBotItem()
                self.logger.info(href)
                item['file_urls'] = [download_url + href]
                item['file_paths'] = settings.get('FILES_STORE')
                return item