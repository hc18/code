>优化器
>1. tf.train.GradientDescentOptimizer 
>2. tf.train.AdadeltaOptimizer 
>3. tf.train.AdagradOptimizer 
>4. tf.train.AdagradDAOptimizer 
>5. tf.train.MomentumOptimizer 
>6. tf.train.AdamOptimizer 
>7. tf.train.FtrlOptimizer 
>8. tf.train.ProximalGradientDescentOptimizer 
>9. tf.train.ProximalAdagradOptimizer 
>10. tf.train.RMSPropOptimizer

###### 1. 各种优化器对比
- 标准梯度下降法:（速度慢）
标准梯度下降先计算所有样本汇总误差，然后根据总误差来更新权值
- 随机梯度下降法: （引入比较多的噪声，权值方向不一定正确）
随机梯度下降随机抽取一个样本来计算误差，然后更新权值
- 批量梯度下降法:
批量梯度下降算是一种折中的方案，从总样本中选取一个批次(比如一共有10000个样本，随 机选取100个样本作为一个batch)，然后计算这个batch的总误差，根据总误差来更新权值。
######2.  随机梯度下降法
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5d5f84a68b120323.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
`SGD: W = W−η⋅∇WJ(W;x(i);y(i))`
- W:要训练的参数 
- J(W):代价函数 
- ∇WJ(W):代价函数的梯度 
- η:学习率
######3. Momentum（训练速度非常快）
γ:动力，通常设置为0.9
`vt = γvt-1 + η∇WJ(W)`
`W = W−vt` 
当前权值的改变会受到上一次权值改变的影响，类似于小球向下滚动的时候带上了惯性。这样可以加快小球的向下的速度。
######4. NAG(Nesterov accelerated gradient):
vt = γvt-1 + η∇WJ(W−γvt 1) 
W = W−vt
NAG在TF中跟Momentum合并在同一个函数tf.train.MomentumOptimizer中，可以通过参数配置启用。 
在Momentun中小球会盲目地跟从下坡的梯度，容易发生错误,所以我们需要一个更聪明的小球，这个小球提前知道它要去哪里，它还要知道走到坡底的时候速度慢下来而不是又冲上另 一个坡。γvt−1会用来修改W的值，计算W−γvt−1可以表示小球下一个位置大概在哪里。从 而我们可以提前计算下一个位置的梯度，然后使用到当前位置。
######5 Adagrad:
i:代表第i个分类
t:代表出现次数
ε:的作用是避免分母为0，取值一般为1e-8
η:取值一般为0.01 
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ea260037539a54da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

它是基于SGD的一种算法，它的核心思想是**对比较常见的数据给予它比较小的学习率去调整参数，对于比较罕见的数据给予它比较大的学习率**去调整参数。它很适合应用于数据稀疏的数据集(比如一个图片数据集，有10000张狗的照片，10000张猫的照片，只有100张大象的照片)。 Adagrad主要的优势在于不需要人为的调节学习率，它可以自动调节。它的缺点在于，随着迭代次数的增多，学习率也会越来越低，最终会趋向于0。
######6.RMSprop
RMS(Root Mean Square)是均方根的缩写。
 γ:动力，通常设置为0.9
η:取值一般为0.001
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1a181dd7791cd3b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
RMSprop借鉴了一些Adagrad的思想，不过这里RMSprop只用到了前t-1次梯度平方的平均值加上当前梯度的平方的和的开平方作为学习率的分母。这样RMSprop不会出现学习率越来越低的问题，而且也能自己调节学习率，并且可以有一个比较好的效果。
######7. Adadelta
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6e37329f8d0c832e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
使用Adadelta我们甚至不需要设置一个默认学习率，在Adadelta不需要使用学习率也可以达 到一个非常好的效果。
######8. Adam
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6fb95d7ddd37f09d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
就像Adadelta和RMSprop一样Adam会存储之前衰减的平方梯度，同时它也会保存之前衰减 的梯度。经过一些处理之后再使用类似Adadelta和RMSprop的方式更新参数。
######9. 优化器代码
```

# coding: utf-8

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
lr = tf.Variable(0.001, dtype=tf.float32)

#创建一个简单的神经网络
W1 = tf.Variable(tf.truncated_normal([784,500],stddev=0.1))
b1 = tf.Variable(tf.zeros([500])+0.1)
L1 = tf.nn.tanh(tf.matmul(x,W1)+b1)
L1_drop = tf.nn.dropout(L1,keep_prob) 

W2 = tf.Variable(tf.truncated_normal([500,300],stddev=0.1))
b2 = tf.Variable(tf.zeros([300])+0.1)
L2 = tf.nn.tanh(tf.matmul(L1_drop,W2)+b2)
L2_drop = tf.nn.dropout(L2,keep_prob) 

W3 = tf.Variable(tf.truncated_normal([300,10],stddev=0.1))
b3 = tf.Variable(tf.zeros([10])+0.1)
prediction = tf.nn.softmax(tf.matmul(L2_drop,W3)+b3)

#交叉熵代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#训练
train_step = tf.train.AdamOptimizer(lr).minimize(loss)

#初始化变量
init = tf.global_variables_initializer()

#结果存放在一个布尔型列表中
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))#argmax返回一维张量中最大的值所在的位置
#求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(51):
        #lr=learning rate, 随着迭代次数的增加，学习率不断的降低
        sess.run(tf.assign(lr, 0.001 * (0.95 ** epoch)))
        for batch in range(n_batch):
            batch_xs,batch_ys =  mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:1.0})
        
        learning_rate = sess.run(lr)
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels,keep_prob:1.0})
        print ("Iter " + str(epoch) + ", Testing Accuracy= " + str(acc) + ", Learning Rate= " + str(learning_rate))

Iter 0, Testing Accuracy= 0.9499, Learning Rate= 0.001
Iter 1, Testing Accuracy= 0.9618, Learning Rate= 0.00095
Iter 2, Testing Accuracy= 0.966, Learning Rate= 0.0009025
Iter 3, Testing Accuracy= 0.9711, Learning Rate= 0.000857375
Iter 4, Testing Accuracy= 0.9729, Learning Rate= 0.000814506
Iter 5, Testing Accuracy= 0.9743, Learning Rate= 0.000773781
。。。
Iter 46, Testing Accuracy= 0.9819, Learning Rate= 9.44682e-05
Iter 47, Testing Accuracy= 0.9815, Learning Rate= 8.97448e-05
Iter 48, Testing Accuracy= 0.9821, Learning Rate= 8.52576e-05
Iter 49, Testing Accuracy= 0.9818, Learning Rate= 8.09947e-05
Iter 50, Testing Accuracy= 0.9827, Learning Rate= 7.6945e-05

```




