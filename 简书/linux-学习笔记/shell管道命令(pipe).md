||目录|命令
|:---:|:---:|:--:|
1.| 管道命令|\||
2.|选取命令|cut，grep
3.| 排序命令  |sort,wc,uniq
4.| 双重数据流|tee
5.| 字符转换命令|tr, expand, col, join, paste
6.| 切割命令|split
7.| 参数代换|xargs
####1. 管道命令
![image.png](http://upload-images.jianshu.io/upload_images/6634703-46fd1ec8bdba97e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- command1正确输出，作为command2的输入 然后comand2的输出作为，comand3的输入 ，comand3输出就会直接显示在屏幕上面了。
  - 注意：
    - 1、管道命令只处理前一个命令正确输出，不处理错误输出
    - 2、管道命令右边命令，必须能够接收标准输入流命令才行。
####2. 选取命令
####2.1 cut
- 从某一行将一段信息切出来
```
  cut -d '分隔符' -f fields
  cut -c 字符范围
```
-d |后接分隔字符，与-f一起使用
|:---:|:---:|
-f |根据-d将信息分解成数段，-f后接取第n段
-c |以字符为单位取出固定字符区间
```
# 用“：”分割，取第5段
echo $PATH | cut -d ':' -f 5
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-c9087afc2b2bbce8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# 多行分割
last -5
# 用空格分割，取每行第一段
last -5|cut -d ' ' -f 1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f882b96f74851a22.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# 范围分割
last -3
last -3|cut -c -6
last -3|cut -c 6-
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-222c893d604cf93c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2.2 grep
- 分析一行信息，若当中存在我们需要的信息，则将该行输出，grep 后还可接正则表达式或通配符进行查询。

grep |[-acinv] [-A] [-B] [--color=auto] ‘查找字符串’ filename
|:---:|:---:|
-a|将 binary 文件以 text 文件方式查找数据
-c|计算‘查找字符串’次数
-i|忽略大小写
-n|输出行号
-v|反向选择
-A|后面可跟数字，代表除了本行外，后续的 n 行也都列出来
-B |后面可跟数字，代表除了本行外，前面的 n 行也都列出来
--color=auto |关键字部分添加颜色
```
last -3
last -3|grep 'ttys001'
# 匹配不出现‘ttys001’,并显示行号
last -3|grep -vn 'ttys001'
# 显示匹配到的次数
last -3|grep -c 'chengkai'
# 通配符匹配
last -3|grep -n 'ttys00*'
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-e0a92b7939d5d9ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. 排序命令
####3.1 sort
- sort 可以按照不同的数据类型来排序

语法|sort [-fbMnrtuk]文件或输入流
|:---:|:---:|
-f|忽略大小写
-b|忽略最前面的空格
-M|以月份(英文)来排序
-r|反向排序
-t|分隔符与-k 连用
-u|就是 uniq
-k|以那个 field 的进行排序
```
last -3
# 用‘ ’分割第三段进行排序
last -3|sort -t ' ' -k 3
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-208953829cea429d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3.2 wc
- wc 可以帮助我们统计文件字符信息

语法|wc [lwm]
|:---:|:---:|
-i|仅列出行
-w|仅列数字
-m|字符数
```
cat .bash_profile|wc
wc .bash_profile
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d0797d502cfc85af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3.3 uniq
- 将重复的数据仅列出一列

语法|uniq [-ic]
|:---:|:---:|
-i|忽略大小写
-c|进行计数
```
# last|cut -d ' ' -f 1 |sort 截取登录名并排序
# uniq -c 删除重复列,并计数
# sort –n 按照计数排序
last|cut -d ' ' -f 1 |sort|uniq -c|sort -n
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b396554f54daf41c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. 双重数据流
####4.1 tee
- 如果你既想将输出数据流保存到文件也想同时控制台也会显示，那你就需要使用双重数据流了

语法|tee [-a] file
|:---:|:---:|
-a|以累加的方式进行添加
```
# 将最近登录的信息写入至last.list中,在屏幕上只显示登录名
last -3| tee last.list | cut -d ' ' -f1
# 将列表信息累加至homefile中，并在屏幕上显示
last -3| tee -a homefile
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5d2172c91b9280f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5. 字符转换命令
####5.1 tr
- 可以用来删除和替换一些文字信息

说明|tr 只是改变输出内容，并不会真正去修改文件的内容
|:---:|:---:|
语法|tr –d ‘字符’;tr –s ‘原字符’‘替换字符’
-d|删除
-s|替换
```
cat homefile
cat homefile |tr -s 't' 'T'
cat homefile |tr -d 't'
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-acfe2520204570ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5.2 expand
- 将[tab]按键转为空格键

语法|expand [–t] file
|:---:|:---:|
-t|[tab] 按键替换多少个空格字符
```
cat test
# 把[tab] 键替换为1个空格字符
cat test|expand -1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-730578a84c0019fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5.3 col
- 将一些特殊字符进行转换

语法|col [-xb]
|:---:|:---:|
-x|将 tab 键转成相应的空格
-b|在文字内有反斜杠，仅保留反斜杠后面接的那个字符
```
# 将man 命令的帮助文档保存为man_help，使用-b 参数过滤所有控制字符。在终端中使用如下命令：
man man | col -b > man_help
```
####5.4 join
- 主要是在处理“两个文件当中，有 "相同数据" 的那一行，才将他加在一起”的意思

语法| [-ti12] file1 file2
|:---:|:---:|
-t  |join 默认以空白字符分隔数据，并且比对“第一个字段”的数据，如果两个文件相同，则将两笔数据联成一行，且第一个字段放在第一个！
-i  |忽略大小写的差异；
-1  |这个是数字的 1 ，代表“第一个文件要用那个字段来分析”的意思；
-2  |代表“第二个文件要用那个字段来分析”的意思。

```
head test test1
join test test1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-daf38a077ecaf789.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5.5 paste
- paste 就直接“将两行贴在一起，且中间以 [tab] 键隔开”而已

语法 |[-d] file1 file2
|:---:|:---:|
-d  |后面可以接分隔字符。默认是以 [tab] 来分隔的！
-   |如果 file 部分写成 - ，表示来自 standard input 的数据的意思。
```
paste -d "\n" test test1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b96dcd31eb179d55.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####6.切割命令
####6.1 split
- 将大文件分割成多个小文件查看

语法|split [-bl] file PREFIX
|:---:|:---:|
-b|后面可接欲切割的文件大小
-1|以行数进行切割
PREFIX|切割后文件的前导符
```
# 把文件一行一行分开
split -1 test 
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-8edec0139eb1a6a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####7. 参数代换
####7.1 xargs
- 参数代换的作用:
  - 作为某些指令的参数。比如 which, finger ,find ,whereis 等
  - 作为某些不支持管道命令的输入数据流

语法|xargs [-epn] command
|:---:|:---:|
-e|就是 EOF 的意思，后面可接一个字符串，当分析到这个字符串时，就会停止继续工作
-p|在执行每个参数时，都会询问用户
-n|后面接次数，执行 command 的次数
```
cat test 
cut -d ' ' -f 1 test|xargs whereis
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5561347db2e20e4a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####参考文献
1. https://wizardforcel.gitbooks.io/vbird-linux-basic-4e/content/92.html（鸟哥的linux 私房菜）
