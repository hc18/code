####序章
> 本章讲如何用爬虫下载图片
- 项目需求：
  - 下载[360图片](http://image.so.com)网站中艺术分类下的所有图片到本地
####01 页面分析
```
$ scrapy shell 'http://image.so.com/zj?ch=art&sn=30&listtype=new&temp=1'
>>> import json
>>> res = json.loads(response.body.decode('utf8'))
>>> res
```
####02 编码实现
>三步
1 创建Scrapy项目， 并使用 scrapy genspider 命令创建 Spider
2 在配置文件中启用ImagesPipeline, 并指定图片下载目录
3 实现ImageSpider
######1 创建Scrapy项目， 并使用 scrapy genspider 命令创建 Spider
```
$ scrapy startproject so_image
$ cd so_image/
$ scrapy genspider images image.so.com
```
######2 在配置文件中启用ImagesPipeline, 并指定图片下载目录
```
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipline':1,
}
IMAGES_STORE='download_images'
```
######3 实现ImageSpider
```
# 如果报错ModuleNotFoundError: No module named 'PIL'
pip3 install pillow
``` 
