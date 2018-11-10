##目录
####1. 数组创建函数
####2. 数据运算
####3. 索引和切片
####4. 数组转置和轴对换
####5. 函数
###NumPy 安装与简介
- NumPy是Python语言的一个扩充程序库。支持高级大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
- 官网链接：[http://www.numpy.org/](http://www.numpy.org/)
```javascript
pip3 install Numpy  #(安装了python3)
conda install Numpy #(安装了Anaconda)
brew install Numpy #(mac) 
```
###1. 数组创建函数

![image.png](http://upload-images.jianshu.io/upload_images/6634703-f79f65dc0d3c3942.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
# -*- coding: utf-8 -*-
import numpy as np
print ('使用普通一维数组生成NumPy一维数组')
data = [6, 7.5, 8, 0, 1]
arr = np.array(data)
print (arr)                         
print ('打印元素类型')
print (arr.dtype)               
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-a1bbc8185fa9b1ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
print ('使用普通二维数组生成NumPy二维数组')
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data)
print (arr)
print ('打印数组维度')
print (arr.shape)  #(2,4) 两行四列
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-2c8642149066b1a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
print ('使用zeros/empty')
print (np.zeros(5)) # 生成包含5个0的一维数组
print (np.zeros((3, 2))) # 生成3*2的二维数组
print ('使用arrange生成连续元素')
print (np.arange(15))  # [0, 1, 2, ..., 14]
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-2d101a17431e9352.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###2. 数据运算
```javascript
# -*- coding: utf-8 -*-
import numpy as np
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print (arr * arr)
print (arr - arr)
# 标量操作作用在数组的每个元素上
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print (1 / arr)
print (arr ** 0.5)  # 开根号
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-031c07d6aeb7fdcd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###3. 索引和切片
```javascript
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (arr[2])
print (arr[0][2])
print (arr[0, 2])
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-e27efa79c84a3ba2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print (arr[0])
print (arr[1][0])
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-3a29f41b9b6fd90a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
old_values = arr[0].copy()  # 复制arr[0]的值
arr[0] = 42 # 把arr[0]所有的元素都设置为同一个值
print (arr)
arr[0] = old_values # 把原来的数组写回去
print (arr)
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-80f8300d187a10f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (arr)
print (arr[:2]) # 打印第1、2行
print (arr[:2, 1:]) # 打印第1、2行，第2、3列
print (arr[:, :1])  # 打印第一列的所有元素
arr[:2, 1:] = 0 # 第1、2行，第2、3列的元素设置为0
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-442d2df9c246661b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
print ('使用布尔数组作为索引')
name_arr = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print (name_arr == 'Bob')
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-c4444101ada11635.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 花式索引（Fancy indexing）: 利用整数数组进行索引
```javascript
import numpy as np
print ('Fancy Indexing: 使用整数数组作为索引')
arr = np.arange(32).reshape((8, 4))  # 通过reshape变换成二维数组
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-d3e154de27682617.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
print (arr[[4, 3, 0, 6]]) # 打印arr[4]、arr[3]、arr[0]和arr[6]。
print (arr[[1, 5, 7, 2], [0, 3, 1, 2]]) # 打印arr[1, 0]、arr[5, 3]，arr[7, 1]和arr[2, 2]
print (arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])  # 1572行的0312列,列的顺序也重排了
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-dad829d4569c785b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###4. 数组转置和轴对换
```javascript
# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as np_random
print ('转置矩阵')
arr = (np.arange(15).reshape((3, 5)))
print (arr)
print (arr.T)
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-b96c5f5c2c1a6530.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
print ('转置矩阵做点积')
arr = np_random.randn(6, 3)
print (np.dot(arr.T, arr))
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-45256d14c1d468f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###5. 函数
- 一元函数

![image.png](http://upload-images.jianshu.io/upload_images/6634703-35f7dcd37b0ae0dd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](http://upload-images.jianshu.io/upload_images/6634703-ea9b891d002a1977.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 二元函数

![image.png](http://upload-images.jianshu.io/upload_images/6634703-6a658385527c7e5b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](http://upload-images.jianshu.io/upload_images/6634703-e014a0cd4893d5d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as np_random
print ('求平方根')
arr = np.arange(10)
print(np.sqrt(arr))
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-2b6002880c452291.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
print ('数组比较')
x = np_random.randn(6)
y = np_random.randn(6)
print (x)
print (y)
print (np.maximum(x, y))
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-40d708a18082432c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
print ('使用modf函数把浮点数分解成整数和小数部分')
arr =[1.2,2.5,3.6]  
print (np.modf(arr))
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-c2070203671c86ba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
