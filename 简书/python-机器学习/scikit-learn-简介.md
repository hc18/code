######1. sklearn 图谱
![原版](https://upload-images.jianshu.io/upload_images/6634703-2712406496cdc0e9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 汉化版
![汉化版](https://upload-images.jianshu.io/upload_images/6634703-4ca512cb9aa578e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######2. 简介
- 我们可以看到，机器学习分为四大块，分别是 classification (分类)， clustering (聚类), regression (回归), dimensionality reduction (降维)。
- 给定一个样本特征 x, 我们希望预测其对应的属性值 y, 如果 y 是离散的, 那么这就是一个**分类**问题，反之，如果 y 是连续的实数, 这就是一个**回归**问题。
- 如果给定一组样本特征 `S={x∈RD}`, 我们没有对应的 y, 而是想发掘这组样本在 D 维空间的分布, 比如分析哪些样本靠的更近，哪些样本之间离得很远, 这就是属于**聚类**问题。
- 如果我们想用维数更低的子空间来表示原来高维的特征空间, 那么这就是**降维**问题。
######2.1 classification & regression
- 无论是分类还是回归，都是想建立一个预测模型 H，给定一个输入 x, 可以得到一个输出 y: 
`y=H(x)`
- 不同的只是在分类问题中, y 是离散的; 而在回归问题中 y 是连续的。所以总得来说，两种问题的学习算法都很类似。所以在这个图谱上，我们看到在分类问题中用到的学习算法，在回归问题中也能使用。分类问题最常用的学习算法包括 SVM (支持向量机) , SGD (随机梯度下降算法), Bayes (贝叶斯估计), Ensemble, KNN 等。而回归问题也能使用 SVR, SGD, Ensemble 等算法，以及其它线性回归算法。
######2.2 clustering
- 聚类也是分析样本的属性, 有点类似classification, 不同的就是classification 在预测之前是知道 y 的范围, 或者说知道到底有几个类别, 而聚类是不知道属性的范围的。所以 classification 也常常被称为 supervised learning, 而clustering就被称为 unsupervised learning。 
- clustering 事先不知道样本的属性范围，只能凭借样本在特征空间的分布来分析样本的属性。这种问题一般更复杂。而常用的算法包括 k-means (K-均值), GMM (高斯混合模型) 等。

######2.3 dimensionality reduction
- 降维是机器学习另一个重要的领域, 降维有很多重要的应用, 特征的维数过高, 会增加训练的负担与存储空间, 降维就是希望去除特征的冗余, 用更加少的维数来表示特征. 降维算法最基础的就是PCA了, 后面的很多算法都是以PCA为基础演化而来。
####参考文献
1. https://blog.csdn.net/a790209714/article/details/52708464
2. https://blog.csdn.net/matrix_space/article/details/50541217
3. http://scikit-learn.org/stable/（官网）
