from django.db import models

# Create your models here.

class Address(models.Model):
  zip_code = models.CharField( '郵便番号', max_length=7, help_text='郵便番号')
  pref = models.CharField('都道府県', max_length=50, help_text='都道府県', null=True)
  city = models.CharField('市区町村名', max_length=100, help_text='市区町村名', null=True)
  town = models.CharField('町域名', max_length=255, help_text='町域名', null=True)
  kana_pref = models.CharField('都道府県名カナ', max_length=50, help_text='都道府県名カナ', null=True)
  kana_city = models.CharField('市区町村名カナ', max_length=100, help_text='市区町村名カナ', null=True)
  kana_town = models.CharField('町域名カナ', max_length=100, help_text='町域名カナ', null=True)
  

