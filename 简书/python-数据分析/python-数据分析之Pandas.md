(这篇文章很长，建议收藏起来，用到时再检索)
##pandas简介
- Pandas是python的一个数据分析包
- 官网链接：[http://pandas.pydata.org/](http://pandas.pydata.org/)
- 具备按轴自动或显式数据对齐功能的数据结构
- 集成时间序列功能
- 既能处理时间序列数据也能处理非时间序列数据的数据结构
- 数学运算和约简（比如对某个轴求和）可以根据不同的元数据（轴编号）执行
- 灵活处理缺失数据
-  合并及其他出现在常见数据库（例如基于SQL的）中的关系型运算
###1. 数据结构
####1.1 Series
- Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型） 以及一组与之相关的数据标签（即索引）组成。
- Series的字符串表现形式为：索引在左边，值在右边。
```
>>> from pandas import Series
>>> print ('用数组生成Series')
用数组生成Series
>>> obj = Series([4, 7, -5, 3])
>>> print (obj)

0    4
1    7
2   -5
3    3
dtype: int64

>>> print (obj.values)

[ 4  7 -5  3]

>>> print (obj.index)

RangeIndex(start=0, stop=4, step=1)
```
```
>>> print ('指定Series的index')
指定Series的index
>>> obj2 = Series([4, 7, -5, 3], index = ['d', 'b', 'a', 'c'])
>>> print (obj2)

d    4
b    7
a   -5
c    3
dtype: int64

>>> print (obj2.index)

Index(['d', 'b', 'a', 'c'], dtype='object')

>>> print (obj2['a'])

-5

>>> obj2['d'] = 6
>>> print (obj2[['c', 'a', 'd']])

c    3
a   -5
d    6
dtype: int64

>>> print (obj2[obj2 > 0])  # 找出大于0的元素

d    6
b    7
c    3
dtype: int64

>>> print ('b' in obj2) # 判断索引是否存在

True

>>> print ('e' in obj2)

False

>>> print ('替换index')

替换index

>>> obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
>>> print (obj)

Bob      4
Steve    7
Jeff    -5
Ryan     3
dtype: int64
```
```
>>> print ('使用字典生成Series')

使用字典生成Series

>>> sdata = {'Ohio':45000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
>>> obj3 = Series(sdata)
>>> print (obj3)

Ohio      45000
Oregon    16000
Texas     71000
Utah       5000
dtype: int64

>>> print ('使用字典生成Series，并额外指定index，不匹配部分为NaN。')

使用字典生成Series，并额外指定index，不匹配部分为NaN。

>>> states = ['California', 'Ohio', 'Oregon', 'Texas']
>>> obj4 = Series(sdata, index = states)
>>> print (obj4)

California        NaN
Ohio          45000.0
Oregon        16000.0
Texas         71000.0
dtype: float64

>>> print ('Series相加，相同索引部分相加。')

Series相加，相同索引部分相加。

>>> print (obj3 + obj4)

California         NaN
Ohio           90000.0
Oregon         32000.0
Texas         142000.0
Utah               NaN
dtype: float64

>>> print ('指定Series及其索引的名字')

指定Series及其索引的名字

>>> obj4.name = 'population'
>>> obj4.index.name = 'state'
>>> print (obj4)

state
California        NaN
Ohio          45000.0
Oregon        16000.0
Texas         71000.0
Name: population, dtype: float64

```
####1.2 Dataframe
- DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同 的值类型（数值、字符串、布尔值等）。 
- DataFrame既有行索引也有列索引，它可以被看做由Series组成的字典（共用 同一个索引）

![image.png](http://upload-images.jianshu.io/upload_images/6634703-90f4584ecef47a2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('用字典生成DataFrame，key为列的名字。')

用字典生成DataFrame，key为列的名字。

>>> data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
...         'year':[2000, 2001, 2002, 2001, 2002],
...         'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
>>> print (DataFrame(data))

   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002

>>> print (DataFrame(data, columns = ['year', 'state', 'pop'])) # 指定列 顺序

   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9

```
```
>>> print ('指定索引，在列中指定不存在的列，默认数据用NaN。')

指定索引，在列中指定不存在的列，默认数据用NaN。

>>> frame2 = DataFrame(data,
...                     columns = ['year', 'state', 'pop', 'debt'],
...                     index = ['one', 'two', 'three', 'four', 'five'])
>>> print (frame2)

       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  2.4  NaN
five   2002  Nevada  2.9  NaN

>>> print (frame2['state'])

one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
Name: state, dtype: object

>>> print (frame2.year)

one      2000
two      2001
three    2002
four     2001
five     2002
Name: year, dtype: int64

>>> print (frame2.ix['three'])

year     2002
state    Ohio
pop       3.6
debt      NaN
Name: three, dtype: object

>>> frame2['debt'] = 16.5 # 修改一整列
>>> print (frame2)

       year   state  pop  debt
one    2000    Ohio  1.5  16.5
two    2001    Ohio  1.7  16.5
three  2002    Ohio  3.6  16.5
four   2001  Nevada  2.4  16.5
five   2002  Nevada  2.9  16.5

>>> frame2.debt = np.arange(5)  # 用numpy数组修改元素
>>> print (frame2)

       year   state  pop  debt
one    2000    Ohio  1.5     0
two    2001    Ohio  1.7     1
three  2002    Ohio  3.6     2
four   2001  Nevada  2.4     3
five   2002  Nevada  2.9     4
```
```
>>> print ('用Series指定要修改的索引及其对应的值，没有指定的默认数据用NaN。')

用Series指定要修改的索引及其对应的值，没有指定的默认数据用NaN。

>>> val = Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
>>> frame2['debt'] = val
>>> print (frame2)

       year   state  pop  debt
one    2000    Ohio  1.5   NaN
two    2001    Ohio  1.7  -1.2
three  2002    Ohio  3.6   NaN
four   2001  Nevada  2.4  -1.5
five   2002  Nevada  2.9  -1.7
```
```
>>> print ('赋值给新列')

赋值给新列

>>> frame2['eastern'] = (frame2.state == 'Ohio')  # 如果state等于Ohio为True
>>> print (frame2)

       year   state  pop  debt  eastern
one    2000    Ohio  1.5   NaN     True
two    2001    Ohio  1.7  -1.2     True
three  2002    Ohio  3.6   NaN     True
four   2001  Nevada  2.4  -1.5    False
five   2002  Nevada  2.9  -1.7    False

>>> print (frame2.columns)

Index(['year', 'state', 'pop', 'debt', 'eastern'], dtype='object')
```
```
>>> print ('DataFrame转置')

DataFrame转置

>>> pop = {'Nevada':{2001:2.4, 2002:2.9},
...         'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
>>> frame3 = DataFrame(pop)
>>> print (frame3)

      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.6

>>> print (frame3.T)

        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.6
```
```
>>> print ('指定索引顺序，以及使用切片初始化数据。')
指定索引顺序，以及使用切片初始化数据。
>>> print (DataFrame(pop, index = [2001, 2002, 2003]))
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
2003     NaN   NaN
>>> pdata = {'Ohio':frame3['Ohio'][:-1], 'Nevada':frame3['Nevada'][:2]}
>>> print (DataFrame(pdata))
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
```
```
>>> print ('指定索引和列的名称')
指定索引和列的名称
>>> frame3.index.name = 'year'
>>> frame3.columns.name = 'state'
>>> print (frame3)
state  Nevada  Ohio
year
2000      NaN   1.5
2001      2.4   1.7
2002      2.9   3.6
>>> print (frame3.values)
[[ nan  1.5]
 [ 2.4  1.7]
 [ 2.9  3.6]]
>>> print (frame2.values)
[[2000 'Ohio' 1.5 nan True]
 [2001 'Ohio' 1.7 -1.2 True]
 [2002 'Ohio' 3.6 nan True]
 [2001 'Nevada' 2.4 -1.5 False]
 [2002 'Nevada' 2.9 -1.7 False]]
```
####1.3 索引对象
- pandas中主要的index对象 

![image.png](http://upload-images.jianshu.io/upload_images/6634703-b8edc06cd7181e3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- Index的方法和属性 

![image.png](http://upload-images.jianshu.io/upload_images/6634703-c47d0659788b0f99.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-8196a45207247644.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
>>> import numpy as np
>>> import pandas as pd
>>> import sys
>>> from pandas import Series, DataFrame, Index
>>>
>>> print ('获取index')
获取index
>>> obj = Series(range(3), index = ['a', 'b', 'c'])
>>> index = obj.index
>>> print (index[1:])
Index(['b', 'c'], dtype='object')
>>> try:
...     index[1] = 'd'  # index对象不可修改，所以会报错
... except:
...     print (sys.exc_info()[0])
...
<class 'TypeError'>
```
```
>>> print ('使用Index对象')
使用Index对象
>>> index = Index(np.arange(3))
>>> obj2 = Series([1.5, -2.5, 0], index = index)
>>> print (obj2)
0    1.5
1   -2.5
2    0.0
dtype: float64
>>> print (obj2.index is index)
True
```
```
>>> print ('判断列和索引是否存在')
判断列和索引是否存在
>>> pop = {'Nevada':{20001:2.4, 2002:2.9},
...         'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
>>> frame3 = DataFrame(pop)
>>> print ('Ohio' in frame3.columns)
True
>>> print ('2003' in frame3.index)
False
```
###2. 基本功能
####2.1 重新索引
- 创建一个适应新索引的新对象，该Series的reindex将会根据新索引进行重排。 如果某个索引值当前不存在，就引入缺失值 
- 对于时间序列这样的有序数据，重新索引时可能需要做一些插值处理。 method选项即可达到此目的

![image.png](http://upload-images.jianshu.io/upload_images/6634703-47d17540b49739d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
>>> import numpy as np
>>> from pandas import DataFrame, Series
>>>
>>> print ('重新指定索引及顺序')
重新指定索引及顺序
>>> obj = Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
>>> print (obj)
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
>>> obj2 = obj.reindex(['a', 'b', 'd', 'c', 'e'])
>>> print (obj2)
a   -5.3
b    7.2
d    4.5
c    3.6
e    NaN
dtype: float64
>>> print (obj.reindex(['a', 'b', 'd', 'c', 'e'], fill_value = 0))  # 指 定不存在元素的默认值
a   -5.3
b    7.2
d    4.5
c    3.6
e    0.0
dtype: float64
```
```
>>> print ('重新指定索引并指定填元素充方法')
重新指定索引并指定填元素充方法
>>> obj3 = Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
>>> print (obj3)
0      blue
2    purple
4    yellow
dtype: object
>>> print (obj3.reindex(range(6), method = 'ffill'))
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
```
```
>>> print ('对DataFrame重新指定索引')
对DataFrame重新指定索引
>>> frame = DataFrame(np.arange(9).reshape(3, 3),
...                   index = ['a', 'c', 'd'],
...                   columns = ['Ohio', 'Texas', 'California'])
>>> print (frame)
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8
>>> frame2 = frame.reindex(['a', 'b', 'c', 'd'])
>>> print (frame2)
   Ohio  Texas  California
a   0.0    1.0         2.0
b   NaN    NaN         NaN
c   3.0    4.0         5.0
d   6.0    7.0         8.0
```
```
>>> print ('重新指定column')
重新指定column
>>> states = ['Texas', 'Utah', 'California']
>>> print (frame.reindex(columns = states))
   Texas  Utah  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8
```
```
>>> print ('对DataFrame重新指定索引并指定填元素充方法')
对DataFrame重新指定索引并指定填元素充方法
>>> print (frame.reindex(index = ['a', 'b', 'c', 'd'],
...                     method = 'ffill').reindex(columns = states))
   Texas  Utah  California
a      1   NaN           2
b      1   NaN           2
c      4   NaN           5
d      7   NaN           8
>>> print (frame.ix[['a', 'b', 'd', 'c'], states])
   Texas  Utah  California
a    1.0   NaN         2.0
b    NaN   NaN         NaN
d    7.0   NaN         8.0
c    4.0   NaN         5.0
```
####2.2 丢弃指定轴上的项
- 丢弃某条轴上的一个或多个项很简单，只要有一个索引数组或列表即可。由于 需要执行一些数据整理和集合逻辑，所以drop方法返回的是一个在指定轴上删 除了指定值的新对象 
```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('Series根据索引删除元素')
Series根据索引删除元素
>>> obj = Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])
>>> new_obj = obj.drop('c')
>>> print (new_obj)
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
>>> print (obj.drop(['d', 'c']))
a    0.0
b    1.0
e    4.0
dtype: float64
```
```
>>> print ('DataFrame删除元素，可指定索引或列。')
DataFrame删除元素，可指定索引或列。
>>> data = DataFrame(np.arange(16).reshape((4, 4)),
...                   index = ['Ohio', 'Colorado', 'Utah', 'New York'],
...                   columns = ['one', 'two', 'three', 'four'])
>>> print (data)
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
>>> print (data.drop(['Colorado', 'Ohio']))
          one  two  three  four
Utah        8    9     10    11
New York   12   13     14    15
>>> print (data.drop('two', axis = 1))
          one  three  four
Ohio        0      2     3
Colorado    4      6     7
Utah        8     10    11
New York   12     14    15
>>> print (data.drop(['two', 'four'], axis = 1))
          one  three
Ohio        0      2
Colorado    4      6
Utah        8     10
New York   12     14
```
####2.3 索引、选取和过滤
- Series索引（obj[...]）的工作方式类似于NumPy数组的索引，只不过Series的 索引值不只是整数。
- 利用标签的切片运算与普通的Python切片运算不同，其末端是包含的 （inclusive）。
- 对DataFrame进行索引其实就是获取一个或多个列
- 为了在DataFrame的行上进行标签索引，引入了专门的索引字段ix
##### DataFrame的索引选项

![image.png](http://upload-images.jianshu.io/upload_images/6634703-67e40464d962170d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('Series的索引，默认数字索引可以工作。')
Series的索引，默认数字索引可以工作。
>>> obj = Series(np.arange(4.), index = ['a', 'b', 'c', 'd'])
>>> print (obj['b'])
1.0
>>> print (obj[3])
3.0
>>> print (obj[[1, 3]])
b    1.0
d    3.0
dtype: float64
>>> print (obj[obj < 2])
a    0.0
b    1.0
dtype: float64
```
```
>>> print ('Series的数组切片')
Series的数组切片
>>> print (obj['b':'c'])  # 闭区间
b    1.0
c    2.0
dtype: float64
>>> obj['b':'c'] = 5
>>> print (obj)
a    0.0
b    5.0
c    5.0
d    3.0
dtype: float64
```
```
>>> print ('DataFrame的索引')
DataFrame的索引
>>> data = DataFrame(np.arange(16).reshape((4, 4)),
...                   index = ['Ohio', 'Colorado', 'Utah', 'New York'],
...                   columns = ['one', 'two', 'three', 'four'])
>>> print (data)
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
>>> print (data['two']) # 打印列
Ohio         1
Colorado     5
Utah         9
New York    13
Name: two, dtype: int32
>>> print (data[['three', 'one']])
          three  one
Ohio          2    0
Colorado      6    4
Utah         10    8
New York     14   12
>>> print (data[:2])
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
>>> print (data.ix['Colorado', ['two', 'three']]) # 指定索引和列
two      5
three    6
Name: Colorado, dtype: int32
>>> print (data.ix[['Colorado', 'Utah'], [3, 0, 1]])
          four  one  two
Colorado     7    4    5
Utah        11    8    9
>>> print (data.ix[2])  # 打印第2行（从0开始）
one       8
two       9
three    10
four     11
Name: Utah, dtype: int32
>>> print (data.ix[:'Utah', 'two']) # 从开始到Utah，第2列。
Ohio        1
Colorado    5
Utah        9
Name: two, dtype: int32
```
```
>>> print ('根据条件选择')
根据条件选择
>>> print (data[data.three > 5])
          one  two  three  four
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
>>> print (data < 5)  # 打印True或者False
            one    two  three   four
Ohio       True   True   True   True
Colorado   True  False  False  False
Utah      False  False  False  False
New York  False  False  False  False
>>> data[data < 5] = 0
>>> print (data)
          one  two  three  four
Ohio        0    0      0     0
Colorado    0    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
```
####2.4 算术运算和数据对齐
```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('加法')
加法
>>> s1 = Series([7.3, -2.5, 3.4, 1.5], index = ['a', 'c', 'd', 'e'])
>>> s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index = ['a', 'c', 'e', 'f', 'g'])
>>> print (s1)
a    7.3
c   -2.5
d    3.4
e    1.5
dtype: float64
>>> print (s2)
a   -2.1
c    3.6
e   -1.5
f    4.0
g    3.1
dtype: float64
>>> print (s1 + s2)
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64
```
```
>>> print ('DataFrame加法，索引和列都必须匹配。')
DataFrame加法，索引和列都必须匹配。
>>> df1 = DataFrame(np.arange(9.).reshape((3, 3)),
...                 columns = list('bcd'),
...                 index = ['Ohio', 'Texas', 'Colorado'])
>>> df2 = DataFrame(np.arange(12).reshape((4, 3)),
...                 columns = list('bde'),
...                 index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
>>> print (df1)
            b    c    d
Ohio      0.0  1.0  2.0
Texas     3.0  4.0  5.0
Colorado  6.0  7.0  8.0
>>> print (df2)
        b   d   e
Utah    0   1   2
Ohio    3   4   5
Texas   6   7   8
Oregon  9  10  11
>>> print (df1 + df2)
            b   c     d   e
Colorado  NaN NaN   NaN NaN
Ohio      3.0 NaN   6.0 NaN
Oregon    NaN NaN   NaN NaN
Texas     9.0 NaN  12.0 NaN
Utah      NaN NaN   NaN NaN
```
```
>>> print ('数据填充')
数据填充
>>> df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns = list('abcd'))
>>> df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns = list('abcde'))
>>> print (df1)
     a    b     c     d
0  0.0  1.0   2.0   3.0
1  4.0  5.0   6.0   7.0
2  8.0  9.0  10.0  11.0
>>> print (df2)
      a     b     c     d     e
0   0.0   1.0   2.0   3.0   4.0
1   5.0   6.0   7.0   8.0   9.0
2  10.0  11.0  12.0  13.0  14.0
3  15.0  16.0  17.0  18.0  19.0
>>> print (df1.add(df2, fill_value = 0))
      a     b     c     d     e
0   0.0   2.0   4.0   6.0   4.0
1   9.0  11.0  13.0  15.0   9.0
2  18.0  20.0  22.0  24.0  14.0
3  15.0  16.0  17.0  18.0  19.0
>>> print (df1.reindex(columns = df2.columns, fill_value = 0))
     a    b     c     d  e
0  0.0  1.0   2.0   3.0  0
1  4.0  5.0   6.0   7.0  0
2  8.0  9.0  10.0  11.0  0
```
```
>>> print ('DataFrame与Series之间的操作')
DataFrame与Series之间的操作
>>> arr = np.arange(12.).reshape((3, 4))
>>> print (arr)
[[  0.   1.   2.   3.]
 [  4.   5.   6.   7.]
 [  8.   9.  10.  11.]]
>>> print (arr[0])
[ 0.  1.  2.  3.]
>>> print (arr - arr[0])
[[ 0.  0.  0.  0.]
 [ 4.  4.  4.  4.]
 [ 8.  8.  8.  8.]]
>>> frame = DataFrame(np.arange(12).reshape((4, 3)),
...                   columns = list('bde'),
...                   index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
>>> series = frame.ix[0]
>>> print (frame)
        b   d   e
Utah    0   1   2
Ohio    3   4   5
Texas   6   7   8
Oregon  9  10  11
>>> print (series)
b    0
d    1
e    2
Name: Utah, dtype: int32
>>> print (frame - series)
        b  d  e
Utah    0  0  0
Ohio    3  3  3
Texas   6  6  6
Oregon  9  9  9
>>> series2 = Series(range(3), index = list('bef'))
>>> print (frame + series2)
          b   d     e   f
Utah    0.0 NaN   3.0 NaN
Ohio    3.0 NaN   6.0 NaN
Texas   6.0 NaN   9.0 NaN
Oregon  9.0 NaN  12.0 NaN
>>> series3 = frame['d']
>>> print (frame.sub(series3, axis = 0))  # 按列减
        b  d  e
Utah   -1  0  1
Ohio   -1  0  1
Texas  -1  0  1
Oregon -1  0  1
```
####2.5 函数应用和映射
```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('函数')
函数
>>> frame = DataFrame(np.random.randn(4, 3),
...                   columns = list('bde'),
...                   index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
>>> print (frame)
               b         d         e
Utah    0.490747 -0.001959 -0.160986
Ohio    0.743594 -1.157825  1.067688
Texas  -0.607442  0.785016 -0.496046
Oregon  1.720088  0.149294 -1.645419
>>> print (np.abs(frame))
               b         d         e
Utah    0.490747  0.001959  0.160986
Ohio    0.743594  1.157825  1.067688
Texas   0.607442  0.785016  0.496046
Oregon  1.720088  0.149294  1.645419
```
```
>>> print ('lambda以及应用')
lambda以及应用
>>> f = lambda x: x.max() - x.min()
>>> print (frame.apply(f))
b    2.327530
d    1.942841
e    2.713107
dtype: float64
>>> print (frame.apply(f, axis = 1))
Utah      0.651733
Ohio      2.225513
Texas     1.392458
Oregon    3.365508
dtype: float64
```
```
>>> _format = lambda x: '%.2f' % x
>>> print (frame.applymap(_format))
            b      d      e
Utah     0.49  -0.00  -0.16
Ohio     0.74  -1.16   1.07
Texas   -0.61   0.79  -0.50
Oregon   1.72   0.15  -1.65
>>> print (frame['e'].map(_format))
Utah      -0.16
Ohio       1.07
Texas     -0.50
Oregon    -1.65
Name: e, dtype: object
```
####2.6 排序和排名
```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('根据索引排序，对于DataFrame可以指定轴。')
根据索引排序，对于DataFrame可以指定轴。
>>> obj = Series(range(4), index = ['d', 'a', 'b', 'c'])
>>> print (obj.sort_index())
a    1
b    2
c    3
d    0
dtype: int32
>>> frame = DataFrame(np.arange(8).reshape((2, 4)),
...                   index = ['three', 'one'],
...                   columns = list('dabc'))
>>> print (frame.sort_index())
       d  a  b  c
one    4  5  6  7
three  0  1  2  3
>>> print (frame.sort_index(axis = 1))
       a  b  c  d
three  1  2  3  0
one    5  6  7  4
>>> print (frame.sort_index(axis = 1, ascending = False)) # 降序
       d  c  b  a
three  0  3  2  1
one    4  7  6  5
```
```
>>> print ('根据值排序')
根据值排序
>>> obj = Series([4, 7, -3, 2])
>>> print (obj.sort_values()) # order已淘汰
2   -3
3    2
0    4
1    7
dtype: int64
```
```
>>> print ('DataFrame指定列排序')
DataFrame指定列排序
>>> frame = DataFrame({'b':[4, 7, -3, 2], 'a':[0, 1, 0, 1]})
>>> print (frame)
   a  b
0  0  4
1  1  7
2  0 -3
3  1  2
>>> print (frame.sort_values(by = 'b')) # sort_index(by = ...)已淘汰
   a  b
2  0 -3
3  1  2
0  0  4
1  1  7
>>> print (frame.sort_values(by = ['a', 'b']))
   a  b
2  0 -3
0  0  4
3  1  2
1  1  7
```
```
>>> print ('rank，求排名的平均位置(从1开始)')
rank，求排名的平均位置(从1开始)
>>> obj = Series([7, -5, 7, 4, 2, 0, 4])
>>> # 对应排名：-5(1), 0(2), 2(3), 4(4), 4(5), 7(6), 7(7)
... print (obj.rank())
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64
>>> print (obj.rank(method = 'first'))  # 去第一次出现，不求平均值。
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64
>>> print (obj.rank(ascending = False, method = 'max')) # 逆序，并取最大 值。所以-5的rank是7.
0    2.0
1    7.0
2    2.0
3    4.0
4    5.0
5    6.0
6    4.0
dtype: float64
>>> frame = DataFrame({'b':[4.3, 7, -3, 2],
...                   'a':[0, 1, 0, 1],
...                   'c':[-2, 5, 8, -2.5]})
>>> print (frame)
   a    b    c
0  0  4.3 -2.0
1  1  7.0  5.0
2  0 -3.0  8.0
3  1  2.0 -2.5
>>> print (frame.rank(axis = 1))
     a    b    c
0  2.0  3.0  1.0
1  1.0  3.0  2.0
2  2.0  1.0  3.0
3  2.0  3.0  1.0
```
####2.7 带有重复值的索引
```
>>> print ('重复的索引')
重复的索引
>>> obj = Series(range(5), index = ['a', 'a', 'b', 'b', 'c'])
>>> print (obj.index.is_unique) # 判断是非有重复索引
False
>>> df = DataFrame(np.random.randn(4, 3), index = ['a', 'a', 'b', 'b'])
>>> print (df)
          0         1         2
a -0.819338  0.518905 -0.861562
a  0.573467  1.027358 -0.902153
b  0.990493 -1.257021 -0.687425
b  1.199946 -0.240610 -0.898948
>>> print (df.ix['b'].ix[0])
0    0.990493
1   -1.257021
2   -0.687425
Name: b, dtype: float64
>>> print (df.ix['b'].ix[1])
0    1.199946
1   -0.240610
2   -0.898948
Name: b, dtype: float64
```
### 汇总和计算描述统计
- 常用方法选项 

![image.png](http://upload-images.jianshu.io/upload_images/6634703-48c884fd8dfafdd8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 常用描述和汇总统计函数  I 

![image.png](http://upload-images.jianshu.io/upload_images/6634703-bf895c7b8c3f1198.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](http://upload-images.jianshu.io/upload_images/6634703-1147d8569b7eb4f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('求和')
求和
>>> df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
...               index = ['a', 'b', 'c', 'd'],
...               columns = ['one', 'two'])
>>> print (df)
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3
>>> print (df.sum())  # 按列求和
one    9.25
two   -5.80
dtype: float64
>>> print (df.sum(axis = 1))  # 按行求和
a    1.40
b    2.60
c     NaN
d   -0.55
dtype: float64
```
```
>>> print ('平均数')
平均数
>>> print (df.mean(axis = 1, skipna = False))
a      NaN
b    1.300
c      NaN
d   -0.275
dtype: float64
>>> print (df.mean(axis = 1))
a    1.400
b    1.300
c      NaN
d   -0.275
dtype: float64
```
```
>>> print ('其它')
其它
>>> print (df.idxmax())
one    b
two    d
dtype: object
>>> print (df.cumsum())
    one  two
a  1.40  NaN
b  8.50 -4.5
c   NaN  NaN
d  9.25 -5.8
>>> print (df.describe())
            one       two
count  3.000000  2.000000
mean   3.083333 -2.900000
std    3.493685  2.262742
min    0.750000 -4.500000
25%    1.075000 -3.700000
50%    1.400000 -2.900000
75%    4.250000 -2.100000
max    7.100000 -1.300000
>>> obj = Series(['a', 'a', 'b', 'c'] * 4)
>>> print (obj.describe())
count     16
unique     3
top        a
freq       8
dtype: object
```
####3.1 相关系数与协方差
- 相关系数：相关系数是用以反映变量之间相关关系密切程度的统计指标
-  协方差：从直观上来看，协方差表示的是两个变量总体误差的期望。如果两个 变量的变化趋势一致，也就是说如果其中一个大于自身的期望值时另外一个也 大于自身的期望值，那么两个变量之间的协方差就是正值；如果两个变量的变 化趋势相反，即其中一个变量大于自身的期望值时另外一个却小于自身的期望 值，那么两个变量之间的协方差就是负值
```
# 这一段代码不能翻墙的话读不了
import numpy as np
import pandas_datareader.data as web
from pandas import DataFrame

print ('相关性与协方差')  # 协方差：https://zh.wikipedia.org/wiki/%E5%8D%8F%E6%96%B9%E5%B7%AE)
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '4/1/2016', '7/15/2015')
    price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
    volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
returns = price.pct_change()
print (returns.tail())
print (returns.MSFT.corr(returns.IBM))
print (returns.corr())  # 相关性，自己和自己的相关性总是1
print (returns.cov()) # 协方差
print (returns.corrwith(returns.IBM))
print (returns.corrwith(returns.volume))
```
####3.2 唯一值以及成员资格
- 常用方法

![image.png](http://upload-images.jianshu.io/upload_images/6634703-ab348ae5247ff10b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
>>> print ('去重')
去重
>>> obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
>>> print (obj.unique())
['c' 'a' 'd' 'b']
>>> print (obj.value_counts())
c    3
a    3
b    2
d    1
dtype: int64
```
```
>>> print ('判断元素存在')
判断元素存在
>>> mask = obj.isin(['b', 'c'])
>>> print (mask)
0     True
1    False
2    False
3    False
4    False
5     True
6     True
7     True
8     True
dtype: bool
>>> print (obj[mask]) #只打印元素b和c
0    c
5    b
6    b
7    c
8    c
dtype: object
>>> data = DataFrame({'Qu1':[1, 3, 4, 3, 4],
...                   'Qu2':[2, 3, 1, 2, 3],
...                   'Qu3':[1, 5, 2, 4, 4]})
>>> print (data)
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    4    3    4
>>> print (data.apply(pd.value_counts).fillna(0))
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0
>>> print (data.apply(pd.value_counts, axis = 1).fillna(0))
     1    2    3    4    5
0  2.0  1.0  0.0  0.0  0.0
1  0.0  0.0  2.0  0.0  1.0
2  1.0  1.0  0.0  1.0  0.0
3  0.0  1.0  1.0  1.0  0.0
4  0.0  0.0  1.0  2.0  0.0
```
###4. 处理缺失数据
####4.1 NA处理方法
- NaN（Not a Number）表示浮点数和非浮点数组中的缺失数据 
- None也被当作NA处理 
![image.png](http://upload-images.jianshu.io/upload_images/6634703-4ce10372f72b749a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
>>> import numpy as np
>>> from pandas import Series
>>>
>>> print ('作为null处理的值')
作为null处理的值
>>> string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
>>> print (string_data)
0     aardvark
1    artichoke
2          NaN
3      avocado
dtype: object
>>> print (string_data.isnull())
0    False
1    False
2     True
3    False
dtype: bool
>>> string_data[0] = None
>>> print (string_data.isnull())
0     True
1    False
2     True
3    False
dtype: bool
```
####4.2 滤除缺失数据
```
>>> import numpy as np
>>> from numpy import nan as NA
>>> from pandas import Series, DataFrame
>>>
>>> print ('丢弃NA')
丢弃NA
>>> data = Series([1, NA, 3.5, NA, 7])
>>> print (data.dropna())
0    1.0
2    3.5
4    7.0
dtype: float64
>>> print (data[data.notnull()])
0    1.0
2    3.5
4    7.0
dtype: float64
```
```
>>> print ('DataFrame对丢弃NA的处理')
DataFrame对丢弃NA的处理
>>> data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
...                   [NA, NA, NA], [NA, 6.5, 3.]])
>>> print (data.dropna()) # 默认只要某行有NA就全部删除
     0    1    2
0  1.0  6.5  3.0
>>> print (data.dropna(how = 'all'))  # 全部为NA才删除
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
3  NaN  6.5  3.0
>>> data[4] = NA  # 新增一列
>>> print (data.dropna(axis = 1, how = 'all'))
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0
>>> data = DataFrame(np.random.randn(7, 3))
>>> data.ix[:4, 1] = NA
>>> data.ix[:2, 2] = NA
>>> print (data)
          0         1         2
0 -0.286526       NaN       NaN
1  0.739128       NaN       NaN
2 -1.813093       NaN       NaN
3 -0.030338       NaN -1.822855
4 -0.580589       NaN  1.189702
5 -1.292924  0.109001  1.036571
6 -0.510740  0.857497 -0.126522
>>> print (data.dropna(thresh = 2)) # 每行至少要有2个非NA元素
          0         1         2
3 -0.030338       NaN -1.822855
4 -0.580589       NaN  1.189702
5 -1.292924  0.109001  1.036571
6 -0.510740  0.857497 -0.126522
```
####4.3 填充缺失数据
```
>>> import numpy as np
>>> from numpy import nan as NA
>>> import pandas as pd
>>> from pandas import Series, DataFrame, Index
>>>
>>> print ('填充0')
填充0
>>> df = DataFrame(np.random.randn(7, 3))
>>> df.ix[:4, 1] = NA
>>> df.ix[:2, 2] = NA
>>> print (df.fillna(0))
          0         1         2
0 -0.906578  0.000000  0.000000
1  0.071408  0.000000  0.000000
2  0.026809  0.000000  0.000000
3 -1.800546  0.000000  0.432918
4 -1.568870  0.000000  0.409149
5  1.313441  0.948818 -0.035420
6  0.829020  1.023328  0.274207
>>> df.fillna(0, inplace = True)
>>> print (df)
          0         1         2
0 -0.906578  0.000000  0.000000
1  0.071408  0.000000  0.000000
2  0.026809  0.000000  0.000000
3 -1.800546  0.000000  0.432918
4 -1.568870  0.000000  0.409149
5  1.313441  0.948818 -0.035420
6  0.829020  1.023328  0.274207
```
```
>>> print ('不同行列填充不同的值')
不同行列填充不同的值
>>> print (df.fillna({1:0.5, 3:-1}))  # 第3列不存在
          0         1         2
0 -0.906578  0.000000  0.000000
1  0.071408  0.000000  0.000000
2  0.026809  0.000000  0.000000
3 -1.800546  0.000000  0.432918
4 -1.568870  0.000000  0.409149
5  1.313441  0.948818 -0.035420
6  0.829020  1.023328  0.274207
```
```
>>> print ('不同的填充方式')
不同的填充方式
>>> df = DataFrame(np.random.randn(6, 3))
>>> df.ix[2:, 1] = NA
>>> df.ix[4:, 2] = NA
>>> print (df)
          0         1         2
0  1.260661 -0.195192 -1.566377
1 -0.280009 -0.926795 -1.772026
2 -0.269668       NaN -1.223589
3 -1.829935       NaN -0.860152
4 -0.562236       NaN       NaN
5  2.009366       NaN       NaN
>>> print (df.fillna(method = 'ffill'))
          0         1         2
0  1.260661 -0.195192 -1.566377
1 -0.280009 -0.926795 -1.772026
2 -0.269668 -0.926795 -1.223589
3 -1.829935 -0.926795 -0.860152
4 -0.562236 -0.926795 -0.860152
5  2.009366 -0.926795 -0.860152
>>> print (df.fillna(method = 'ffill', limit = 2))
          0         1         2
0  1.260661 -0.195192 -1.566377
1 -0.280009 -0.926795 -1.772026
2 -0.269668 -0.926795 -1.223589
3 -1.829935 -0.926795 -0.860152
4 -0.562236       NaN -0.860152
5  2.009366       NaN -0.860152
```
```
>>> print ('用统计数据填充')
用统计数据填充
>>> data = Series([1., NA, 3.5, NA, 7])
>>> print (data.fillna(data.mean()))
0    1.000000
1    3.833333
2    3.500000
3    3.833333
4    7.000000
dtype: float64
```
###5. 层次化索引
- 使你能在一个轴上拥有多个（两个以上）索引级别。抽象的说，它使你能以低 纬度形式处理高维度数据。 
```
>>> import numpy as np
>>> from pandas import Series, DataFrame, MultiIndex
>>>
>>> print ('Series的层次索引')
Series的层次索引
>>> data = Series(np.random.randn(10),
...               index = [['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
...                        [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
>>> print (data)
a  1   -0.120844
   2   -0.165075
   3    0.819057
b  1   -1.853474
   2   -1.412147
   3    1.399640
c  1    1.398124
   2   -0.129620
d  2    1.042479
   3   -1.025431
dtype: float64
>>> print (data.index)
MultiIndex(levels=[['a', 'b', 'c', 'd'], [1, 2, 3]],
           labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])
>>> print (data.b)
1   -1.853474
2   -1.412147
3    1.399640
dtype: float64
>>> print (data['b':'c'])
b  1   -1.853474
   2   -1.412147
   3    1.399640
c  1    1.398124
   2   -0.129620
dtype: float64
>>> print (data[:2])
a  1   -0.120844
   2   -0.165075
dtype: float64
>>> print (data.unstack())
          1         2         3
a -0.120844 -0.165075  0.819057
b -1.853474 -1.412147  1.399640
c  1.398124 -0.129620       NaN
d       NaN  1.042479 -1.025431
>>> print (data.unstack().stack())
a  1   -0.120844
   2   -0.165075
   3    0.819057
b  1   -1.853474
   2   -1.412147
   3    1.399640
c  1    1.398124
   2   -0.129620
d  2    1.042479
   3   -1.025431
dtype: float64
```
```
>>> print ('DataFrame的层次索引')
DataFrame的层次索引
>>> frame = DataFrame(np.arange(12).reshape((4, 3)),
...                   index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
...                   columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
>>> print (frame)
     Ohio     Colorado
    Green Red    Green
a 1     0   1        2
  2     3   4        5
b 1     6   7        8
  2     9  10       11
>>> frame.index.names = ['key1', 'key2']
>>> frame.columns.names = ['state', 'color']
>>> print (frame)
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
>>> print (frame.ix['a', 1])
state     color
Ohio      Green    0
          Red      1
Colorado  Green    2
Name: (a, 1), dtype: int32
>>> print (frame.ix['a', 2]['Colorado'])
color
Green    5
Name: (a, 2), dtype: int32
>>> print (frame.ix['a', 2]['Ohio']['Red'])
4
```
```
>>> print ('直接用MultiIndex创建层次索引结构')
直接用MultiIndex创建层次索引结构
>>> print (MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Gree', 'Red', 'Green']],
...                              names = ['state', 'color']))
MultiIndex(levels=[['Colorado', 'Ohio'], ['Gree', 'Green', 'Red']],
           labels=[[1, 1, 0], [0, 2, 1]],
           names=['state', 'color'])
```
####5.1  重新分级顺序
```
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>>
>>> print ('索引层级交换')
索引层级交换
>>> frame = DataFrame(np.arange(12).reshape((4, 3)),
...                   index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
...                   columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
>>> frame.index.names = ['key1', 'key2']
>>> frame_swapped = frame.swaplevel('key1', 'key2')
>>> print (frame_swapped)
           Ohio     Colorado
          Green Red    Green
key2 key1
1    a        0   1        2
2    a        3   4        5
1    b        6   7        8
2    b        9  10       11
>>> print (frame_swapped.swaplevel(0, 1))
           Ohio     Colorado
          Green Red    Green
key1 key2
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
```
```
>>> print ('根据索引排序')
根据索引排序
>>> print (frame.sortlevel('key2'))
__main__:1: FutureWarning: sortlevel is deprecated, use sort_index(level= ...)
           Ohio     Colorado
          Green Red    Green
key1 key2
a    1        0   1        2
b    1        6   7        8
a    2        3   4        5
b    2        9  10       11
>>> print (frame.swaplevel(0, 1).sortlevel(0))
           Ohio     Colorado
          Green Red    Green
key2 key1
1    a        0   1        2
     b        6   7        8
2    a        3   4        5
     b        9  10       11
```
####5.2 根据级别汇总统计
```
>>> import numpy as np
>>> from pandas import DataFrame
>>>
>>> print ('根据指定的key计算统计信息')
根据指定的key计算统计信息
>>> frame = DataFrame(np.arange(12).reshape((4, 3)),
...                   index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
...                   columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
>>> frame.index.names = ['key1', 'key2']
>>> print (frame)
           Ohio     Colorado
          Green Red    Green
key1 key2
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
>>> print (frame.sum(level = 'key2'))
      Ohio     Colorado
     Green Red    Green
key2
1        6   8       10
2       12  14       16
```
####5.3 使用DataFrame的列
```
>>> import numpy as np
>>> from pandas import DataFrame
>>>
>>> print ('使用列生成层次索引')
使用列生成层次索引
>>> frame = DataFrame({'a':range(7),
...                    'b':range(7, 0, -1),
...                    'c':['one', 'one', 'one', 'two', 'two', 'two', 'two'],
...                    'd':[0, 1, 2, 0, 1, 2, 3]})
>>> print (frame)
   a  b    c  d
0  0  7  one  0
1  1  6  one  1
2  2  5  one  2
3  3  4  two  0
4  4  3  two  1
5  5  2  two  2
6  6  1  two  3
>>> print (frame.set_index(['c', 'd']))  # 把c/d列变成索引
       a  b
c   d
one 0  0  7
    1  1  6
    2  2  5
two 0  3  4
    1  4  3
    2  5  2
    3  6  1
>>> print (frame.set_index(['c', 'd'], drop = False)) # 列依然保留
       a  b    c  d
c   d
one 0  0  7  one  0
    1  1  6  one  1
    2  2  5  one  2
two 0  3  4  two  0
    1  4  3  two  1
    2  5  2  two  2
    3  6  1  two  3
>>> frame2 = frame.set_index(['c', 'd'])
>>> print (frame2.reset_index())
     c  d  a  b
0  one  0  0  7
1  one  1  1  6
2  one  2  2  5
3  two  0  3  4
4  two  1  4  3
5  two  2  5  2
6  two  3  6  1
```
###6. 其他话题
####6.1 整数索引
```
>>> import numpy as np
>>> import sys
>>> from pandas import Series, DataFrame
>>>
>>> print ('整数索引')
整数索引
>>> ser = Series(np.arange(3.))
>>> print (ser)
0    0.0
1    1.0
2    2.0
dtype: float64
>>> try:
...     print (ser[-1]) # 这里会有歧义
... except:
...     print (sys.exc_info()[0])
... ser2 = Series(np.arange(3.), index = ['a', 'b', 'c'])
  File "<stdin>", line 5
    ser2 = Series(np.arange(3.), index = ['a', 'b', 'c'])
       ^
SyntaxError: invalid syntax
>>> print (ser2[-1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ser2' is not defined
>>> ser3 = Series(range(3), index = [-5, 1, 3])
>>> print (ser3.iloc[2])  # 避免直接用[2]产生的歧义
2
```
```
>>> print ('对DataFrame使用整数索引')
对DataFrame使用整数索引
>>> frame = DataFrame(np.arange(6).reshape((3, 2)), index = [2, 0, 1])
>>> print (frame)
   0  1
2  0  1
0  2  3
1  4  5
>>> print (frame.iloc[0])
0    0
1    1
Name: 2, dtype: int32
>>> print (frame.iloc[:, 1])
2    1
0    3
1    5
Name: 1, dtype: int32
```
