####序章
>本章讲如何用爬虫下载文件
- 项目需求：
  - 下载http://matplotlib.org 网站中所有例子的源码文件到本地
####01 页面分析
######011 分析链接
```
$ scrapy shell http://matplotlib.org/examples/index.html
view(response)
```
- 观察发现，所有链接都在<div class="toctree-wrapper compound">下的每一个<li class="toctree-l2"> 中
![image.png](http://upload-images.jianshu.io/upload_images/6634703-dc74f324230a0520.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 共抓到506条链接
```
>>>from scrapy.linkextractors import LinkExtractor
>>>le = LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2')
>>>links = le.extract_links(response)
>>>[link.url for link in links]
>>> len(links)
506
```
######012 分析页面
```
>>> fetch('http://matplotlib.org/examples/animation/animate_decay.html')
>>> view(response)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b9b8d3e60b778662.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 提取源码下载地址
```
>>> href=response.css('a.reference.external::attr(href)').extract_first()
>>> href
'animate_decay.py'
>>> response.urljoin(href)
'https://matplotlib.org/examples/animation/animate_decay.py'
```
####02 编码实现
>共四步
1 创建Scrapy项目，并使用scrapy genspider 命令创建 Spider
2 在配置文件中启用FilesPipeline, 并指定文件下载目录
3 实现 ExampleItem
4 实现ExamplesSpider
######1 创建Scrapy项目，并使用scrapy genspider 命令创建 Spider
```
$ scrapy startproject matplotlib_examples
$ cd matplotlib_examples
$ scrapy genspider examples matplotlib.org
```
######2 在配置文件(setting.py)中启用FilesPipeline, 并指定文件下载目录
```
ITEM_PIPELINES = {
	'scrapy.pipelines.files.FilesPipeline':1,
}
FILES_STORE = 'examples_src
```
######3 实现 ExampleItem
- 在file_urls 和 files 两个字段， 在items.py中完成如下代码
```
class ExampleItem(scrapy.Item):
	file_urls = scrapy.Field()
	files = scrapy.Field()
```
######4 实现ExamplesSpider (examples.py文件)
```
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import ExampleItem

class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    # 设置其实爬取点
    start_urls = ['http://matplotlib.org/examples/index.html']

    # 提取每个文件的链接，用其构造Request对象并提交
    def parse(self, response):
		le = LinkExtractor(restrict_css='div.toctree-wrapper.compound',deny='/index.html$')
		print(len(le.extract_links(response)))
		for link in le.extract_links(response):
			yield scrapy.Request(link.url,callback=self.parse_example)
	# 分析页面，提取源码下载地址
	def parse_example(self, response):
		href = response.css('a.reference.external::attr(href)').extract_first()
		url = response.urljoin(href)
		example = ExampleItem()
		example['file_urls'] = [url]
		return example       

```
######03 运行结果
```
$ scrapy crawl examples -o examples.json
```
- 文件下载结果信息
```
$ cat examples.json

{"file_urls": ["https://matplotlib.org/examples/animation/animate_decay.py"], "files": [{"url": "https://matplotlib.org/examples/animation/animate_decay.py", "path": "full/769c3346594cdc7614da607216022177d1834c84.py", "checksum": "444b19b47ac56a3680e1a9f801fd612d"}]},
{"file_urls": ["https://matplotlib.org/mpl_examples/api/power_norm_demo.py"], "files": [{"url": "https://matplotlib.org/mpl_examples/api/power_norm_demo.py", "path": "full/db82afab30511b0044a0669a090b72ee2a4aa245.py", "checksum": "e88adcdedb8f1dbfa6a77f80aea9d1d6"}]},
```
- 查看下载目录 exmaples_src
```
$ cat examples_src
```
![](http://upload-images.jianshu.io/upload_images/6634703-4c9bcfa38437e146.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 这串代码看不懂，需要写一个脚本，把这窜代码重命名
- 在pipelines.py 实现 如下代码
```
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import basename,dirname,join

class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        return join(basename(dirname(path)),basename(path))
```
- 修改配置文件, 使用MyFilePipeline 代替 FilesPipeline
```
ITEM_PIPELINES = {
	#'scrapy.pipelines.files.FilesPipeline':1,
	'matplotlib_examples.pipelines.MyFilesPipeline':1,
}
FILES_STORE = 'examples_src'
```
- 删除文件，重新运行爬虫
```
$ rm -r examples_src/full
$ rm examples.json 
$ scrapy crawl examples -o examples.json
$ tree example_src
```
![](http://upload-images.jianshu.io/upload_images/6634703-ed3ecf12a9d31bf0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 最后507个文件按类别被下载到26个目录
![image.png](http://upload-images.jianshu.io/upload_images/6634703-18296aae35504f7b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

