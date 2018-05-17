# address_api
_日本住所のAPI_

Django REST Framework + Scrapy

１、スクレイピングで郵便データを取得してDB保存
２、日本郵便番号のAPI

Apache設定
```sh
WSGIScriptAlias / /var/www/html/address_api/django_api/wsgi.py
WSGIPythonPath /var/www/html/address_api
WSGIPythonHome /home/ec2-user/.pyenv/versions/3.6.0

Alias /static/ /var/www/html/address_api/static/

<Directory /var/www/html/address_api/django_api>
<Files wsgi.py>
Order deny,allow
Allow from all
</Files>
</Directory>

```
住所取得CRON
日曜日0時0分に実行
```sh
0 0 * * 0 cd /var/www/html/address_api/address_bot/ && ~/.pyenv/shims/scrapy crawl address > /var/tmp/address.log

```

住所APIサーバコマンド
```sh
サーバ再起動
sudo service httpd restart
サーバ停止
sudo service httpd stop
サーバ起動
sudo service httpd start
```

下記の場所にソースを配置する

```sh
/var/www/html/address_api/*
```
管理サイトユーザ作成
```sh
cd /var/www/html/address_api/
python manage.py createsuperuser

例：
$ python manage.py createsuperuser
Username (leave blank to use 'hoge'): admin
Email address: admin@example.com
Password: hogefuga
Password (again): hogefuga
Superuser created successfully.
```

環境起動
```sh
cd /var/www/html/address_api/
python manage.py runserver

```

※画面が崩れる場合、
```sh
cd /var/www/html/address_api/
python manage.py collectstatic
```


API URL


一覧取得
```url
GET /api/v1/address/
```
![一覧取得](https://github.com/sayi65/address_api/blob/master/api_list.png "サンプル")


特定のデータを取得
```url
GET /api/v1/address/?zipcode=0000000
```
![一覧取得](https://github.com/sayi65/address_api/blob/master/api_get_one.png "サンプル")

