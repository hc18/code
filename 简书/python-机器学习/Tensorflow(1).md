####目录
>1. 初识
>2. fetch and feed
>3. 非线性模型

######1. 初识
- 矩阵相乘
```
import tensorflow as tf

# 创建一个一行两列的矩阵
m1 = tf.constant([[3,3]])
# 创建一个两行一列的矩阵
m2 = tf.constant([[2],[3]])
# 两个矩阵相成
product = tf.matmul(m1,m2)
# 调用sess 的run方法来执行矩阵乘法
with tf.Session() as sess:
    result = sess.run(product)
    print(result)

[[15]]
```
- 矩阵加减
```
import tensorflow as tf
# 创建一个变量
x = tf.Variable([1,2])
# 创建一个常量
a = tf.constant([3,3])
# 相减、相加
sub = tf.subtract(x,a)
add = tf.add(x,sub)

# 初始化变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(add))
    print(sess.run(sub))

[-1  1]
[-2 -1]
```
- 矩阵累加
```
# 创建一个变量初始化为0
state = tf.Variable(0,name='counter')
new_value = tf.add(state, 1)
# 赋值op
update = tf.assign(state, new_value)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for i in range(5):
        sess.run(update)
        print(sess.run(state))

0
1
2
3
4
5
```
######2. fetch and feed
- fetch: 运行多个op
```
import tensorflow as tf
input1= tf.constant(3.0)
input2= tf.constant(2.0)
input3= tf.constant(5.0)

add = tf.add(input2,input3)
mul = tf.multiply(input1,add)

with tf.Session() as sess:
    result = sess.run([mul,add])
    print(result)

[21.0, 7.0]
```
- feed
```
input1= tf.placeholder(tf.float32)
input2= tf.placeholder(tf.float32)
output= tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[8.],input2:[2.]}))

[ 16.]
```
```
import tensorflow as tf
import numpy as np

# 使用numpy生成100个随机点
x_data = np.random.rand(100)
y_data = x_data*0.1 + 0.2

# 构造一个非线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b

# 二次代价函数
# reduce_mean , 取矩阵的平均数，起到降维的作用
loss = tf.reduce_mean(tf.square(y_data-y))

#定义一个梯度下降法来进行训练的优化器
#0.1 表示学习率，表示收敛的快慢
optimizer= tf.train.GradientDescentOptimizer(0.1)
#最小化代价函数
train = optimizer.minimize(loss)
#初始化变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step%50 ==0:
            print(step,sess.run([k,b]))

0 [0.053788777, 0.10022569]
50 [0.10169169, 0.19908892]
100 [0.10049076, 0.19973569]
150 [0.10014237, 0.19992332]
200 [0.10004131, 0.19997776]
```
######3 非线性模型
```

# coding: utf-8


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


#使用numpy生成200个随机点
# np.newaxis,加入新维度，每一个点作为一行
x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis]
noise = np.random.normal(0,0.02,x_data.shape)
y_data = np.square(x_data) + noise

#定义两个placeholder
x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])

#定义神经网络中间层
#1 代表输入值，10 代表10个神经元
Weights_L1 = tf.Variable(tf.random_normal([1,10]))
biases_L1 = tf.Variable(tf.zeros([1,10]))
# 信号总和
Wx_plus_b_L1 = tf.matmul(x,Weights_L1) + biases_L1
# tanh双曲正切函数：将实数映射到[-1,1] 
L1 = tf.nn.tanh(Wx_plus_b_L1)

#定义神经网络输出层
#10 代表10个神经元，1 代表1个输出层
Weights_L2 = tf.Variable(tf.random_normal([10,1]))
biases_L2 = tf.Variable(tf.zeros([1,1]))
Wx_plus_b_L2 = tf.matmul(L1,Weights_L2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2)

#二次代价函数
loss = tf.reduce_mean(tf.square(y-prediction))
#使用梯度下降法训练
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
    #变量初始化
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})
        
    #获得预测值
    prediction_value = sess.run(prediction,feed_dict={x:x_data})
    #画图
    plt.figure()
    plt.scatter(x_data,y_data)
    # 'r-' 红色实线，lw 线宽为5
    plt.plot(x_data,prediction_value,'r-',lw=5)
    plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-46d74c40550e0f6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
