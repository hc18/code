1. 线性判别式分析（Linear Discriminant Analysis），简称为LDA。也称为Fisher线性判别（Fisher Linear Discriminant，FLD）
2. 基本思想是将高维的模式样本投影到最佳鉴别矢量空间，以达到抽取分类信息和压缩特征空间维数的效果，投影后保证模式样本在新的子空间有**最大的类间距离**和**最小的类内距离**，即模式在该空间中有最佳的可分离性。
3. LDA与前面介绍过的PCA都是常用的降维技术。PCA主要是从特征的协方差角度，去找到比较好的投影方式。LDA更多的是考虑了标注，即希望投影后不同类别之间数据点的距离更大，同一类别的数据点更紧凑。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-357a5a55c5422852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-53112b9ec2d1459c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 这里的y 是x投影到直线上的点到原点的距离。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d245084d719b2733.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 什么是最佳的直线（w）呢？我们首先发现，能够使投影后的两类样本中心点尽量分离的直线是好的直线，定量表示就是上面的J（w）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9ac8d2c637feec15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
但是只考虑J(w)是不行的，样本点均匀分布在椭圆里，投影到横轴x1上时能够获得更大的中心点间距J(w)，但是由于有重叠，x1不能分离样本点。投影到纵轴x2上，虽然J(w)较小，但是能够分离样本点。因此我们还需要考虑样本点之间的方差，方差越大，样本点越难以分离。我们使用另外一个度量值，称作散列值（scatter），对投影后的类求散列值
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ac6731ca0d6dc603.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-265d0c4977b0c47e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
-  而我们想要的投影后的样本点的样子是：不同类别的样本点越分开越好，同类的越聚集越好，也就是均值差越大越好，散列值越小越好。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-22cb623a8d448699.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
-  接下来的事就比较明显了，我们只需寻找使J(w)最大的w即可。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1ac57a90a62eb86c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-068cb499d089bf3f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-008efcb48b11ac77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-aeb47dfc3adc9025.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 这两个求导没看懂，先留着以后看
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ba166608d0a149f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-812867879e7b761f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####LDA实例详解（matlab）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-bdf36298e13c3706.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dfd1d90678a5ba1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1578cd92f0bfeac5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f451dfa220592638.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-c5baa5ac8dc6a607.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ce3a6640b630610d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-af19e8ac0bb90465.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dc686e242393c266.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-4acc86139c49947b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d3a8848b10aff609.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5376ad6fbd981ad8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####LDA vs PCA
　　　　LDA用于降维，和PCA有很多相同，也有很多不同的地方，因此值得好好的比较一下两者的降维异同点。
　　　　首先我们看看相同点：
　　　　1）两者均可以对数据进行降维。
　　　　2）两者在降维时均使用了矩阵特征分解的思想。
　　　　3）两者都假设数据符合高斯分布。
　　　　我们接着看看不同点：
　　　　1）LDA是有监督的降维方法，而PCA是无监督的降维方法
　　　　2）LDA降维最多降到类别数k-1的维数，而PCA没有这个限制。
　　　　3）LDA除了可以用于降维，还可以用于分类。
　　　　4）LDA选择分类性能最好的投影方向，而PCA选择样本点投影具有最大方差的方向。
　　　　这点可以从下图形象的看出，在某些数据分布下LDA比PCA降维较优。
#### 参考文献
1. https://blog.csdn.net/jnulzl/article/details/49894041
2. http://www.cnblogs.com/jerrylead/archive/2011/04/21/2024384.html

