# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pandas
import datetime
from scrapy.conf import settings
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from address_bot.items import AddressApiItem
from zipfile import ZipFile
from django.core.management import call_command
from django.db import connection
from io import StringIO
from os import rename


######
from pprint import pprint

class AddressBotPipeline(FilesPipeline):
    
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url)
    
    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        file = ZipFile(item['file_paths'] + file_paths[0])
        file_name = file.infolist()[0].filename
        df = pandas.read_csv(file.open(file_name),encoding='Shift_JIS')
        header = df.columns.values.tolist()
        data = df.values
        
        AddressApiItem.django_model.objects.all().delete()
        # sequence reset処理を追加
        # commands = StringIO()
        # cursor = connection.cursor()
        # with open('C:/Users/003418/Documents/adress_api/django_api/') as f:
        #     call_command('sqlsequencereset', stdout=f)
        # # call_command('sqlsequencereset', 'api', stdout=commands)

        # pprint(commands.getvalue())
        # cursor.execute(commands.getvalue())
        # for line in data:
        #     address = AddressApiItem()
        #     address['zip_code'] = line[2]           
        #     address['pref'] = line[6]
        #     address['city'] = line[7]
        #     address['town'] = line[8]
        #     address['kana_pref'] = line[3]
        #     address['kana_city'] = line[4]
        #     address['kana_town'] = line[5]
        #     address.save()
        
        rename(item['file_paths'] + file_paths[0] ,item['file_paths'] + 'full/'  + datetime.date.today().strftime('%Y%m%d')  + '.zip')
