![image.png](https://upload-images.jianshu.io/upload_images/6634703-fb87c1d70417b14e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- beta分布可以看作一个概率的概率分布，当你不知道一个东西的具体概率是多少时，它可以给出了所有概率出现的可能性大小。
- 棒球活动，根据棒球的历史信息，我们知道球员的击球率应该是0.215到0.36之间。
- 所以吧(a,b) 调为（81，219）可以算作先验分布，此分布是（0.215-0.36）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-148241401bd25d35.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-4ce5a9b05221fbc4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 如果打了300次，击中100次，新的分布为beta（181,419）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-59db67524a2a1fa3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 没有先验分布的命中率为100/300=0.333
- 有先验分布的命中率为 181/600=0.303
