####序章
> 目前，大部分网站都具有用户登录功能，其中某些网站只有在用户登录后才能获得有价值的信息，在爬取这类网站时，Scrapy 爬虫程序需要先模拟用户登录，再爬取内容， 这一章来学习在Scrapy中模拟登录的方法。

####01 登录实质
练手网站http://example.webscraping.com
- 登录上面网站，并login,可以在Network,抓取HTTP响应信息，响应头部中长长的Set-Cookie 字段就是网站服务器程序保存在客户端的Cookie 信息
![image.png](http://upload-images.jianshu.io/upload_images/6634703-68b1ffe64956ce89.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####02 Scrapy 模拟登录
######021 使用FormRequest
- 创建表单
```
$ scrapy shell http://example.webscraping.com/places/default/user/login?_next=/places/default/index
>>> sel = response.xpath('//div[@style]/input')
>>> sel
[<Selector xpath='//div[@style]/input' data='<input name="_next" type="hidden" value='>, <Selector xpath='//div[@style]/input' data='<input name="_formkey" type="hidden" val'>, <Selector xpath='//div[@style]/input' data='<input name="_formname" type="hidden" va'>]
>>> fd = dict(zip(sel.xpath('./@name').extract(), sel.xpath('./@value').extract()))
>>> fd['email']='liushuo@webscraping.com'
>>> fd['password']='12345678'
>>> fd
{'_next': '/places/default/index', '_formkey': 'a827dcb8-c423-4fe6-bde8-dd8dbd299cfe', '_formname': 'login', 'email': 'liushuo@webscraping.com', 'password': '12345678'}
>>> from scrapy.http import FormRequest
>>> request = FormRequest('http://example.webscraping.com/places/default/user/login?_next=/places/default/index',formdata=fd)
>>> fetch(request)
2017-12-24 11:12:11 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (303) to <GET http://example.webscraping.com/places/default/index> from <POST http://example.webscraping.com/places/default/user/login?_next=/places/default/index>
2017-12-24 11:12:11 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://example.webscraping.com/places/default/index> (referer: None)
>>> 'Welcome Liu' in response.text
True
>>> view(response)
True
```
- 用view(response)可以看到已经登录
![image.png](http://upload-images.jianshu.io/upload_images/6634703-13dadc8dcc14f58d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 另一种简单的构建表单的方式，即调用FormRequest 的 from_response方法。调用时需要传入一个Response对象作为第一个参数， 该方法会解析Response对象所包含页面中的<form>元素，帮助用户创建FormRequest 对象，并将隐藏<input>中的信息自动填入表单数据
```
>>>fd = {'email':'liushuo@webscraping.com','password':'12345678'}
>>>request = FormRequest.from_response(response, formdata = fd)
```
- 接下来爬取用户个人信息
```
>>> fetch('http://example.webscraping.com/places/default/user/profile?_next=/places/default/index')
2017-12-24 11:37:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://example.webscraping.com/places/default/user/profile?_next=/places/default/index> (referer: None)
>>> keys = response.css('table label::text').re('(.+):')
>>> keys
['First name', 'Last name', 'E-mail']
>>> values = response.css('table td.w2p_fw::text').extract()
>>> values
['Liu', 'Shuo', 'liushuo@webscraping.com']
>>> dict(zip(keys, values))
{'First name': 'Liu', 'Last name': 'Shuo', 'E-mail': 'liushuo@webscraping.com'}
```
######022 实现登录Spider
```
# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["example.webscraping.com"]
    start_urls = ['http://example.webscraping.com/places/default/user/profile?_next=/places/default/index']

    def parse(self, response):
        # 解析登录后下载的页面, 此例中为用户个人信息页面
        keys = response.css('table label::text').re('(.+):')
        values = response.css('table td.w2p_fw::text').extract()

        yield dict(zip(keys, values))

# 登录页面的url
login_url = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'

def start_requests(self):
    yield Request(self.login_url, callback=self.login)

def login(self, response):
    # 登录页面的解析函数，构造FormRequest对象提交表单
    fd = {'email':'liushuo@webscraping.com','password':'12345678'}
    yield FormRequest.from_response(response, formdata=fd,callback=self.parse_login)

def parse_login(self, response):
    # 登录成功后， 继续爬取start_urls中的页面
    if'Welcom Liu' in response.text:
        yield from super().start_requests()
```
####03 有验证码登录
- 目前，很多网站为了防止爬虫爬取，登录时需要用户输入验证码。下面我们学习如何在爬虫程序中人工识别验证码。
```
class 
```
