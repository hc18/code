####1. GEO 数据库搜索界面
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ddece1573f02671d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. Find genes
- find gene name or symbol: 直接查找数据集组中该基因的基因表达谱
- find genes that are up/down for this conditions: 可以根据选择实验的筛选条件，来找到一系列随该筛选条件有较明显表达差异的基因表达谱。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1f1db1d6475e1468.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-df4ae56a61cb2a58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. Compare 2 sets of samples
![image.png](https://upload-images.jianshu.io/upload_images/6634703-c8121297da8d39eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1527fd2b9684a434.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. Cluster heatmaps 聚类分析图
1. 层级聚类方法：（single-link: 最近距离、complete-link: 最远距离、Average-link: 平均距离）
2. 分散性聚类方法：
- K - Medioids算法 ：用类中的某个点来代表该聚类，能处理任意类型的属性，对异常数据不够敏感
- K - Means 算法： 聚类中心用个各类别中所有数据的平均值表示，应用最为广泛，收敛速度快，能扩展以用于大规模的数据集，倾向于识别凸形分布、大小相近、密度相近的聚类，中心选择和噪声聚类对结果影响大
3. 按基因在染色体上的位置来聚类
![image.png](https://upload-images.jianshu.io/upload_images/6634703-faa0b68a6c5dd667.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-824286f641436d3b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a2842c431add601a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-8f43188226dcd9d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-0e782789986a7d3b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5. Experiment design value distribution (箱线图)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ff377b7f6d8ff9d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-b484bf6cd0a28b47.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####6. GEO2R工具
- GEO2R 能利用开源软件R平台和bioconductor进行数据处理
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f1c5f05f051e4990.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-42abec8d7016dbae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1f5af02a8f1f30b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 分析后的结果
![image.png](https://upload-images.jianshu.io/upload_images/6634703-7477f8e2227ccba3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-024976cc73ae167a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/6634703-01085e3dc70c8b33.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- R 语言脚本，可以自己下载学习修改
```
# Version info: R 3.2.3, Biobase 2.30.0, GEOquery 2.40.0, limma 3.26.8
# R scripts generated  Wed May 16 00:10:26 EDT 2018

################################################################
#   Differential expression analysis with limma
library(Biobase)
library(GEOquery)
library(limma)

# load series and platform data from GEO

gset <- getGEO("GSE642", GSEMatrix =TRUE, AnnotGPL=TRUE)
if (length(gset) > 1) idx <- grep("GPL81", attr(gset, "names")) else idx <- 1
gset <- gset[[idx]]

# make proper column names to match toptable 
fvarLabels(gset) <- make.names(fvarLabels(gset))

# group names for all samples
gsms <- "000000111111"
sml <- c()
for (i in 1:nchar(gsms)) { sml[i] <- substr(gsms,i,i) }

# log2 transform
ex <- exprs(gset)
qx <- as.numeric(quantile(ex, c(0., 0.25, 0.5, 0.75, 0.99, 1.0), na.rm=T))
LogC <- (qx[5] > 100) ||
          (qx[6]-qx[1] > 50 && qx[2] > 0) ||
          (qx[2] > 0 && qx[2] < 1 && qx[4] > 1 && qx[4] < 2)
if (LogC) { ex[which(ex <= 0)] <- NaN
  exprs(gset) <- log2(ex) }

# set up the data and proceed with analysis
sml <- paste("G", sml, sep="")    # set group names
fl <- as.factor(sml)
gset$description <- fl
design <- model.matrix(~ description + 0, gset)
colnames(design) <- levels(fl)
fit <- lmFit(gset, design)
cont.matrix <- makeContrasts(G1-G0, levels=design)
fit2 <- contrasts.fit(fit, cont.matrix)
fit2 <- eBayes(fit2, 0.01)
tT <- topTable(fit2, adjust="fdr", sort.by="B", number=250)

tT <- subset(tT, select=c("ID","adj.P.Val","P.Value","t","B","logFC","Gene.symbol","Gene.title"))
write.table(tT, file=stdout(), row.names=F, sep="\t")


################################################################
#   Boxplot for selected GEO samples
library(Biobase)
library(GEOquery)

# load series and platform data from GEO

gset <- getGEO("GSE642", GSEMatrix =TRUE, getGPL=FALSE)
if (length(gset) > 1) idx <- grep("GPL81", attr(gset, "names")) else idx <- 1
gset <- gset[[idx]]

# group names for all samples in a series
gsms <- "000000111111"
sml <- c()
for (i in 1:nchar(gsms)) { sml[i] <- substr(gsms,i,i) }
sml <- paste("G", sml, sep="")  set group names

# order samples by group
ex <- exprs(gset)[ , order(sml)]
sml <- sml[order(sml)]
fl <- as.factor(sml)
labels <- c("A","B")

# set parameters and draw the plot
palette(c("#dfeaf4","#f4dfdf", "#AABBCC"))
dev.new(width=4+dim(gset)[[2]]/5, height=6)
par(mar=c(2+round(max(nchar(sampleNames(gset)))/2),4,2,1))
title <- paste ("GSE642", '/', annotation(gset), " selected samples", sep ='')
boxplot(ex, boxwex=0.6, notch=T, main=title, outline=FALSE, las=2, col=fl)
legend("topleft", labels, fill=palette(), bty="n")

```




