- 主成分分析（PCA）是一种能够极大提升无监督特征学习速度的数据降维算法
####1 降维
- 举一个把2维降低到1维的例子
![image.png](http://upload-images.jianshu.io/upload_images/6634703-ee0d861fa9d7a1ba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 这些数据已经进行了预处理，使得每个特征x1和x2具有相同的均值（零）和方差。
- 为方便展示，根据值的大小，我们将每个点分别涂上了三种颜色之一，但该颜色并不用于算法而仅用于图解。
- PCA算法将寻找一个低维空间来投影我们的数据。从下图中可以看出，u1是数据变化的主方向，而u2是次方向。
![image.png](http://upload-images.jianshu.io/upload_images/6634703-e14ad555ea9aa00f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 用以下公式算出协方差u1,u2
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f0ba846ecb0ffe71.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 假设x的均值为零，那么Sigma就是x的协方差矩阵。
- 算出u1 的协方差为7.29，u2 的协方差为0.69
![image.png](http://upload-images.jianshu.io/upload_images/6634703-57395fd9b2e7086c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2 旋转数据
- 把 x 用（u1,u2）作为基旋转数据
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b44d717ab86c07b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-0ea77003f2b06688.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3 数据降维
- 先举一个四维的例子
- 特征矩阵是一个对角线矩阵从左上到右下数值依次递减,每个数值表示一个特征值(pca的特征矩阵的值都是正数)。
- 特征值越大表示这个维度包含的信息越多，你看有几个比较大的特征值，k大概就是选几个.简单的例子:你对数据做了一个PCA产生了一个特征矩阵(这个数据的维度是4)
- 特征两辆之间的协方差为0
![image.png](http://upload-images.jianshu.io/upload_images/6634703-4f4ae06dcb8ac401.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 很显然特征值得变化就告诉你有两个特征值100 和 30 远远大于剩下的那个两个1 和0.1，你就可以设定k是2,因为100 和 30对应的维度已近基本上囊括的数据的绝大多数的信息
- 回到我们上面的例子，取（n=2,k=1）实现降维
![image.png](http://upload-images.jianshu.io/upload_images/6634703-a715e076246919e5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 在面的二维实验中，我们保留了，7.29/(7.29+0.69)=91.3%的方差。
- 一般向他人介绍PCA算法详情，告诉他们你选择的k保留了95%的方差，比告诉他们你保留了前120个（或任意某个数字）主成分更好理解。
####4 参考文献
1. https://www.zhihu.com/question/21980732(知乎)
2. http://ufldl.stanford.edu/wiki/index.php/%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90（主成分分析与白化）
3. https://wenku.baidu.com/view/1745b0be2cc58bd63186bdad.html（PCA的原理及详细步骤）
