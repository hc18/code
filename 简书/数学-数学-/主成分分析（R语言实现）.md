####前言
主成分分析原理在我另一篇里有介绍（https://www.jianshu.com/p/7ceb82959258）
####1. 降维概述
- 降维是指将样本从输入空间通过线性或非线性映射到一个低维空间
- 降维可以减少无用信息和冗余信息，将高维数据转换为易于处理的低维数据，减少了后续步骤处理的计算量，当降至三维以下时还可用于可视化技术，从而额发挥人在低维空间感知上的优点，发现数据集的空间分布、聚类性质等结构特征
####2. 主成分分析
![image.png](https://upload-images.jianshu.io/upload_images/6634703-056988474c957931.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####R 语言实现
####2.1 材料准备
1. 分析数据，横轴为样本名称，纵轴为芯片探针
![image.png](https://upload-images.jianshu.io/upload_images/6634703-4c418015adeee7d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 不同的肿瘤样本临床分期信息
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3da9bcc0015bddba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####R 语言实现
```
##读入数据
dat = read.table("GeneExpression.txt",header=TRUE,sep="\t")
traits = read.table('sampleTraits.txt',sep="\t",header= T)

##定义颜色
blue = "#307eb9"
purple = "#974e9e"
red = "#e41e25"
orange = "#f57f21"
yellow = "#f4ed35"
lblue = "#74d7ff"
red2 = "#ff1751"
green = "#4cb049"

color = factor(traits$grade,
               labels = c(lblue,purple,orange,yellow,red2,green,"black"),
               levels = c("G1","G2","G3","G4","G5","G6","G7"))

##主成分分析 ？princomp 查看帮助文档
pca <- princomp(dat)

##可视化， 可多角度观看
#draw 3d plot--1
library(rgl) 
plot3d(pca$loadings[,1:3],col=color,
       type="s",radius=0.005,
       grid=50L,pch=16)

#draw 3d plot--2
##一个角度
library(scatterplot3d)
scatterplot3d(pca$loadings[,1:3],main='PCA',color=color,type='p',
              highlight.3d=F,angle=60,grid=T,box=T,scale.y=1,
              cex.symbols=0.8,pch=16,col.grid='lightblue')
legend("topright",paste("G",1:7,sep=""),fill=c(lblue,purple,orange,yellow,red2,green,"black"),box.col="grey")

##多个角度，存到pdf,可以选一张喜欢的图展示
library(scatterplot3d)
pdf('pca.pdf',onefile=TRUE,width=8,height=8)
diffangle <- function(ang){
  scatterplot3d(pca$loadings[,1:3],main='PCA',color=color,type='p',
                highlight.3d=F,angle=ang,grid=T,box=T,scale.y=1,
                cex.symbols=1.2,pch=16,col.grid='lightblue')
  legend("topright",paste("G",1:7,sep=""),fill=c(lblue,purple,orange,yellow,red2,green,"black"),box.col="grey")
}
sapply(seq(-360,360,5),diffangle)
dev.off()

```
- 可见同期样本很好的发生了聚集，期与期之间也相互有距离
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3b585c93dbf6e04b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9b3cbad8fcf07248.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
