>Scrapy是用纯Python实现一个为了爬取网站数据、提取结构性数据而编写的应用框架，用途非常广泛。
Scrapy 使用了 Twisted(其主要对手是Tornado)异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。
####01 Scrapy架构图(绿线是数据流向)：
![image.png](http://upload-images.jianshu.io/upload_images/6634703-ec66b757e5fbfd04.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- Scrapy Engine(引擎): 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。
- Scheduler(调度器): 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎
- Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的---Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，
- Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)，
- Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.
- Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件。
- Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）
####02 入门案例
>以爬取1000本书名和价格信息为例子
######021 下载 Scrapy
```
pip3 install scrapy
```
- 创建一个Scrapy 项目
```
$ scrapy startproject example
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-65ab01ad8d8dd07a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- scrapy.cfg ：项目的配置文件
- example/ ：项目的Python模块，将会从这里引用代码
- items.py ：项目的目标文件
- pipelines.py ：项目的管道文件
- settings.py ：项目的设置文件
- spiders/ ：存储爬虫代码目录
######022. 网页解析
网址：http://books.toscrape.com/
>爬虫核心思想
1 爬虫从哪个或哪些页面开始爬取？
2 对于一个已下载的页面， 提取其中的哪些数据？
3 爬取完当前页面后，接下来爬取哪个或哪些页面？
- 右击鼠标点检查
![image.png](http://upload-images.jianshu.io/upload_images/6634703-886d86ea4d92406b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 找到要抓的内容
![](http://upload-images.jianshu.io/upload_images/6634703-ae10d9233745a8d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 1000本书，每页50本，所以有20页链接要抓取
![image.png](http://upload-images.jianshu.io/upload_images/6634703-158bd65ee1d0e5fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

######023. 代码实现
- 在example/spiders 目录下创建book_spider.py
```
# coding=utf-8
import scrapy
class BooksSpider(scrapy.Spider):
    # 一个项目中可能有多个爬虫，这个爬虫的名字叫"books",
    name = "books"

    # 定义爬虫爬取的起始点， 起始点可以是多个
    start_urls = ['http://books.toscrape.com/']

    # 提取数据
    def parse(self, response):
        # 先定位每一本书，每一本书在<article class="product_pod">里
        for book in response.css('article.product_pod'):
            # 书名在article/h3/a 元素的title里
            # <a title="A Light in the Attic">A Light in the...</a>
            name=book.xpath('./h3/a/@title').extract_first()
            # 书价格在<p class="price_color">$51.77</p>的text中
            price = book.css('p.price_color::text').extract_first()
            yield {
                'name':name,
                'price':price,

            }
    # 提取链接
    # 下一页的url 在ul.pager>li.next>a 里面
        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            # 如果找到下一页的URL， 得到绝对路径， 构造新的Request对象
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse)
```
- 要建立一个Spider， 你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性 和 一个方法。

  - name = "" ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。

  - allow_domains = [] 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。

  - start_urls = () ：爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。

  - parse(self, response) ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
    - 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
    - 生成需要下一页的URL请求。

![image.png](http://upload-images.jianshu.io/upload_images/6634703-158395bae7b44609.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 终端运行代码
```
# scrapy crawl <spider_name>
# -o books.csv 输出到csv文件
$ scrapy crawl books -o books.csv
```
- 查看抓到的内容
```
# 不显示第一行的csv 头部
$ sed -n '2,$p' books.csv | cat -n
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-8642790a8132ceec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

