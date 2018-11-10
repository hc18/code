####前言
- 基因之间存在共表达
- 共表达的基因可能具有相似的生物功能
- 从具有相似的表达谱的基因去推测其功能
- 利用不同基因表达模式对样本进行分类，找到潜在的分子标志物
- 更好的可视化
####1. 层次聚类
- 层次聚类原理：https://www.jianshu.com/p/bf314992d4c2 （我在另一篇文章有写，这里不做详细介绍）
- 在聚类分析中，基因被看作是一个向量
- 通过元素与元素之间的距离，将不同的元素归类
![基因表达量用数据表示，方便计算距离](https://upload-images.jianshu.io/upload_images/6634703-457647930fd9c2de.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. R 语言实现
####2.1 材料准备
1. 找到事先筛选好的差异表达基因，横轴为样本，纵轴为基因
![image.png](https://upload-images.jianshu.io/upload_images/6634703-c4b9b7a3abb3bf91.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 样本的临床信息（HCC肝癌，NOR，正常组）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5c2b4ad4723b19c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2.2 R 代码
```
library(gplots)
library(RColorBrewer)
options(stringsAsFactors = F)

#读取数据
datExp = read.table('ExpressionDataForDEG.txt',sep='\t',header=T)
View(head(datExp))

#处理数据
datExp1 = datExp[, -1] # -1 表示第一列不要
rownames(datExp1) = datExp[, 1] # 把基因名称定义为行名
View(datExp1)

#读取患者分组信息
datTraits = read.table('SampleTraits.txt',sep='\t',header=T)
View(datTraits)
color = factor(datTraits$tumor,labels=c('orange','blue'),levels = c("HCC","NOR"))
color

#数据转换
datExp1 = as.matrix(datExp1) # 把dataframe 转换成 matrix

#聚类热图 
# 参数具体含义 ？heatmap.2 查询
heatmap.2(datExp1,col = greenred(75), 
          hclust=function(x) hclust(x,method = 'ward.D2'),
          distfun=function(x) dist(x,method='euclidean'),
          scale = "row",dendrogram = 'both',
          key = TRUE, symkey = FALSE, density.info = "none", 
          trace = "none", cexRow = 0.5,
          ColSideColors = as.character(color)
)
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-52a71d5c6ddb19d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 生物学意义：
1. 筛选的差异基因可以显著的把肿瘤样本和正常样本筛选出来
2. 分类出来的基因，可以用于后续功能富集分析
3. 导出尽量pdf 格式，是矢量图，便于投稿修改
