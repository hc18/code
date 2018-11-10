##1. 利用数组进行数据处理
```javascript
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pylab
points = np.arange(-5, 5, 0.01) # 生成100个点
xs, ys = np.meshgrid(points, points)  # xs, ys互为转置矩阵
print (xs)
print (ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print (z)
# 画图
plt.imshow(z, cmap = plt.cm.gray);
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
pylab.show() 
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-e67e0bca10df89fe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####1.1  将条件逻辑表述为数组运算
```javascript
import numpy as np
import numpy.random as np_random
print ('更多where的例子')
arr = np_random.randn(4, 4)
print (arr)

[[-0.24957277 -1.00358211 -0.73089612  0.2547624 ]
[ 0.37150224 -0.13316825 -0.60619815 -1.92511077]
[-0.42200075 -0.48937521 -1.25945836 -0.73708106]
[-0.52699294  1.2829272  0.5382728  -0.33665592]]

print (np.where(arr > 0, 2, -2))

[[-2 -2 -2  2]
[ 2 -2 -2 -2]
[-2 -2 -2 -2]
[-2  2  2 -2]]

print (np.where(arr > 0, 2, arr))

[[-0.24957277 -1.00358211 -0.73089612  2.        ]
[ 2.        -0.13316825 -0.60619815 -1.92511077]
```
```javascript
print ('where嵌套')
cond_1 = np.array([True, False, True, True, False])
cond_2 = np.array([False, True, False, True, False])
# 传统代码如下
result = []
for i in range(len(cond_1)):
    if cond_1[i] and cond_2[i]:
        result.append(0)
    elif cond_1[i]:
        result.append(1)
    elif cond_2[i]:
        result.append(2)
    else:
        result.append(3)
print (result)

[1, 2, 1, 0, 3]

# np版本代码
result = np.where(cond_1 & cond_2, 0, \
          np.where(cond_1, 1, np.where(cond_2, 2, 3)))
print (result)

[1 2 1 0 3]

```
####1.2 数学和统计方法

![image.png](http://upload-images.jianshu.io/upload_images/6634703-bd9ef5edf7fdedf1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```javascript
import numpy as np
import numpy.random as np_random
print ('求和，求平均')
arr = np.random.randn(5, 4)
print (arr)

[[ 0.91340516 -0.28913556 -0.70409556  0.79581511]
[ 0.03067817 -1.48720141 -0.12093709 -0.46505081]
[ 1.19378156 -1.6550555  1.66422768 -0.21638596]
[ 0.05186091 -0.26038421  1.10220866  0.15916608]
[ 1.27671635 -1.88666043  1.97051236  0.2858806 ]]

print (arr.mean())

0.117967306233

print (arr.sum())

2.35934612466

print (arr.mean(axis = 1))  # 对每一行的元素求平均

[ 0.17899729 -0.51062779  0.24664195  0.26321286  0.41161222]
print (arr.sum(0))  # 对每一列元素求和，axis可以省略。

[ 3.46644215 -5.57843711  3.91191605  0.55942504]
```
```javascript
'''
cumsum:
- 按列操作：a[i][j] += a[i - 1][j]
- 按行操作：a[i][j] *= a[i][j - 1]
cumprod:
- 按列操作：a[i][j] += a[i - 1][j]
- 按行操作：a[i][j] *= a[i][j - 1]
'''
print ('cunsum和cumprod函数演示')
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print (arr.cumsum(0))  # 累加

[[ 0  1  2]
[ 3  5  7]
[ 9 12 15]]

print (arr.cumprod(1)) # 累乘

[[  0  0  0]
[  3  12  60]
[  6  42 336]]
```
####1.3 布尔型数组的方法
```javascript
import numpy as np
import numpy.random as np_random
print ('对正数求和')
arr = np_random.randn(100)

47

print ((arr > 0).sum())
print ('对数组逻辑操作')
bools = np.array([False, False, True, False])
print (bools.any()) # 有一个为True则返回True

True

print (bools.all()) # 有一个为False则返回False

False
```
####1.4 排序
```javascript
import numpy.random as np_random
print ('一维数组排序')
arr = np_random.randn(5)
arr.sort()
print (arr)

[-0.95478899 -0.84025039 -0.81146653 -0.59203327 -0.08063988]

print ('二维数组排序')
arr = np_random.randn(3, 2)
print (arr)

[[ 0.22553826 -0.55803348]
[-1.26086564  0.52919879]
[-0.44668631 -0.53374782]]

arr.sort(1) # 对每一行元素做排序
print (arr)

[[-0.55803348  0.22553826]
[-1.26086564  0.52919879]
[-0.53374782 -0.44668631]]

```
####1.5 去重以及其它集合运算

![image.png](http://upload-images.jianshu.io/upload_images/6634703-d476437775747c49.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```javascript
import numpy as np
import numpy.random as np_random

print ('用unique函数去重')
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print (sorted(set(names)))  # 传统Python做法

['Bob', 'Joe', 'Will']

print (np.unique(names))

['Bob' 'Joe' 'Will']

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print (np.unique(ints))

[1 2 3 4]

print ('查找数组元素是否在另一数组')
values = np.array([6, 0, 0, 3, 2, 5, 6])
print (np.in1d(values, [2, 3, 6]))

[ True False False  True  True False  True]

```
####1.6 数组文件的输入输出
```
import numpy as np
print ('读取csv文件做为数组')
arr = np.loadtxt('array_ex.txt', delimiter = ',')
print (arr)

print ('数组文件读写')
arr = np.arange(10)
np.save('some_array', arr)
print (np.load('some_array.npy'))

print ('多个数组压缩存储')
np.savez('array_archive.npz', a = arr, b = arr)
arch = np.load('array_archive.npz')
print (arch['b'])
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-57ada4795b750719.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##2 线性代数
- 常用的numpy.linalg函数 I
![image.png](http://upload-images.jianshu.io/upload_images/6634703-dd86207afd54a3ca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-fe093aea0076b0d6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```javascript
# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as np_random
from numpy.linalg import inv, qr

print ('矩阵乘法')
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print (x.dot(y))

[[  28.  64.]
[  67.  181.]]

print (np.dot(x, np.ones(3)))

[  6.  15.]

```
```javascript
x = np_random.randn(5, 5)
print ('矩阵求逆')
mat = x.T.dot(x)
print (inv(mat))  # 矩阵求逆

[[ 1.56337148  2.0598732  0.71214902]
[ 2.0598732  3.70889345  1.32647939]
[ 0.71214902  1.32647939  0.67314987]]

print (mat.dot(inv(mat))) # 与逆矩阵相乘，得到单位矩阵。

[[  1.00000000e+00  -1.11022302e-16  -2.77555756e-17]
[  2.22044605e-16  1.00000000e+00  0.00000000e+00]
[ -4.44089210e-16  0.00000000e+00  1.00000000e+00]]

print ('矩阵消元')
print (mat)
q, r = qr(mat)
print (q)
print (r)
```
##3. 随机数生成
- numpy.random 函数

![image.png](http://upload-images.jianshu.io/upload_images/6634703-0142afba94db8924.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-23376233bdc27897.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```javascript
print ('正态分布随机数')
samples = np.random.normal(size=(4, 4))
print (samples)

print ('批量按正态分布生成0到1的随机数')
N = 10
print (np.random.normal(size = N))
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-50b30827e548ad26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##4. 高级应用 数组重塑
```javascript
import numpy as np

print ("将一维数组转换为二维数组")
arr = np.arange(8)
print (arr.reshape((4, 2)))

[[0 1]
[2 3]
[4 5]
[6 7]]

print (arr.reshape((4, 2)).reshape((2, 4))) # 支持链式操作

[[0 1 2 3]
[4 5 6 7]]

print ("维度大小自动推导")
arr = np.arange(15)
print (arr.reshape((5, -1)))

[[ 0  1  2]
[ 3  4  5]
[ 6  7  8]
[ 9 10 11]
[12 13 14]]

print ("获取维度信息并应用")
other_arr = np.ones((3, 5))
print (other_arr.shape)
print (arr.reshape(other_arr.shape))
(3, 5)
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]]

print ("高维数组拉平")
arr = np.arange(15).reshape((5, 3))
print (arr.ravel())

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
```
####4.1 数组的合并和拆分
- 数组连接函数

![image.png](http://upload-images.jianshu.io/upload_images/6634703-9c269e741dd3f36e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```javascript
# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as np_random

print ('连接两个二维数组')
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

print (np.concatenate([arr1, arr2], axis = 0))  # 按行连接

[[ 1  2  3]
[ 4  5  6]
[ 7  8  9]
[10 11 12]]

print (np.concatenate([arr1, arr2], axis = 1))  # 按列连接

[[ 1  2  3  7  8  9]
[ 4  5  6 10 11 12]]

# 所谓堆叠，参考叠盘子。。。连接的另一种表述
print ('垂直stack与水平stack')
print (np.vstack((arr1, arr2))) # 垂直堆叠

[[ 1  2  3]
[ 4  5  6]
[ 7  8  9]
[10 11 12]]

print (np.hstack((arr1, arr2))) # 水平堆叠

[[ 1  2  3  7  8  9]
[ 4  5  6 10 11 12]]

print ('拆分数组')
arr = np_random.randn(5, 5)
print (arr)

[[ 0.05528194 -1.40691043  1.25390116  0.01343898 -0.56362107]
[-0.67196856 -2.01689483  0.530919  -0.01049739 -0.08576697]
[-0.00469774  0.60896671  0.49864293 -1.16233372  1.09303811]
[-1.6787031  0.1201058  0.83891825 -0.97806989  1.01268929]
[ 0.23928598  0.50982453 -0.77814664  0.71755991 -0.66536248]]

print ('水平拆分')
first, second, third = np.split(arr, [1, 3], axis = 0)
print ('first')
print (first)

[[ 0.05528194 -1.40691043  1.25390116  0.01343898 -0.56362107]]

print ('second')
print (second)

[[-0.67196856 -2.01689483  0.530919  -0.01049739 -0.08576697]
[-0.00469774  0.60896671  0.49864293 -1.16233372  1.09303811]]

print ('third')
print (third)

[[-1.6787031  0.1201058  0.83891825 -0.97806989  1.01268929]
[ 0.23928598  0.50982453 -0.77814664  0.71755991 -0.66536248]]

print ('垂直拆分')
first, second, third = np.split(arr, [1, 3], axis = 1)
print ('first')
print (first)

[[ 0.05528194]
[-0.67196856]
[-0.00469774]
[-1.6787031 ]
[ 0.23928598]]

print ('second')
print (second)

[[-1.40691043  1.25390116]
[-2.01689483  0.530919  ]
[ 0.60896671  0.49864293]
[ 0.1201058  0.83891825]
[ 0.50982453 -0.77814664]]

print ('third')
print (third)

[[ 0.01343898 -0.56362107]
[-0.01049739 -0.08576697]
[-1.16233372  1.09303811]
[-0.97806989  1.01268929]
[ 0.71755991 -0.66536248]]

# 堆叠辅助类
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np_random.randn(3, 2)
print ('r_用于按行堆叠')

[[ 0.          1.        ]
[ 2.          3.        ]
[ 4.          5.        ]
[-0.1285436  1.78124128]
[-1.18281363 -0.5240686 ]
[ 0.14317738  1.4884177 ]]

print (np.r_[arr1, arr2])
print ('c_用于按列堆叠')
print (np.c_[np.r_[arr1, arr2], arr])

[[ 0.          1.          0.        ]
[ 2.          3.          1.        ]
[ 4.          5.          2.        ]
[-0.1285436  1.78124128  3.        ]
[-1.18281363 -0.5240686  4.        ]
[ 0.14317738  1.4884177  5.        ]]

print ('切片直接转为数组')
print (np.c_[1:6, -10:-5])

[[  1 -10]
[  2  -9]
[  3  -8]
[  4  -7]
[  5  -6]]

```
####4.2 元素的重复操作
```javascript
import numpy as np
import numpy.random as np_random

print ('Repeat: 按元素')
arr = np.arange(3)
print (arr.repeat(3))

[0 0 0 1 1 1 2 2 2]

print (arr.repeat([2, 3, 4])) # 3个元素，分别复制2, 3, 4次。长度要匹配！

[0 0 1 1 1 2 2 2 2]

print ('Repeat，指定轴')
arr = np_random.randn(2, 2)
print (arr)

[[-0.24003754  0.87388196]
[ 0.63967445  0.53702917]]

print (arr.repeat(2, axis = 0)) # 按行repeat

[[-0.24003754  0.87388196]
[-0.24003754  0.87388196]
[ 0.63967445  0.53702917]
[ 0.63967445  0.53702917]]

print (arr.repeat(2, axis = 1)) # 按列repeat

[[-0.24003754 -0.24003754  0.87388196  0.87388196]
[ 0.63967445  0.63967445  0.53702917  0.53702917]]

print (arr.repeat(2, axis = 0)) # 按行repeat

[[-0.24003754  0.87388196]
[-0.24003754  0.87388196]
[ 0.63967445  0.53702917]
[ 0.63967445  0.53702917]]

print ('Tile: 参考贴瓷砖')
print (np.tile(arr, 2))

[[-0.24003754  0.87388196 -0.24003754  0.87388196]
[ 0.63967445  0.53702917  0.63967445  0.53702917]]

print (np.tile(arr, (2, 3)))  # 指定每个轴的tile次数

[[-0.24003754  0.87388196 -0.24003754  0.87388196 -0.24003754  0.87388196]
[ 0.63967445  0.53702917  0.63967445  0.53702917  0.63967445  0.53702917]
[-0.24003754  0.87388196 -0.24003754  0.87388196 -0.24003754  0.87388196]
[ 0.63967445  0.53702917  0.63967445  0.53702917  0.63967445  0.53702917]]
```
####4.3 花式索引的等价函数

```javascript
# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as np_random

print ('Fancy Indexing例子代码')
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print (arr[inds])

[700 100 200 600]

print ('使用take')
print (arr.take(inds))

[700 100 200 600]

print ('使用put更新内容')
arr.put(inds, 50)
print (arr)

[  0  50  50 300 400 500  50  50 800 900]
[  0  10  20 300 400 500  60  70 800 900]

arr.put(inds, [70, 10, 20, 60])
print (arr)

[[-0.93008115  0.61977807 -0.25993519 -1.09063511]
[ 0.73107853 -1.25725762  0.75042044  0.89568034]]

arr.put(inds, [70, 10, 20, 60])
print (arr)

[[-0.25993519 -0.93008115 -0.25993519  0.61977807]
[ 0.75042044  0.73107853  0.75042044 -1.25725762]]

```
