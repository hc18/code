####序章
> 本章介绍scrapy shell 以及优化前一章[《Scrapy框架》](https://www.jianshu.com/p/f97b80a57b51)的代码
- 项目需求：
  - 去网站爬取： http://books.toscrape.com
  - 提取信息包括：书名，价格，评价等级，产品编码， 库存量， 评价数量。
  - 爬取的结果保存到csv中
#### 01. scrapy shell
- 用 scrapy shell <URL> 命令，它可以使用户可以在交互式命令下操作一个Scrapy爬虫，从而提高开发效率
```
$ scrapy shell http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
```
```
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x101885cf8>
[s]   item       {}
[s]   request    <GET http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html>
[s]   response   <200 http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html>
[s]   settings   <scrapy.settings.Settings object at 0x106c28860>
[s]   spider     <DefaultSpider 'default' at 0x1099c17f0>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>>
```
- Scrapy Shell根据下载的页面会自动创建一些方便使用的对象，例如 Response 对象，以及 Selector 对象 (对HTML及XML内容)。
- 当shell载入后，将得到一个包含response数据的本地 response 变量，输入 response.body将输出response的包体，输出 response.headers 可以看到response的包头。
- 输入 response.selector 时， 将获取到一个response 初始化的类 Selector 的对象，此时可以通过使用 response.selector.xpath()或response.selector.css() 来对 response 进行查询。
######012. Selectors选择器
>Scrapy Selectors 内置 XPath 和 CSS Selector 表达式机制
- Selector有四个基本的方法，最常用的还是xpath:
  - xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表
  - extract(): 序列化该节点为Unicode字符串并返回list
  - css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表，语法同 BeautifulSoup4
  - re(): 根据传入的正则表达式对数据进行提取，返回Unicode字符串list列表
>XPath表达式的例子及对应的含义:
```
/html/head/title: 选择<HTML>文档中 <head> 标签内的 <title> 元素
/html/head/title/text(): 选择上面提到的 <title> 元素的文字
//td: 选择所有的 <td> 元素
//div[@class="mine"]: 选择所有具有 class="mine" 属性的 div 元素
```
#### 02. 页面分析
```
# 交互行输入
>>> view(response)
```
- 注意这个页面虽然和浏览器打开的一样，但是这是scrapy 爬虫下载的页面。在进行分析时，使用view函数更加可靠
![image.png](http://upload-images.jianshu.io/upload_images/6634703-2b9bb1e54baf3395.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 提取页面数据
```
>>> sel=response.css('table.table.table-striped')
>>> sel.xpath('(.//tr)[1]/td/text()').extract_first()
'a897fe39b1053632'
>>> sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')
'22'
>>> sel.xpath('(.//tr)[last()]/td/text()').extract_first()
'0'
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6f2f22eed3ee5b4e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 提取页面链接
```
>>> fetch('http://books.toscrape.com/')
2017-12-22 10:42:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://books.toscrape.com/> (referer: None)
>>> view(response)
True
>>> from scrapy.linkextractors import LinkExtractor
>>> le = LinkExtractor(restrict_css='article.product_pod')
>>> le.extract_links(response)
```
```
[Link(url='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html', text='', fragment='', nofollow=False), 
Link(url='http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html', text='', fragment='', nofollow=False), 
Link(url='http://books.toscrape.com/catalogue/soumission_998/index.html', text='', fragment='', nofollow=False), 
Link(url='http://books.toscrape.com/catalogue/sharp-objects_997/index.html', text='', fragment='', nofollow=False), 
...
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-1fbf9fc4c25620fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####03 编码实现
######031创建一个scrapy项目
```
$ scrapy startproject toscrape_book
```
- 创建Spider 文件以及Spider 类
- scrapy genspider <爬虫名字> <要爬取的网站>
```
cd toscrape_book/
scrapy genspider books books.toscrape.com
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-4754d08bc1abfc8a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

######032 items.py
- 在 toscrape_book/items.py 中添加封装书籍信息的Item类, 代码如下
```
class BookItem(scrapy.Item):
	name = scrapy.Field()				#书名
	price = scrapy.Field()				#价格吗
	review_rating = scrapy.Field()		#评价等级
	review_num = scrapy.Field()			#评价数量
	upc = scrapy. Field()				#产品编码
	stock = scrapy. Field()				#库存量
```
###### 033 books.py
```
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # 书籍列表页面的解析函数
    def parse(self, response):
        # 提取书籍列表页面中每本书的链接
        le = LinkExtractor(restrict_css='article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)

        # 提取"下一页"的链接
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le. extract_links(response)
        if links:
            next_url = link[0].url
            yield scrapy.Request(next_url, callback=self.parse)
    # 书籍页面的解析函数
    def parse_book(self,response):
        book = BookItem()
        sel = response.css('div.product_main')
        book['name'] = sel.xpath('./h1/text()').extract_first()
        book['price'] = sel.css('p.price_color::text').extract_first()
        book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating([A-Za-z]+)')

        sel = response.css('table.table.table-striped')
        book['upc']=sel.xpath('(.//tr)[1]/td/text()').extract_first()
        book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')
        book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()

        yield book
```
######034 pipelines.py
- 用户评分输出是one-five, 不好看，把这个输出换成1-5
```
class ToscrapeBookPipeline(object):
    review_rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.review_rating_map[rating]

        return item
```
######035 settings.py
```
# 输出顺序固定
FEED_EXPORT_FIELDS = ['upc','name','price','stock','review_rating','review_num']
# 把注释去掉，启用BookPipeline
ITEM_PIPELINES = {
    'toscrape_book.pipelines.ToscrapeBookPipeline': 300,
}
```
####04 运行爬虫
```
$ scrapy crawl books -o books.csv
$ cat -n books.csv
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b9af48f01f8d86e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
