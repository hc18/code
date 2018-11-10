![image.png](https://upload-images.jianshu.io/upload_images/6634703-da5a25a421b5db59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 这篇文章用公共数据发表到了 scientific report，影响因子为4.29。
####0. 文章idea来源
- 近年来，癌症基因图谱越来越完善，研究人员发现癌症来自不同的组织可以共享一些共同的特征，如突变，甲基化和转录组学变化。那么研究者门在不同的组织中寻找一些lncRNAs 与癌症的关系。
> 于是作者有了一个idea, 是不是不同的癌症之间，也共享一些lncRNA变异?
####1. 有了idea, 寻找新颖的解决方法
- 以前人们认为长链非编码RNA(后面 lncRNA)是“噪音”，对蛋白质编码没什么作用，但是现在已经有很多证据表明它的生物学功能广泛，但是大多数lncRNA 功能尚未阐明，理解它的功能也是一个巨大的挑战。
- 从做实验角度寻找lncRNA功能的缺陷是通量太低，速度慢；计算角度预测lncRNA功能的缺陷是，假阳性太多，不稳定。
- 不过，市面上已经有一个成熟软件“WGCNA” 已经成功用于蛋白质编码基因，详见[WGCNA（加权基因共表达网络分析）](https://www.jianshu.com/p/3618f5ff3eb0).
- 但是，这个牛X的方法在 癌症和lncRNA 中还没有人用！（这是创新点）
####2.有了解决方法，寻找实验对象
- 前面已经有一个idea 和解决方法了, 那么对象是谁呢？网上公共数据库找呗，于是作者定位了四个库：
- 12个肺癌，29个乳腺癌，14个前列腺癌，11个膀胱癌
![image.png](https://upload-images.jianshu.io/upload_images/6634703-b99b503afd3827b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. 结果
>1. 先看一下差异表达

![image.png](https://upload-images.jianshu.io/upload_images/6634703-0334e2f73ef81bfb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 图a 说明，PCGs 14470 中有11147 共表达
2. 图b 说明，lncRNA 2902 中有896共表达
3. 图c 横坐标 不同基因，纵坐标表达比例
4. PCGs 表达 高于 lncRNA

>2. 再看一下聚类，癌症样本和正常样本

![Hierarchical clustering based on expression profiles of significantly differentially expressed lncRNA genes (DELs) from each cancer type. (a) The heatmap of 357 DELs in bladder cancer. (b) The heatmap of 321 DELs in prostate cancer. (c) The heatmap of 267 DELs lung adenocarcinoma. (d) The heatmap of 375 DELs in breast cancer. The intensity of the color scheme is scaled to expression values (log2(FPKM + 0.1)) which are Z-score standardized per gene. The color bar above the heatmap represents the sample groups, and red indicates tumor sample, and blue represents normal sample.](https://upload-images.jianshu.io/upload_images/6634703-0a9a9a9b7907b3d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 聚类效果不错，红色代表肿瘤样本，蓝色代表正常样本。
>3. 作者筛选出有236个共表达lncRNA,但只有11个有文献报道，见下图

![所有四种癌症中的11种特征性的onco-lncRNA的热图。红色表示上调，蓝色表示下调。空白表示在癌症中不显着表达的基因。](https://upload-images.jianshu.io/upload_images/6634703-86f873fce57b7735.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>4. 共表达进化树

![image.png](https://upload-images.jianshu.io/upload_images/6634703-43ee71c418d6da7a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-de4402adb58e1b9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 总共分为12 个模块
- 作者说 brown 模型非常重要，因为有67个共表达

>5. 作者把这12个模块做了功能富集分析，并预测这些表达的功能

 ![image.png](https://upload-images.jianshu.io/upload_images/6634703-2e933647401271ac.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 6. 最后为共表达网络分析

![brown top51 hub 基因](https://upload-images.jianshu.io/upload_images/6634703-40a89b82b649724a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 网络不要做的太大，不然无法体现生物学信息
- 分为6个功能类描述
####5 结论
1. 首次使用WGCNA方法基于RNA-seq数据研究跨多个癌症的lncRNA的功能
2. 这篇文章找到的236个onco-reports 只有11个是已报到的，剩下的需要去验证
3. 提出了一种简便高效的策略来鉴定与癌症相关的重要lncRNA并预测它们潜在的功能作用，这可以指导随后的实验研究。




