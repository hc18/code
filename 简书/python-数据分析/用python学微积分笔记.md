####1. 函数
######1.1 多项式(polynomials)：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a07f121191e73275.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
 def f(x):
        return x**3 - 5*x**2 + 9

import numpy as np
x = np.linspace(-5, 5, num = 100)
y = f(x)
import matplotlib.pyplot as plt
plt.plot(x,y)
```
######2.1 指数函数(Exponential Functions):
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dbcb7b31fadd5a93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 方法一
```
def exp(x):
        return np.e**x
```
- 方法二
![image.png](https://upload-images.jianshu.io/upload_images/6634703-45a525e279e9cd92.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
def exp2(x):
        sum = 0
        for k in range(100):
            sum += float(x**k)/np.math.factorial(k)
        return sum
```
######3.1 对数函数(Logarithmic Functions):
![image.png](https://upload-images.jianshu.io/upload_images/6634703-4ea1cc888efda9bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
x = np.linspace(0,10,100,endpoint = False)
y1 = np.log2(x)
y2 = np.log(x)
y3 = np.log10(x)
plt.plot(x,y1,'red',x,y2,'yellow',x,y3,'blue')
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a91858e8f3a232f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. 复合函数
######2.1 函数的复合（Composition）:
![image.png](https://upload-images.jianshu.io/upload_images/6634703-09d85744c33eca82.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import numpy as np
import matplotlib.pyplot as plt
def f(x): return x+1
def g(x): return x**2
def h(x): return f(g(x))
x = np.array(range(-10,10))
# 这里我们使用了Python的list comprehension来计算y
y = np.array([h(i) for i in x])
# 'bo' 将表示我们会使用蓝色的圆圈绘制点图，而非默认的线图
plt.plot(x, y, 'bo')
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a3474ee9dc39324f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import numpy as np
import matplotlib.pyplot as plt
def f(x): return x+1

def g(x): return x**2

x = np.array(range(-10,10))
h2 = lambda x: f(g(x))
plt.plot(x,h2(x),'rs')


plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6bc2800d9519f2ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######2.2 逆函数
![image.png](https://upload-images.jianshu.io/upload_images/6634703-71c3f1fcc7561d92.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import numpy as np
import matplotlib.pyplot as plt
import math
w = lambda x: x**2
winv = lambda x: np.sqrt(x)
x = np.linspace(0,2,100)
plt.plot(x, w(x),'b',x,winv(x),'r',x,x,'g-.')
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-79a371defe3168ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######2.3 高阶函数（Higher Order Functions）:
- 我们可以不局限于仅将数值作为函数的输入输出，函数本身也可以作为输入和输出。
```
def g(x): 
	return x**2

def horizontal_shift(f,H): 
	return lambda x: f(x-H)

x = np.linspace(-10,10,100)
shifted_g = horizontal_shift(g,2)
plt.plot(x,g(x),'b',x,shifted_g(x),'r')
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-aa51d36ab1024539.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. 欧拉公式（Euler's Formula）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-cf409c8a1fe97daf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
