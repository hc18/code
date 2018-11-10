####1. 多项式
![image.png](https://upload-images.jianshu.io/upload_images/6634703-10d6b5337adf9620.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
import sympy as sp
x = sp.Symbol('x')
# 返回积分函数
print(sp.integrate(3.0*x**2 + 1,x))

# 返回积分值
from scipy.integrate import quad
def f(x):
    return 3.0*x**2 + 1
i=quad(f,0,2)
print(i)
```
```
1.0*x**3 + 1.0*x
(10.000000000000002, 1.1102230246251568e-13) # 第二项是误差，可忽略，取i[0]即可
```
####2. 复合函数
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1778fbcb233fde52.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import sympy as sp
x = sp.Symbol('x')
# 返回积分函数
print(sp.integrate(sp.sin(3.0*x),x))

# 返回积分值
from scipy.integrate import quad
import numpy as np
def f(x):
    return np.exp(-x)* np.sin(3.0*x)
i=quad(f,0,2)
print(i)
```
```
-0.333333333333333*cos(3.0*x)
(0.26479800224918304, 6.070902242420391e-15)
```
####3. 查看图像
wolframalpha.com
![image.png](https://upload-images.jianshu.io/upload_images/6634703-86ef07950d6181d6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
