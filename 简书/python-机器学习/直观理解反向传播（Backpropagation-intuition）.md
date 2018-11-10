- 参数
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ab177f3286591575.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 对应网络如下
![image.png](https://upload-images.jianshu.io/upload_images/6634703-eeff9f78e7601f04.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 其中对应的矩阵表示如下
![image.png](https://upload-images.jianshu.io/upload_images/6634703-cb3d6a329342b0aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 首先我们先走一遍正向传播，公式与相应的数据对应如下：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-283a8ee98eb8b5fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-915da08604c20d70.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1b1531f6017ef30c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-195f9c97364edbcd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 我们希望损失函数越小越好，所以用了反向传播算法。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-12ae98399701a1d2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 这个时候我们需要求出C对w的偏导，则根据链式法则有：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-c4abfb4e82b2332b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 同理有：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-0326f730bdbc6fdb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 到此我们已经算出了最后一层的参数偏导了.我们继续往前面链式推导：
- 我们现在还需要求
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3eb516befaebef1f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 下面给出一个推导其它全都类似
![image.png](https://upload-images.jianshu.io/upload_images/6634703-572d29819098b434.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 同理可得其它几个式子：
- 则最终的结果为：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d9b881d066d8ad95.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-125053ee93da365b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####讲义
![image.png](https://upload-images.jianshu.io/upload_images/6634703-2c4a6d1319819924.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dd64e795d46e8a5c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e0cd58118336cea8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-65886310a74ec71e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####实战
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5a5abbbe500eef3a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import numpy as np


# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(10000):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)


Output After Training:
[[ 0.00966449]
 [ 0.00786506]
 [ 0.99358898]
 [ 0.99211957]]
```
