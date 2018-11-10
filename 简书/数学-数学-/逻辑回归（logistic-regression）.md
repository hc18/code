>成本最小的学习方案: 了解公式推导指南，用计算机语言实现一遍，解决一个实例。
######1. 公式推导
- 在线性回归中，我们研究的是连续量的变化情况，而在逻辑回归中研究对象则变成了离散量，简单来说，在线性回归中我们输入一个值 x ，然后输出它对应的数值 y ，而在逻辑回归中，我们输入一个值  x ，判断它是属于 0 还是 1 。
- 对于判断输入值属于 0 还是 1 ，我们通过的是概率的方法，概率大于 50\% 判断为 1 ，概率小于  50\% 判断为 0 。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5086cf2f320b2ed5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
具体详见 https://zhuanlan.zhihu.com/p/37020923
- 通常，我们让0为“负类”（Negative class），1为“正类”（Positive class）：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3ce982bf6fd4c024.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 因为有一个outliner, 所以线形拟合不够好
![image.png](https://upload-images.jianshu.io/upload_images/6634703-59cefc6a5c3123db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-2ad654cf31b87745.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-660d93bfbc51e127.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 所以引入逻辑回归
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3283c49b4e47cc68.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3cb14970653ce23a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5daffbc34df07f5a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 训练集用来拟合参数θ，然后θ就决定了决策边界。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-8d73854f7b17c3ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 训练集用来拟合参数θ，然后θ就决定了决策边界。
####代价函数（cost function）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5a7b97f407c1b88d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
这样代价函数，是非凸函数，如果使用梯度下降，几乎不能收敛到最全局最小值，所以我们需要寻找其他的是凸函数的代价函数，这样就可以使用之前学过的算法了。
（只有凸函数可以到全局最小值，其他可能到局部最低点）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-c0158ba3f0661fad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6c4484d1f1356685.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f39a7f5518408828.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-da868cebb162653a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 当假设h(θ)=1时，如果y是1，那么cost=0；如果y=0，那么cost=∞。
当假设h(θ)=0时，如果y时1，那么cost=∞；如果y=0，那么cost=0。
######简化代价函数和梯度下降
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3b60feb6b3391c22.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9d2bdc0ea5af2c29.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 这个代价函数它是凸的（convex），所以使用梯度下降可以获得全局最优解。
- 梯度下降（gradient descent ）：
线性回归的特征缩放（提高梯度下降的速度）在逻辑回归中依然可以使用。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-0193e442314694aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-be097a82fe569f64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-959c2fcb9701ccde.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6bf740a834a32a3b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####python 实战
####1. logRegression.py
```
#################################################
# logRegression: Logistic Regression
# Author : zouxy
# Date   : 2014-03-02
# HomePage : http://blog.csdn.net/zouxy09
# Email  : zouxy09@qq.com
#################################################

from numpy import *
import matplotlib.pyplot as plt
import time


# calculate the sigmoid function
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))

# train a logistic regression model using some optional optimize algorithm
# input: train_x is a mat datatype, each row stands for one sample
#		 train_y is mat datatype too, each row is the corresponding label
#		 opts is optimize option include step and maximum number of iterations
def trainLogRegres(train_x, train_y, opts):
    # calculate training time
    startTime = time.time()

    numSamples, numFeatures = shape(train_x)
    alpha = opts['alpha']
    maxIter = opts['maxIter']
    weights = ones((numFeatures, 1))

    # optimize through gradient descent algorilthm
    for k in range(maxIter):
        if opts['optimizeType'] == 'gradDescent':  # gradient descent algorilthm
            output = sigmoid(train_x * weights)
            error = train_y - output
            weights = weights + alpha * train_x.transpose() * error
        elif opts['optimizeType'] == 'stocGradDescent':  # stochastic gradient descent
            for i in range(numSamples):
                output = sigmoid(train_x[i, :] * weights)
                error = train_y[i, 0] - output
                weights = weights + alpha * train_x[i, :].transpose() * error
        elif opts['optimizeType'] == 'smoothStocGradDescent':  # smooth stochastic gradient descent
            # randomly select samples to optimize for reducing cycle fluctuations
            dataIndex = list(range(numSamples))
            for i in range(numSamples):
                alpha = 4.0 / (1.0 + k + i) + 0.01
                randIndex = int(random.uniform(0, len(dataIndex)))
                output = sigmoid(train_x[randIndex, :] * weights)
                error = train_y[randIndex, 0] - output
                weights = weights + alpha * train_x[randIndex, :].transpose() * error
                del (dataIndex[randIndex])  # during one interation, delete the optimized sample
        else:
            raise NameError('Not support optimize method type!')

    print('Congratulations, training complete! Took %fs!' % (time.time() - startTime))
    return weights


# test your trained Logistic Regression model given test set
def testLogRegres(weights, test_x, test_y):
    numSamples, numFeatures = shape(test_x)
    matchCount = 0
    for i in range(numSamples):
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
        if predict == bool(test_y[i, 0]):
            matchCount += 1
    accuracy = float(matchCount) / numSamples
    return accuracy


# show your trained logistic regression model only available with 2-D data
def showLogRegres(weights, train_x, train_y):
    # notice: train_x and train_y is mat datatype
    numSamples, numFeatures = shape(train_x)
    if numFeatures != 3:
        print("Sorry! I can not draw because the dimension of your data is not 2!")
        return 1

    # draw all samples
    for i in range(numSamples):
        if int(train_y[i, 0]) == 0:
            plt.plot(train_x[i, 1], train_x[i, 2], 'or')
        elif int(train_y[i, 0]) == 1:
            plt.plot(train_x[i, 1], train_x[i, 2], 'ob')

    # draw the classify line
    min_x = min(train_x[:, 1])[0, 0]
    max_x = max(train_x[:, 1])[0, 0]
    weights = weights.getA()  # convert mat to array
    y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
    y_max_x = float(-weights[0] - weights[1] * max_x) / weights[2]
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()




def loadData():
    train_x = []
    train_y = []
    fileIn = open('testSet.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split()
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        train_y.append(float(lineArr[2]))
    return mat(train_x), mat(train_y).transpose()


## step 1: load data
print("step 1: load data...")
train_x, train_y = loadData()
test_x = train_x
test_y = train_y

## step 2: training...
print("step 2: training...")
opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'smoothStocGradDescent'}
optimalWeights = trainLogRegres(train_x, train_y, opts)

## step 3: testing
print("step 3: testing...")
accuracy = testLogRegres(optimalWeights, test_x, test_y)

## step 4: show the result
print("step 4: show the result...")
print('The classify accuracy is: %.3f%%' % (accuracy * 100))
showLogRegres(optimalWeights, train_x, train_y)
```
data
```
-0.017612	14.053064	0
-1.395634	4.662541	1
-0.752157	6.538620	0
-1.322371	7.152853	0
0.423363	11.054677	0
0.406704	7.067335	1
0.667394	12.741452	0
-2.460150	6.866805	1
0.569411	9.548755	0
-0.026632	10.427743	0
0.850433	6.920334	1
1.347183	13.175500	0
1.176813	3.167020	1
-1.781871	9.097953	0
-0.566606	5.749003	1
0.931635	1.589505	1
-0.024205	6.151823	1
-0.036453	2.690988	1
-0.196949	0.444165	1
1.014459	5.754399	1
1.985298	3.230619	1
-1.693453	-0.557540	1
-0.576525	11.778922	0
-0.346811	-1.678730	1
-2.124484	2.672471	1
1.217916	9.597015	0
-0.733928	9.098687	0
-3.642001	-1.618087	1
0.315985	3.523953	1
1.416614	9.619232	0
-0.386323	3.989286	1
0.556921	8.294984	1
1.224863	11.587360	0
-1.347803	-2.406051	1
1.196604	4.951851	1
0.275221	9.543647	0
0.470575	9.332488	0
-1.889567	9.542662	0
-1.527893	12.150579	0
-1.185247	11.309318	0
-0.445678	3.297303	1
1.042222	6.105155	1
-0.618787	10.320986	0
1.152083	0.548467	1
0.828534	2.676045	1
-1.237728	10.549033	0
-0.683565	-2.166125	1
0.229456	5.921938	1
-0.959885	11.555336	0
0.492911	10.993324	0
0.184992	8.721488	0
-0.355715	10.325976	0
-0.397822	8.058397	0
0.824839	13.730343	0
1.507278	5.027866	1
0.099671	6.835839	1
-0.344008	10.717485	0
1.785928	7.718645	1
-0.918801	11.560217	0
-0.364009	4.747300	1
-0.841722	4.119083	1
0.490426	1.960539	1
-0.007194	9.075792	0
0.356107	12.447863	0
0.342578	12.281162	0
-0.810823	-1.466018	1
2.530777	6.476801	1
1.296683	11.607559	0
0.475487	12.040035	0
-0.783277	11.009725	0
0.074798	11.023650	0
-1.337472	0.468339	1
-0.102781	13.763651	0
-0.147324	2.874846	1
0.518389	9.887035	0
1.015399	7.571882	0
-1.658086	-0.027255	1
1.319944	2.171228	1
2.056216	5.019981	1
-0.851633	4.375691	1
-1.510047	6.061992	0
-1.076637	-3.181888	1
1.821096	10.283990	0
3.010150	8.401766	1
-1.099458	1.688274	1
-0.834872	-1.733869	1
-0.846637	3.849075	1
1.400102	12.628781	0
1.752842	5.468166	1
0.078557	0.059736	1
0.089392	-0.715300	1
1.825662	12.693808	0
0.197445	9.744638	0
0.126117	0.922311	1
-0.679797	1.220530	1
0.677983	2.556666	1
0.761349	10.693862	0
-2.168791	0.143632	1
1.388610	9.341997	0
0.317029	14.739025	0
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-b5167a37a0936827.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####参考文献
1. https://www.jianshu.com/p/3231d44d5f6f
2. https://blog.csdn.net/zouxy09/article/details/20319673
