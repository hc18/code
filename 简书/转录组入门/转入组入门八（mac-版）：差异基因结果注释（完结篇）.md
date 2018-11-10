####任务
>我们统一选择p<0.05而且abs(logFC)大于1的基因为显著差异表达基因集，对这个基因集用R包做KEGG/GO超几何分布检验分析。然后把表达矩阵和分组信息分别作出cls和gct文件，导入到GSEA软件分析。基本任务是完成这个分析。[生信技能树](http://www.biotrainee.com/thread-1749-1-1.html)
####1. 差异基因筛选
- 把“转入组入门七”的代码搬运过来，最后我们得到的数据是diff_gene_deseq2, 包含了差役表达基因
```
library(DESeq2)
# 首先将四个文件分别赋值：control1，control2，rep1，rep2
control1 <- read.table("/Users/chengkai/Desktop/zhuanlu_files/RNA-Seq/matrix/SRR3589959.count", sep="\t", col.names = c("gene_id","control1"))
control2 <- read.table("/Users/chengkai/Desktop/zhuanlu_files/RNA-Seq/matrix/SRR3589961.count", sep="\t", col.names = c("gene_id","control2"))
rep1 <- read.table("/Users/chengkai/Desktop/zhuanlu_files/RNA-Seq/matrix/SRR3589960.count", sep="\t", col.names = c("gene_id","akap951"))
rep2 <- read.table("/Users/chengkai/Desktop/zhuanlu_files/RNA-Seq/matrix/SRR3589962.count", sep="\t",col.names = c("gene_id","akap952"))
# 将四个矩阵按照gene_id进行合并，并赋值给raw_count
raw_count <- merge(merge(control1, control2, by="gene_id"), merge(rep1,rep2, by="gene_id"))
# 需要将合并的raw_count进行过滤处理，里面有5行需要删除的行，在我们的小鼠的表达矩阵里面，是1,2,48823,48824,48825这5行。并重新赋值给raw_count_filter
raw_count_filt <- raw_count[-48823:-48825, ]
raw_count_filter <- raw_count_filt[-1:-2, ]
# 因为我们无法在EBI数据库上直接搜索找到ENSMUSG00000024045.5这样的基因，只能是ENSMUSG00000024045的整数，没有小数点，所以需要进一步替换为整数的形式。
# 第一步将匹配到的.以及后面的数字连续匹配并替换为空，并赋值给ENSEMBL
ENSEMBL <- gsub("\\.\\d*", "", raw_count_filter$gene_id)
row.names(raw_count_filter) <- ENSEMBL
# 去掉data 第一列
raw_count_filter <- raw_count_filter[ ,-1]
# 构建dds矩阵
# 这一步很关键，要明白condition这里是因子，不是样本名称；小鼠数据有对照组和处理组，各两个重复
condition <- factor(c(rep("control",2),rep("akap95",2)), levels = c("control","akap95"))
# 获取count数据
countData <- raw_count_filter[,1:4]
# 样本信息矩阵：第一列是样本名称，第二列是样本处理情况，即condition
colData <- data.frame(row.names=colnames(raw_count_filter), condition)
# 构建dds矩阵
dds <- DESeqDataSetFromMatrix(countData, colData, design= ~ condition)
# 查看一下dds的内容
head(dds)
# normalize 数据
dds2 <- DESeq(dds)
# 查看结果的名称，本次实验中是 "Intercept"，"condition_akap95_vs_control"
resultsNames(dds2)
# 将结果用results()函数来获取，赋值给res变量
res <- results(dds2)
# summary一下，看一下结果的概要信息
summary(res)
# 获取padj（p值经过多重校验校正后的值）小于0.05，表达倍数取以2为对数后大于1或者小于-1的差异表达基因。
table(res$padj<0.05)
res <- res[order(res$padj),]
diff_gene_deseq2 <-subset(res,padj < 0.05 & (log2FoldChange > 1 | log2FoldChange < -1))
```
####2. GO/KEGG分析及GSEA
- 2.1 安装clusterProfiler
```
source("https://bioconductor.org/biocLite.R")
biocLite("clusterProfiler")
# 看看是否安装成功
library(clusterProfiler)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-3a4e53d09a34cbe6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# 继续安装DOSE包
biocLite("DOSE")
# 安装成功
library(clusterProfiler)
```
- 2.2 安装构建自己的基因组注释数据
[Biocouductor官网](http://bioconductor.org/packages/release/BiocViews.html#___OrgDb)已经拥有了构建好的常用的19个注释数据库，包括了小鼠，人类和拟南芥等常用注释数据，可以用安装bioconductor包的方法来直接安装和载入注释数据，直接使用。
![image.png](http://upload-images.jianshu.io/upload_images/6634703-fa05bebfc9942ff0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# 载入小鼠的注释数据
biocLite("org.Mm.eg.db")
library(org.Mm.eg.db)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-131a1741a3abd9ca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# 安装AnnotationDbi
biocLite("AnnotationDbi")
# 安装成功
library(org.Mm.eg.db)
```
2.3 GO(Gene Ontology) 分析
- ID 转换函数介绍
```
keytypes(org.Mm.eg.db)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-106d46dca045f87c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```

```

