# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(help_text='市区町村名', max_length=100, null=True, verbose_name='市区町村名'),
        ),
        migrations.AlterField(
            model_name='address',
            name='kana_city',
            field=models.CharField(help_text='市区町村名カナ', max_length=100, null=True, verbose_name='市区町村名カナ'),
        ),
        migrations.AlterField(
            model_name='address',
            name='kana_pref',
            field=models.CharField(help_text='都道府県名カナ', max_length=50, null=True, verbose_name='都道府県名カナ'),
        ),
        migrations.AlterField(
            model_name='address',
            name='kana_town',
            field=models.CharField(help_text='町域名カナ', max_length=100, null=True, verbose_name='町域名カナ'),
        ),
        migrations.AlterField(
            model_name='address',
            name='pref',
            field=models.CharField(help_text='都道府県', max_length=50, null=True, verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='address',
            name='town',
            field=models.CharField(help_text='町域名', max_length=255, null=True, verbose_name='町域名'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(help_text='郵便番号', max_length=7, verbose_name='郵便番号'),
        ),
    ]