>学习网站链接  http://www.jianshu.com/u/390b6edb26a8

#第一章 创建一个blog应用
> 在这本书中，你将学习如何创建完整的Django项目，可以在生产环境中使用。假如你还没有安装Django，在本章的第一部分你将学习如何安装。本章会覆盖如何使用Django去创建一个简单的blog应用。本章的目的是使你对该框架的工作有个基本概念，了解不同的组件之间是如何产生交互，并且教你一些技能通过使用一些基本功能方便地创建Djang项目。你会被引导创建一个完整的项目但是不会对所有的细节都进行详细说明。不同的框架组件将在本书接下来的章节中进行介绍。
本章会覆盖以下几点：

- 安装Django并创建你的第一个项目
- 设计模型（models）并且生成模型（model）数据库迁移
- 给你的模型（models）创建一个管理站点
- 使用查询集（QuerySet）和管理器（managers）
- 创建视图（views），模板（templates）和URLs
- 给列表视图（views）添加页码
- 使用Django内置的视图（views）
***
####1. 安装Django
####1.1 创建虚拟环境
- 每一个虚拟环境都是独立的开发系统，创建虚拟环境就是为了解决不同项目中不同软件版本需求问题
```
# 我用python3.6
pip3 install virtualenv
```
- 创建独立环境
```
virtualenv my_env
```
- 激活独立环境
```
source my_env/bin/activate
```
- 左边出现（my_env）代表激活成功
- deactivate 退出虚拟环境
![image.png](http://upload-images.jianshu.io/upload_images/6634703-ed0c02faa2db76f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####1.2 安装Django
- 以下所有命令都在虚拟环境中使用
```
pip3.6 install Django==1.8.6
```
- 出现下面信息，代表安装成功
![image.png](http://upload-images.jianshu.io/upload_images/6634703-ce951fc813eecb71.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2 创建第一个项目
####2.1 创建一个mysite 项目
```
# 创建一个mysite 项目
django-admin startproject mysite
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f4520f25be364cdc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- manage.py:一个实用的命令行，用来与你的项目进行交互。它是一个对django-admin.py工具的简单封装。你不需要编辑这个文件。
- mysite/:你的项目目录，由以下的文件组成：
  - init.py:一个空文件用来告诉Python这个mysite目录是一个Python模块。
  - settings.py:你的项目的设置和配置。里面包含一些初始化的设置。
  - urls.py:你的URL模式存放的地方。这里定义的每一个URL都映射一个视图（view）。
  - wsgi.py:配置你的项目运行如同一个WSGI应用。
```
# 在数据库中创建初始应用
cd mysite
python manage.py migrate
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6c912a2441a6eba0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2.2 运行开发服务器
```
# 开启开发服务器
python manage.py runserver
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6b81fe836edb7619.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 网页输入http://127.0.0.1:8000/ 有惊喜
![image.png](http://upload-images.jianshu.io/upload_images/6634703-03cfcb7afd811481.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2.3 创建一个应用
```
python manage.py startapp blog
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5d2cdd4dc3b8064a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- ***admin.py***: 在这儿你可以注册你的模型（models）并将它们包含到Django的管理页面中。使用Django的管理页面是可选的。
- ***migrations***: 这个目录将会包含你的应用的数据库迁移。Migrations允许Django跟踪你的模型（model）变化并因此来同步数据库。
- ***models.py***: 你的应用的数据模型（models）。所有的Django应用都需要拥有一个models.py文件，但是这个文件可以是空的。
- ***tests.py***：在这儿你可以为你的应用创建测试。
- ***views.py***：你的应用逻辑将会放在这儿。每一个视图（view）都会接受一个HTTP请求，处理该请求，最后返回一个响应。
####2.3.1 设计blog数据架构
- 把下面代码复制粘贴到blog应用下的models.py文件中
```
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # 标题
    title = models.CharField(max_length=250)
    # 短标签
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    # 外键（Django 一篇帖子只能由一名用户编写，一名用户能编写多篇帖子）
    author = models.ForeignKey(User,
                                related_name='blog_posts')
    # 帖子的主体（内容）
    body = models.TextField()
    # 帖子发表的时间
    publish = models.DateTimeField(default=timezone.now)
    # 帖子创建时间
    created = models.DateTimeField(auto_now_add=True)
    # 帖子更新时间
    updated = models.DateTimeField(auto_now=True)
    # 帖子当前状态
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
                            
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
```
- 在终端安装pytz模块，处理日期
```
pip3 install pytz
```
####2.3.2 激活应用
- 编辑settings.py 文件，在INSTALLED_APPS设置中添加blog
```
INSTALLED_APPS = ( 
    'django.contrib.admin',    
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles',
    'blog',
 )
```
####2.4 创建和进行数据迁移
- 在项目主目录下执行命令
```
# 创建一个数据迁移
python manage.py makemigrations blog
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-444d83504414084b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 同步数据库
```
python manage.py migrate
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-dfe91f94ae8af63b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2.5 为你的模型（models）创建一个管理站点
####2.5.1 创建一个超级用户
```
# 创建一个管理员
python manage.py createsuperuser
```
- 需要输入用户名，邮箱，密码
```
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
- 现在，通过`python manage.py runserver`命令来启动开发服务器，之后在浏览器中打开
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)你会看到管理站点的登录页面，如下所示：
![image.png](http://upload-images.jianshu.io/upload_images/6634703-7daf33b23c2a4d5b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 登陆后页面
![image.png](http://upload-images.jianshu.io/upload_images/6634703-91f589bbd637fb23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 2.5.2 在管理站点中添加你的模型（models）
- 编辑blog 应用下的admin.py文件
```
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
- 刷新浏览器
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b84e16ecb88eb72c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 点击`+Add`可以添加一篇新帖子
![image.png](http://upload-images.jianshu.io/upload_images/6634703-80dfa07a8e3a86b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2.6 定制models的展示形式
- 编辑blog应用下的admin.py 文件
```
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)
```
- 刷新浏览器可以看到页面展示
- ![image.png](http://upload-images.jianshu.io/upload_images/6634703-2540921717fcac07.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3 使用查询集（QuerySet）和管理器（managers）
####3.1 创建对象
- 打开终端运行以下命令
```
python manage.py shell
```
- 然后依次输入以下内容
```
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='admin')
>>> post = Post.objects.create(title='One more post',
                        slug='one-more-post',
                        body='Post body.',
                        author=user)
>>> post.save()
```
- get() 方法允许你从数据库取回一个单独的对象。
####3.2 更新对象
- 现在，改变这篇帖子的标题并且再次保存对象
```
>>> post.title = 'New title'
>>> post.save()
```
>对象的改变一直存在内存中直到执行save()方法
####3.3 取回对象
- 获取一张表中的所有对象
```
>>> all_posts = Post.objects.all()
```
- 执行查询集
```
>>> Post.objects.all()
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5e45643fce88f9a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3.4 使用filter()方法
- 查找所有2017年发表的帖子
```
Post.objects.filter(publish__year=2017)
```
- 2017年发布的所有作者用户名为admin的帖子
- 下面两种写法等价
```
Post.objects.filter(publish__year=2017, author__username='admin')
Post.objects.filter(publish__year=2017).filter(author__username='admin')
```
####3.5 使用exclude()
- 返回所有2015年发布的帖子但是这些帖子的题目开头不能是Why
```
Post.objects.filter(publish__year=2015).exclude(title__startswith='Why')
```
####3.6 使用order_by()
- 取回所有对象并通过它们的标题进行排序
```
Post.objects.order_by('title')
```
- 默认是升序,负号为降序
```
Post.objects.order_by('-title')
```
####3.7 删除对象
- 请注意，删除对象也将删除任何的依赖关系
```
post = Post.objects.get(id=1)
post.delete()
```
####3.8 查询集（QuerySet）什么时候会执行
>只要你喜欢，你可以连接许多的过滤给查询集（QuerySet）而且不会立马在数据库中执行直到这个查询集（QuerySet）被执行。查询集（QuerySet）只有在以下情况中才会执行：
* 在你第一次迭代它们的时候
* 当你对它们的实例进行切片：例如Post.objects.all()[:3]
* 当你对它们进行了打包或缓存
* 当你对它们调用了repr()或len()方法
* 当你明确的对它们调用了list()方法
* 当你在一个声明中测试它，例如bool(), or, and, or if
####3.9 创建model manager
- 编辑你的blog应用下的models.py文件添加如下代码来创建一个管理器（manager）
```
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')
    
class Post(models.Model):
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
```
####4 构建列和详情试图（views）
####4.1 创建列和详情
- 编辑blog应用下中views.py文件
```
from django.shortcuts import render, get_object_or_404
from .models import Post
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
```
####4.2 为视图（views）添加URL模式
- 在blog应用目录下创建一个urls.py文件
```
from django.conf.urls import url
from . import views
urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]
```
- year：需要四位数
- month：需要两位数。不及两位数，开头带上0，比如 01，02
- day：需要两位数。不及两位数开头带上0
- post：可以由单词和连字符组成

编辑你的项目中的mysite文件夹中的urls.py文件
```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^blog/', include('blog.urls',
        namespace='blog',
        app_name='blog')),
]
```
####4.3 模型（models）的标准URLs
- 编辑你的models.py文件添加如下代码
```
from django.core.urlresolvers import reverse
Class Post(models.Model):
    # ...
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])
```
####4.4 为视图（views）创建模板（templates）
- 在blog 应用目录下创建以下目录结构和文件
```
templates/
    blog/
        base.html
        post/
            list.html
            detail.html
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-e0ae9b8c789019bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- base.html
```
{% load staticfiles %}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
  <link href="{% static "css/blog.css" %}" rel="stylesheet">
</head>
<body>
  <div id="content">
    {% block content %}
    {% endblock %}
  </div>
  <div id="sidebar">
    <h2>My blog</h2>
      <p>This is my blog.</p>
  </div>
</body>
</html>
```
- list.html
```
{% extends "blog/base.html" %}

{% block title %}My Blog{% endblock %}

{% block content %}
  <h1>My Blog</h1>
  {% for post in posts %}
    <h2>
      <a href="{{ post.get_absolute_url }}">
        {{ post.title }}
      </a>
    </h2>
    <p class="date">
      Published {{ post.publish }} by {{ post.author }}
    </p>
    {{ post.body|truncatewords:30|linebreaks }}
  {% endfor %}
{% endblock %}
```
- 打开终端执行命令`python manage.py runserver`来启动开发服务器。在浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) 你会看到运行结果。
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b0261873edad9a57.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- detail.html
```{% extends "blog/base.html" %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
  <h1>{{ post.title }}</h1>
  <p class="date">
    Published {{ post.publish }} by {{ post.author }}
  </p>
  {{ post.body|linebreaks }}
{% endblock %}
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-2c954b8b21f0389e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4.5 添加页码
- 编辑blog应用下的views.py
```
from django.shortcuts import render, get_object_or_404
from .models import Post
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
```
- 在blog应用的templates文件夹下创建一个新文件命名为pagination.html
```
<div class="pagination">
  <span class="step-links">
    {% if page.has_previous %}
      <a href="?page={{ page.previous_page_number }}">Previous</a>
    {% endif %}
    <span class="current">
      Page {{ page.number }} of {{ page.paginator.num_pages }}.
    </span>
      {% if page.has_next %}
        <a href="?page={{ page.next_page_number }}">Next</a>
      {% endif %}
  </span>
</div>
```
- 编辑list.html模版
```
{% block content %}
  ...
  {% include "pagination.html" with page=posts %}
{% endblock %}
```
- 现在，在你的浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)。 你会看到帖子列的底部已经有分页处理：

![image.png](http://upload-images.jianshu.io/upload_images/6634703-4d7bf3c9751e6e28.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4.6 使用基于类的视图（views）
- 编辑你的blog应用下的views.py文件
```
from django.views.generic import ListView
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
```
- 打开你的blog应用下的urls.py文件，替换urlpatterns
```
urlpatterns = [
    # post views
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(),name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]
```
- 编辑post_list.html模版
```
{% include "pagination.html" with page=page_obj %}
```
####5 总结
1. 可能水平有限，看不懂作者的行文思路，有时候都不知道自己在做什么～
2. 由于是第一章，算是概述，即对整本书的概览，所以很多步骤，我都没有深究
3. 很多代码都不知道什么意思，但我还是坚持把教程给重复出来了（每一步都亲测可行），只是想实现自己搭一个博客的愿望，虽然很难，但我不会放弃的。
