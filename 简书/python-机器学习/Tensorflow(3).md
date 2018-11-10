>[优化MNIST分类简单版本](https://www.jianshu.com/p/2862b01abf9d)
>1. 二次代价函数VS交叉商代价函数
>2. 防止过拟合

######1.  二次代价函数 VS 交叉商代价函数
######1.1 二次代价函数
![ 二次代价函数](https://upload-images.jianshu.io/upload_images/6634703-4b632f744d88aaeb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![二次代价函数](https://upload-images.jianshu.io/upload_images/6634703-288ed0baa3c6d330.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![二次代价函数](https://upload-images.jianshu.io/upload_images/6634703-24b01202fb9f7fd6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>1. 假设目标收敛到1，A离目标比较远，梯度大，权值调整大，收敛比B快，所以调整方案**合理**
>2. 假设目标收敛到0，B离目标比较远，梯度小，权值调整小，收敛比A慢，所以调整方案**不合理**
######1.2 交叉商代价函数（cross_entropy）
![交叉商代价函数](https://upload-images.jianshu.io/upload_images/6634703-6017ff55e71e69bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![交叉商代价函数](https://upload-images.jianshu.io/upload_images/6634703-53489b127e7a1f61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 对数释然代价函数（留个标记）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f3ec615ffac8e1ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 把[优化MNIST分类简单版本](https://www.jianshu.com/p/2862b01abf9d)的代码替换一句话，
```
# 二次代价函数
# loss = tf.reduce_mean(tf.square(y-prediction))
# 交叉商代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))

Iter 0,Testing Accuracy 0.825
Iter 1,Testing Accuracy 0.8943
Iter 2,Testing Accuracy 0.901
Iter 3,Testing Accuracy 0.9057
Iter 4,Testing Accuracy 0.908
Iter 5,Testing Accuracy 0.9102
Iter 6,Testing Accuracy 0.9116
Iter 7,Testing Accuracy 0.9135
Iter 8,Testing Accuracy 0.9143
Iter 9,Testing Accuracy 0.9155
Iter 10,Testing Accuracy 0.9179
Iter 11,Testing Accuracy 0.9189
Iter 12,Testing Accuracy 0.9192
Iter 13,Testing Accuracy 0.9201
Iter 14,Testing Accuracy 0.9209
Iter 15,Testing Accuracy 0.9201
Iter 16,Testing Accuracy 0.9201
Iter 17,Testing Accuracy 0.9211
Iter 18,Testing Accuracy 0.9215
Iter 19,Testing Accuracy 0.9211
Iter 20,Testing Accuracy 0.9211
```
- 和下面的二次代价函数比较可以得到，交叉熵代价函数要比二次代价函数收敛的快
```
Iter 1,Testing Accuracy 0.8705
Iter 2,Testing Accuracy 0.8824
Iter 3,Testing Accuracy 0.8869
Iter 4,Testing Accuracy 0.8936
Iter 5,Testing Accuracy 0.8968
Iter 6,Testing Accuracy 0.9002
Iter 7,Testing Accuracy 0.9013
Iter 8,Testing Accuracy 0.9032
Iter 9,Testing Accuracy 0.9055
Iter 10,Testing Accuracy 0.9065
Iter 11,Testing Accuracy 0.9072
Iter 12,Testing Accuracy 0.9077
Iter 13,Testing Accuracy 0.9091
Iter 14,Testing Accuracy 0.9099
Iter 15,Testing Accuracy 0.9108
Iter 16,Testing Accuracy 0.9112
Iter 17,Testing Accuracy 0.9131
Iter 18,Testing Accuracy 0.9134
Iter 19,Testing Accuracy 0.9133
```
######2. 防止过拟合
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5bc566af78850d80.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f5a7f88d9da5d1a7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 防止过拟合的三个办法
![image.png](https://upload-images.jianshu.io/upload_images/6634703-834a6c752ffb980c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```

# coding: utf-8

# In[3]:

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#载入数据集
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

#每个批次的大小
batch_size = 100
#计算一共有多少个批次
n_batch = mnist.train.num_examples // batch_size

#定义两个placeholder
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])
keep_prob=tf.placeholder(tf.float32)

#创建一个简单的神经网络
# truncated_normal 截断正态分布要比初始值为0好
W1 = tf.Variable(tf.truncated_normal([784,2000],stddev=0.1))
b1 = tf.Variable(tf.zeros([2000])+0.1)
# L1 为第一层神经元的输出
L1 = tf.nn.tanh(tf.matmul(x,W1)+b1)
# keep_prob 设定有多少神经元是工作的，1 是100%，0.7是70%
L1_drop = tf.nn.dropout(L1,keep_prob) 

# 中间隐藏层，其实不需要这么多，为了等下过拟合做个比较
W2 = tf.Variable(tf.truncated_normal([2000,2000],stddev=0.1))
b2 = tf.Variable(tf.zeros([2000])+0.1)
L2 = tf.nn.tanh(tf.matmul(L1_drop,W2)+b2)
L2_drop = tf.nn.dropout(L2,keep_prob) 

W3 = tf.Variable(tf.truncated_normal([2000,1000],stddev=0.1))
b3 = tf.Variable(tf.zeros([1000])+0.1)
L3 = tf.nn.tanh(tf.matmul(L2_drop,W3)+b3)
L3_drop = tf.nn.dropout(L3,keep_prob) 

W4 = tf.Variable(tf.truncated_normal([1000,10],stddev=0.1))
b4 = tf.Variable(tf.zeros([10])+0.1)
prediction = tf.nn.softmax(tf.matmul(L3_drop,W4)+b4)

#二次代价函数
# loss = tf.reduce_mean(tf.square(y-prediction))
#交叉熵代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#初始化变量
init = tf.global_variables_initializer()

#结果存放在一个布尔型列表中
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))#argmax返回一维张量中最大的值所在的位置
#求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys =  mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:1.0})
        
        test_acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels,keep_prob:1.0})
        train_acc = sess.run(accuracy,feed_dict={x:mnist.train.images,y:mnist.train.labels,keep_prob:1.0})
        print("Iter " + str(epoch) + ",Testing Accuracy " + str(test_acc) +",Training Accuracy " + str(train_acc))

Iter 0,Testing Accuracy 0.9447,Training Accuracy 0.957964
Iter 1,Testing Accuracy 0.956,Training Accuracy 0.973982
Iter 2,Testing Accuracy 0.9639,Training Accuracy 0.981436
Iter 3,Testing Accuracy 0.9652,Training Accuracy 0.985691
Iter 4,Testing Accuracy 0.9662,Training Accuracy 0.987873
Iter 5,Testing Accuracy 0.9685,Training Accuracy 0.989109
Iter 6,Testing Accuracy 0.9682,Training Accuracy 0.990345
Iter 7,Testing Accuracy 0.968,Training Accuracy 0.991036
Iter 8,Testing Accuracy 0.9687,Training Accuracy 0.991655
Iter 9,Testing Accuracy 0.9704,Training Accuracy 0.992164
Iter 10,Testing Accuracy 0.9689,Training Accuracy 0.9926
Iter 11,Testing Accuracy 0.9702,Training Accuracy 0.992964
Iter 12,Testing Accuracy 0.9708,Training Accuracy 0.993291
Iter 13,Testing Accuracy 0.9709,Training Accuracy 0.993691
Iter 14,Testing Accuracy 0.9713,Training Accuracy 0.993945
Iter 15,Testing Accuracy 0.9708,Training Accuracy 0.994164
Iter 16,Testing Accuracy 0.9712,Training Accuracy 0.994364
Iter 17,Testing Accuracy 0.9709,Training Accuracy 0.994509
Iter 18,Testing Accuracy 0.9715,Training Accuracy 0.9948
Iter 19,Testing Accuracy 0.9723,Training Accuracy 0.994909
Iter 20,Testing Accuracy 0.9725,Training Accuracy 0.995055

```
 - 把dropout 1.0改成0.7 可以发现，用训练集来做测试，和测试集做测试的准确率相近，所以1.0存在过拟合的情况
- 使用dropout 虽然收敛变慢，但是他可以尽量避免过拟合。

```
把1.0 改成0.7
#sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:1.0
sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.7

Iter 0,Testing Accuracy 0.918,Training Accuracy 0.913455
Iter 1,Testing Accuracy 0.9314,Training Accuracy 0.928945
Iter 2,Testing Accuracy 0.9365,Training Accuracy 0.935145
Iter 3,Testing Accuracy 0.9385,Training Accuracy 0.9406
Iter 4,Testing Accuracy 0.9467,Training Accuracy 0.945218
Iter 5,Testing Accuracy 0.9473,Training Accuracy 0.949473
Iter 6,Testing Accuracy 0.9509,Training Accuracy 0.953127
Iter 7,Testing Accuracy 0.9525,Training Accuracy 0.955727
Iter 8,Testing Accuracy 0.9543,Training Accuracy 0.956818
Iter 9,Testing Accuracy 0.9548,Training Accuracy 0.958855
Iter 10,Testing Accuracy 0.9569,Training Accuracy 0.961
Iter 11,Testing Accuracy 0.957,Training Accuracy 0.9622
Iter 12,Testing Accuracy 0.958,Training Accuracy 0.963
Iter 13,Testing Accuracy 0.9607,Training Accuracy 0.964327
Iter 14,Testing Accuracy 0.9625,Training Accuracy 0.966436
Iter 15,Testing Accuracy 0.9621,Training Accuracy 0.9664
Iter 16,Testing Accuracy 0.9634,Training Accuracy 0.967764
Iter 17,Testing Accuracy 0.9634,Training Accuracy 0.968382
Iter 18,Testing Accuracy 0.9657,Training Accuracy 0.969218
Iter 19,Testing Accuracy 0.9651,Training Accuracy 0.970436
Iter 20,Testing Accuracy 0.9658,Training Accuracy 0.971345
```







