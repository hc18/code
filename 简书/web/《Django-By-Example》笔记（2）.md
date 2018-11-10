>学习网站链接  http://www.jianshu.com/u/390b6edb26a8

#第二章 用高级特性来增强你的blog

在上一章中，你创建了一个基础的博客应用。现在你将利用一些高级的特性例如通过email来分享帖子，添加评论，给帖子打上tag，检索出相似的帖子等将它改造成为一个功能更加齐全的博客。在本章中，你将会学习以下几点：

- 通过Django发送email
- 在视图（views）中创建并操作表单
- 通过模型（models）创建表单
- 集成第三方应用
- 构建复杂的查询集（QuerySets)
***
####1. 通过email 分享帖子
- 共四步：
1. 创建一个表单填写他们的姓名，email,和评论等
2. 在view.py文件中创建一个视图，来操作发布的数据
3. 在urls.py 中为新的视图（view）添加一个URL模式
4. 创建一个模板（template）来展示这个表单
####1.1 使用Django创建表单
- 在你blog应用的目录下创建一个forms.py文件，输入以下代码：
```
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                                         widget=forms.Textarea)
```
####1.2 在视图中操作表单
- 当表单成功提交后你必须创建一个新的视图（views）来操作表单和发送email。编辑blog应用下的views.py文件，添加以下代码：
```

```
