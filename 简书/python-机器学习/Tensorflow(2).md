>MNIST分类简单版本
1. MNIST数据集的官网:[Yann LeCun's MNIST](http://yann.lecun.com/exdb/mnist/)
2. 下载下来的数据集被分成两部分:60000行的训练数据集(mnist.train)和10000行的测试数据
集(mnist.test)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f6927fad28c7ebe5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-de972de7aea98ca5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-291a2fcab1958000.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![构建神经网络](https://upload-images.jianshu.io/upload_images/6634703-fa2f280f7c8c8ab1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/200)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-30af0c2a5a0ed9bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```

# coding: utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#载入数据集
# one_hot 把标签转换为0和1
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

#每个批次的大小，一次性放入100张图片进行训练，以矩阵的形式
batch_size = 100
#计算一共有多少个批次
n_batch = mnist.train.num_examples // batch_size

#定义两个placeholder，None代表任意的值，784=28*28。
x = tf.placeholder(tf.float32,[None,784])
#0-9 共10个数字
y = tf.placeholder(tf.float32,[None,10])

#创建一个简单的神经网络
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
# 把输出的信号转换成概率值
prediction = tf.nn.softmax(tf.matmul(x,W)+b)

#二次代价函数
loss = tf.reduce_mean(tf.square(y-prediction))
#使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#初始化变量
init = tf.global_variables_initializer()

#结果存放在一个布尔型列表中
#比较这两个参数的大小是否一样（标签位置）
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))#argmax返回一维张量中最大的值所在的位置
#求准确率，cast 把 ture变成1，false变成0
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(init)
    # 把所有图片训练20次
    for epoch in range(20):
        for batch in range(n_batch):
            # batch_xs 图片数据，batch_ys 图片标签
            batch_xs,batch_ys =  mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})
        #训练一次后，查看准确率
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("Iter " + str(epoch) + ",Testing Accuracy " + str(acc))


Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
Iter 0,Testing Accuracy 0.8325
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


