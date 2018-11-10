####前言
- 这篇文章讲WGCNA方法论
- 这篇文章发在2008年BMC Bioinformatics(IF = 3.781)，但是到目前的引用量高达1926.
####1. 为什么要开发这个软件
1. 在现有方法中（差异分析或趋势分析无法对基因进行有效分类）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e00f86e6e23a8f1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 依赖数据的功能分析无法推测新的调控关系
- Kegg 的 pathway 都来源文献已报到的调控关系
- 如果你关注的调控系在已有数据库未录入（或还没被报道），依赖这些分析是难以找到线索的。
####2. WGCNA 有点
- 从“系统”的角度去解析关注的问题，而不是去罗列单一基因的清单
- 研究关注点是基因模块，而不是单一基因
- 网络的概念让抽象的生物学问题更直观易懂
####3. 基础知识
1. 为什么基因表达量存在相关性
- 在一定机制控制下，功能相关的一组基因，协调一致，共同表达
- 也有可能一个基因诱导/遏制另外一个基因的表达
2. 模块 ：表达模式相似的一组基因
3. 模块中的所有基因进行 PCA 分 析，得到的主成1（PC1 ）的值。 PC1 相当于模块中所有基因表达量的加权，可以代 表这个模块的达式。
####3. WGCNA 网络相关的一些基础概念
######3.1 Functions for network construction
- 无尺度网络介绍
![image.png](https://upload-images.jianshu.io/upload_images/6634703-78ee97dd002f0ada.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 如何把基因与基因之间的关系矩阵变为0-1的矩阵。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-431eb6661babc1f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-91900625f51e7a97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9f88ab4bb7d7712f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-db8478a2a845c4eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e48f4295cbdb401b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ccb1b5dbc685da94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. WGCNA 网络生物学意义的挖掘
######4.1 目标模块选取
1. 模块表达模式
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d8ef869d1b29bd0b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 模块相关性分析
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a8ee05331248db9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 富集分析
- 如上文提到的 存在诱导 /阻遏表达（ TF 和靶基因）或协调表达（例如 被同一个 TF 调控一组基因）关系的，更容易出现在个模块中。
- 而且在大样本的情况下，基因表达分类更加有规律。 
- 所以，对模块开展 KEGG KEGG、GO 功能富集分析，通常会找到很有规律的类型。
######4.2 模块内的分析
1. 从模板基因入手
- 模块内的功能调控关系分析
2. 基因的模块内连通性
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f6e8c4461bbdd565.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 核心基因
![image.png](https://upload-images.jianshu.io/upload_images/6634703-7d16d14e76acd593.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. 目标基因相关的局部调控网络
![image.png](https://upload-images.jianshu.io/upload_images/6634703-826a72ad8d159ba3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
5. 关注特定类型的基因
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f57c671c5648f6d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5. 进行WGCNA分析的两个关键问题
1. WGCNA 分析对样本有什么要求？
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e2d2be49a57e8bd7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####6. WGCNA的步骤总结
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f8f1ee0e103344bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-74bf3374a37b99a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-66ff1c54815c3c7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

