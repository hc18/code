No. |目录
|:---:|:---|
1. |正则表达式概述
2. |re模块介绍
3. |单字符匹配
4. |原始字符窜
5. |多字符匹配
6. |边界匹配
7. |分组匹配
8. |函数
9. |贪婪和非贪婪
10. |常用正则表达式
11. |镇楼图
####1. 正则表达式概述
- Regular Expression，在代码中常简写为regex、regexp或RE
- 正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。在很多文本编辑器里，正则表达式通常被用来检索、替换那些匹配某个模式的文本。
####2. re模块介绍
####2.1 re模块
- re.match() 能够匹配出以xxx开头的字符串
```
#coding=utf-8
# 导入re模块
import re
# 使用match方法进行匹配操作
result = re.match("hello","hello.cn")
# 如果上一步匹配到数据的话，可以使用group方法来提取数据
print(result.group())

hello
```
####3. 单字符匹配
字符	|功能
|:---:|:---:|
.	|匹配任意1个字符（除了\n）
[ ]	|匹配[ ]中列举的字符
\d	|匹配数字，即0-9
\D	|匹配非数字，即不是数字
\s	|匹配空白，即 空格，tab键
\S	|匹配非空白
\w	|匹配单词字符，即a-z、A-Z、0-9、_
\W	|匹配非单词字符
- 示例1： .
```
>>> import re
>>> ret = re.match(".","a")    # 匹配任意一个
>>> ret.group()
'a'
```
- 示例2：[ ]
```
>>> # coding=utf-8
>>> import re
>>> 
>>> ret = re.match("h", "hello Python")  # 正则表达式区分大小写
>>> ret.group()
'h'
>>> 
>>> ret = re.match("H", "Hello Python")
>>> ret.group()
'H'
>>> 
>>> ret = re.match("[hH]", "hello Python") # 大小写h都可以的情况
>>> ret.group()
'h'
>>> ret = re.match("[hH]", "Hello Python")
>>> ret.group()
'H'
>>> 
>>> ret = re.match("[0123456789]", "7Hello Python") # 匹配数字一
>>> ret.group()
'7'
>>> 
>>> ret = re.match("[0-9]", "7Hello Python") # 匹配数字二
>>> ret.group()
'7'
```
- 示例3：\d
```
# coding=utf-8
import re
ret = re.match("嫦娥1号","嫦娥1号发射成功")
print(ret.group())

嫦娥1号
ret = re.match("嫦娥\d号","嫦娥1号发射成功")
print(ret.group())

嫦娥1号
```
####4. 原始字符窜
- Python中字符串前面加上 r 表示原生字符串
- 如果路径很长，你一定会恨死反斜杠的
```
mm = "c:\\a\\b\\c"
mm
'c:\\a\\b\\c'
print(mm)
c:\a\b\c
re.match("c:\\\\",mm).group()
'c:\\'
ret = re.match("c:\\\\",mm).group()
print(ret)
c:\
ret = re.match("c:\\\\a",mm).group()
print(ret)
c:\a
ret = re.match(r"c:\\a",mm).group()
print(ret)
c:\a
ret = re.match(r"c:\a",mm).group()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
####5.多字符匹配
字符	|功能
|:---:|:---:|
*	|匹配前一个字符出现0次或者无限次，即可有可无
+	|匹配前一个字符出现1次或者无限次，即至少有1次
?	|匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	|匹配前一个字符出现m次
{m,}	|匹配前一个字符至少出现m次
{m,n}	|匹配前一个字符出现从m到n次
- 匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
```
ret = re.match("[A-Z][a-z]*","Mm")
ret.group()
'Mm'

ret = re.match("[A-Z][a-z]*","Aabcdef")
ret.group()
'Aabcdef'
```
- 匹配出，变量名是否有效
```
ret = re.match("[a-zA-Z_]+[\w_]*","name1")
ret.group()
'name1'

ret = re.match("[a-zA-Z_]+[\w_]*","_name")
ret.group()
'_name'

ret = re.match("[a-zA-Z_]+[\w_]*","2_name")
ret.group()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
- 匹配出，0到99之间的数字
```

ret = re.match("[1-9]?[0-9]","7")
ret.group()
'7'

ret = re.match("[1-9]?[0-9]","33")
ret.group()
'33'

ret = re.match("[1-9]?[0-9]","09")
ret.group()
'0'
```
####6. 边界匹配
字符	|功能
|:---:|:---:|
^	|匹配字符串开头
$	|匹配字符串结尾
\b	|匹配一个单词的边界
\B	|匹配非单词边界
- 示例1:匹配163.com的邮箱地址
```
# 正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.com")
ret.group()
'xiaoWang@163.com'

# 不正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.comheihei")
ret.group()
'xiaoWang@163.com'

# 通过$来确定末尾
ret = re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.comheihei")
ret.group()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
- 示例2: \b
```
re.match(r".*\bver\b", "ho ver abc").group()
'ho ver'

re.match(r".*\bver\b", "ho verabc").group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'

re.match(r".*\bver\b", "hover abc").group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
- 示例3：\B
```
>>> re.match(r".*\Bver\B", "hoverabc").group()
'hover'

>>> re.match(r".*\Bver\B", "ho verabc").group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'

>>> re.match(r".*\Bver\B", "hover abc").group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'

>>> re.match(r".*\Bver\B", "ho ver abc").group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
####7. 分组匹配
字符	|功能
|:---:|:---:|
'\|'	|匹配左右任意一个表达式
(ab)	|将括号中字符作为一个分组
\num	|引用分组num匹配到的字符串
(?P<name>)	|分组起别名
(?P=name)	|引用别名为name分组匹配到的字符串
- 匹配出0-100之间的数字
```
#coding=utf-8

import re

ret = re.match("[1-9]?\d","8")
ret.group()
'8'

ret = re.match("[1-9]?\d","78")
ret.group()
'78'

# 不正确的情况
ret = re.match("[1-9]?\d","08")
ret.group()
'0'

# 修正之后的
ret = re.match("[1-9]?\d$","08")
ret.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'

# 添加|
ret = re.match("[1-9]?\d$|100","8")
ret.group()
'8'

ret = re.match("[1-9]?\d$|100","78")
ret.group()
'78'

ret = re.match("[1-9]?\d$|100","08")
ret.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'

ret = re.match("[1-9]?\d$|100","100")
ret.group()
'100'
```
- 匹配出163、126、qq邮箱之间的数字
```
>>> ret = re.match("\w{4,20}@163\.com", "test@163.com")
>>> ret.group()
'test@163.com'
>>> 
>>> ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
>>> ret.group()
'test@126.com'
>>> 
>>> ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
>>> ret.group()
'test@qq.com'
>>> 
>>> ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
>>> ret.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
- group
```
>>> ret = re.match("([^-]*)-(\d+)","010-12345678")
>>> ret.group()
'010-12345678'
>>> ret.group(1)
'010'
>>> ret.group(2)
'12345678'
```
- 匹配出<html>hh</html>
```
# 能够完成对正确的字符串的匹配
>>> ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</html>")
>>> ret.group()
'<html>hh</html>'
>>> 
# 如果遇到非正常的html格式字符串，匹配出错
>>> ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmlbalabala>")
>>> ret.group()
'<html>hh</htmlbalabala>'
>>> 
# 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
>>> ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
>>> ret.group()
'<html>hh</html>'
>>> 
# 因为2对<>中的数据不一致，所以没有匹配出来
>>> ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</htmlbalabala>")
>>> ret.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
- 匹配出<html><h1>www.hello.cn</h1></html>
```
>>> ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.hello.cn</h1></html>")
>>> ret.group()
'<html><h1>www.hello.cn</h1></html>'
>>> 
>>> ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.hello.cn</h2></html>")
>>> ret.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
- 匹配出<html><h1>www.hello.cn</h1></html>(方法二)
```
>>> ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
>>> ret.group()
'<html><h1>www.itcast.cn</h1></html>'
>>> ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.hello.cn</h2></html>")
>>> ret.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```
####8. 函数
####8.1 search
- 匹配出文章阅读的次数
```
#coding=utf-8
import re

ret = re.search(r"\d+", "阅读次数为 9999")
print(ret.group())

9999
```
####8.2 findall
- 统计出python、c、c++相应文章阅读的次数
```
>>> ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
>>> print (ret)
['9999', '7890', '12345']
```
####8.3 sub 将匹配到的数据进行替换
- 将匹配到的阅读次数加1
```
#coding=utf-8
import re

ret = re.sub(r"\d+", '998', "python = 997")
print (ret)

python = 998
```
- 方法二
```
#coding=utf-8
import re

def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret = re.sub(r"\d+", add, "python = 997")
print (ret)

ret = re.sub(r"\d+", add, "python = 99")
print (ret)

python = 998
python = 100
```
####8.4 split 根据匹配进行切割字符串，并返回一个列表
```
#coding=utf-8
import re

ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print (ret)

['info', 'xiaoZhang', '33', 'shandong']
```
####9. 贪婪和非贪婪
- Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；非贪婪则相反，总是尝试匹配尽可能少的字符。
- 在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
```
s="This is a number 234-235-22-423"
r=re.match("(.+)(\d+-\d+-\d+-\d+)",s)
print(r.group(1))
print(r.group(2))
r=re.match("(.+?)(\d+-\d+-\d+-\d+)",s)
print(r.group(1))
print(r.group(2))

This is a number 23
4-235-22-423
This is a number 
234-235-22-423
```
```
>>> re.match(r"aa(\d+)","aa2343ddd").group(1)
'2343'
>>> re.match(r"aa(\d+?)","aa2343ddd").group(1)
'2'
>>> re.match(r"aa(\d+)ddd","aa2343ddd").group(1) 
'2343'
>>> re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
'2343'
```
####10. 常用正则表达式
####10.1 校验数字的表达式
1 |数字|^[0-9]*$
|:---:|---|---|
 2| n位的数字|^\d{n}$
 3| 至少n位的数字|^\d{n,}$
 4| m-n位的数字|^\d{m,n}$
 5| 零和非零开头的数字：|^(0\|[1-9][0-9]*)$
 6 |非零开头的最多带两位小数的数字|^([1-9][0-9]*)+(.[0-9]{1,2})?$
 7 |带1-2位小数的正数或负数|^(\-)?\d+(\.\d{1,2})?$
 8 |正数、负数、和小数|^(\-\|\+)?\d+(\.\d+)?$
 9 |有两位小数的正实数|^[0-9]+(.[0-9]{2})?$
10| 有1~3位小数的正实数|^[0-9]+(.[0-9]{1,3})?$
11| 非零的正整数|^[1-9]\d*$ 或 ^([1-9][0-9]*){1,3}$ 或 ^\+?[1-9][0-9]*$
12| 非零的负整数|^\-[1-9][]0-9"*$ 或 ^-[1-9]\d*$
13 |非负整数|^\d+$ 或 ^[1-9]\d*\|0$
14 |非正整数|^-[1-9]\d*\|0$ 或 ^((-\d+)\|(0+))$
15 |非负浮点数|^\d+(\.\d+)?$ 或 ^[1-9]\d*\.\d*\|0\.\d*[1-9]\d*\|0?\.0+\|0$
16 |非正浮点数|^((-\d+(\.\d+)?)\|(0+(\.0+)?))$ 或 ^(-([1-9]\d*\.\d*\|0\.\d*[1-9]\d*))\|0?\.0+\|0$
17 |正浮点数|^[1-9]\d*\.\d*\|0\.\d*[1-9]\d*$ 或 ^(([0-9]+\.[0-9]*[1-9][0-9]*)\|([0-9]*[1-9][0-9]*\.[0-9]+)\|([0-9]*[1-9][0-9]*))$
18 |负浮点数|^-([1-9]\d*\.\d*\|0\.\d*[1-9]\d*)$ 或 ^(-(([0-9]+\.[0-9]*[1-9][0-9]*)\|([0-9]*[1-9][0-9]*\.[0-9]+)\|([0-9]*[1-9][0-9]*)))$
19 |浮点数|^(-?\d+)(\.\d+)?$ 或 ^-?([1-9]\d*\.\d*\|0\.\d*[1-9]\d*\|0?\.0+\|0)$
####10.2 校验字符的表达式
1 |汉字|^[\u4e00-\u9fa5]{0,}$
|:---:|---|---|
2 |英文和数字|^[A-Za-z0-9]+$ 或 ^[A-Za-z0-9]{4,40}$
3 |长度为3-20的所有字符|^.{3,20}$
4 |由26个英文字母组成的字符串|^[A-Za-z]+$
5 |由26个大写英文字母组成的字符串|^[A-Z]+$
6 |由26个小写英文字母组成的字符串|^[a-z]+$
7 |由数字和26个英文字母组成的字符串|^[A-Za-z0-9]+$
8 |由数字、26个英文字母或者下划线组成的字符串|^\w+$ 或 ^\w{3,20}$
9 |中文、英文、数字包括下划线|^[\u4E00-\u9FA5A-Za-z0-9_]+$
10 |中文、英文、数字但不包括下划线等符号|^[\u4E00-\u9FA5A-Za-z0-9]+$ 或 ^[\u4E00-\u9FA5A-Za-z0-9]{2,20}$
11 |可以输入含有^%&',;=?$\"等字符|[^%&',;=?$\x22]+
12 |禁止输入含有~的字符|[^~\x22]+
####10.3 特殊需求表达式
 1 |mail地址|^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
|:---:|---|---|
 2 |域名|\[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?
 3 |InternetURL|[a-zA-z]+://[^\s]* 或 ^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$
 4 |手机号码|^(13[0-9]\|14[0-9]\|15[0-9]\|166\|17[0-9]\|18[0-9]\|19[8\|9])\d{8}$
 5 |电话号码|^(\(\d{3,4}-)\|\d{3.4}-)?\d{7,8}$ 
 6 |国内电话号码|\d{3}-\d{8}\|\d{4}-\d{7} 
 7 |18位身份证号码(数字、字母x结尾)|^((\d{18})\|([0-9x]{18})\|([0-9X]{18}))$
 8 |帐号是否合法(字母开头，允许5-16字节，允许字母数字下划线)|\^[a-zA-Z][a-zA-Z0-9_]{4,15}$
 9 |密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)|^[a-zA-Z]\w{5,17}$
10 |强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-10之间)|^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$  
11 |日期格式|^\d{4}-\d{1,2}-\d{1,2}
12 |一年的12个月(01～09和1～12)|^(0?[1-9]\|1[0-2])$
13 |一个月的31天(01～09和1～31)|^((0?[1-9])\|((1\|2)[0-9])\|30\|31)$ 
14 |xml文件|^([a-zA-Z]+-?)+[a-zA-Z0-9]+\\.[x\|X][m\|M][l\|L]$
15 |中文字符的正则表达式|[\u4e00-\u9fa5]
16 |双字节字符|[^\x00-\xff]    (包括汉字在内，可以用来计算字符串的长度(一个双字节字符长度计2，ASCII字符计1))
17 |空白行的正则表达式|\n\s*\r    (可以用来删除空白行)
18 |HTML标记的正则表达式|<(\S*?)[^>]*>.*?</\1>\|<.*? />    (网上流传的版本太糟糕，上面这个也仅仅能部分，对于复杂的嵌套标记依旧无能为力)
19 |首尾空白字符的正则表达式|^\s*\|\s*$或(^\s*)\|(\s*$)    (可以用来删除行首行尾的空白字符(包括空格、制表符、换页符等等)，非常有用的表达式)
20 |腾讯QQ号|[1-9][0-9]{4,}    (腾讯QQ号从10000开始)
21 |中国邮政编码|[1-9]\d{5}(?!\d)    (中国邮政编码为6位数字)
22 |IP地址|\d+\.\d+\.\d+\.\d+    (提取IP地址时有用)
23 |IP地址|((?:(?:25[0-5]\|2[0-4]\\d\|[01]?\\d?\\d)\\.){3}(?:25[0-5]\|2[0-4]\\d\|[01]?\\d?\\d)) 
####11. 镇楼图
![这图总结的真好](http://upload-images.jianshu.io/upload_images/6634703-387bc6d93ff2788a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####参考文献
1. http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html（图来源）
2. http://www.cnblogs.com/zxin/archive/2013/01/26/2877765.html（常用正则表达式来源）
