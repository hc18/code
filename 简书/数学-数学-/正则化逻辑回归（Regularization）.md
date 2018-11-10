######1. 过拟合的问题（The problem of overfitting）
正则化可以减轻过拟合问题。
欠拟合（underfitting）
高偏差（high bias）
过拟合（overfitting）
高方差（high variance）
泛化（generalize）：指假设模型能应用到新样本的能力。
- 特征太多，数据量太少，过度拟合就会发生：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a1c07c8087118cbd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>解决过度拟合方法：
1.减少特征数量：
手动选择
使用模型选择算法（后面会讲）
>2. 正则化（regularization）
保留所有的特征，但是减少参数θj的大小（magnitude/values）
当我们有很多特征的时候依然工作很好，并且每个特征都对预测y有一定的贡献

![image.png](https://upload-images.jianshu.io/upload_images/6634703-f8b79eb57a6ced45.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######2. 代价函数（Cost function）
- 正则化思想：减小高次项的θ值，使得曲线平滑。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3c4b5f9472e74105.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 加入正则项。λ是正则化参数，保持我们能很好的拟合数据，保持参数较小从而避免过拟合。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-48970228f4a700ba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-c13400d2b5091e31.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
λ不能太大，否则就是一条直线，（underfitting/too high bias），肯定也不能太小，否则就没效果了。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f83f662a7c7812bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######3. 正则化线性回归（Regularization linear regression）
梯度下降（gradient decent）算法下正则化线性回归的计算：
θ0不参与，所以排除在外。
相当于把θj缩小了。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-22b65134ca46da24.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 在正规方程（normal equation）中正则化线性回归的计算：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-367dd7a4bad086af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 加入正则化项后，只要 λ>0 那么该矩阵可逆。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-46e421c639f67f36.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######4 正则化逻辑回归（Regularization logistic regression）
- 原理相同，加入正则化项，然后计算：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-944f2c58856386c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-111f4c1e8e64a91d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



