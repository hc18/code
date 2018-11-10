![image.png](https://upload-images.jianshu.io/upload_images/6634703-d630cf134e01a25b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 5 维窗口，在序列T里面扫过，每走一步，start positon 建立一个index
####如何索引？
- 先找索引开始坐标，然后匹配剩下的
![](https://upload-images.jianshu.io/upload_images/6634703-7bc13dcec87eb181.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 
####优化
- 3维 index
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5e0a1c0d80f5a680.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 按照字母大小排序
![image.png](https://upload-images.jianshu.io/upload_images/6634703-879c29bcdce3c82a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 比如说要查找TGG，用二分法快速定位
![image.png](https://upload-images.jianshu.io/upload_images/6634703-fc8693aa479ff7cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 最后找到TGG，（大O=log(n)）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-fe20bd12cb85a2e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


