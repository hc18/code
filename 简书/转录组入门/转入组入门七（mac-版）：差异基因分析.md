####任务
-  差异基因分析这个步骤推荐在R里面做，载入表达矩阵，然后设置好分组信息，统一用DEseq2进行差异分析，当然也可以走走edgeR或者limma的voom流程。基本任务是得到差异分析结果，进阶任务是比较多个差异分析结果的异同点。[生信技能树](http://www.biotrainee.com/thread-1748-1-1.html)
######1. 读取表达矩阵
```
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
raw_count_filter <- raw_count_filter[ ,-1]
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-da0a7aa554f8596d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

######2. DESeq2 
```
# 下载DESeq2
source("https://bioconductor.org/biocLite.R")
biocLite("GenomeInfoDb")
```
- DESeq2 对于输入数据的要求
  1. DEseq2要求输入数据是由整数组成的矩阵。
  2. DESeq2要求矩阵是没有标准化的。
- DESeq2进行差异表达分析
  - DESeq2包分析差异表达基因简单来说只有三步：构建dds矩阵，标准化，以及进行差异分析。
```
dds <- DESeqDataSetFromMatrix(countData = cts, colData = coldata, design= ~ batch + condition) #~在R里面用于构建公式对象，~左边为因变量，右边为自变量。
dds <- DESeq(dds) #标准化
res <- results(dds, contrast=c("condition","treated","control")) #差异分析结果
```
######3. 构建dds矩阵
- ***表达矩阵：***即上述代码中的countData，就是我们前面通过read count计算后并融合生成的矩阵，行为各个基因，列为各个样品，中间为计算reads或者fragment得到的整数。

- ***样品信息矩阵：***即上述代码中的colData，它的类型是一个dataframe（数据框），第一列是样品名称，第二列是样品的处理情况（对照还是处理等），即condition，condition的类型是一个factor。
- ***差异比较矩阵：*** 即上述代码中的design。 差异比较矩阵就是告诉差异分析函数是要从要分析哪些变量间的差异，简单说就是说明哪些是对照哪些是处理。
```
# 这一步很关键，要明白condition这里是因子，不是样本名称；小鼠数据有对照组和处理组，各两个重复
> condition <- factor(c(rep("control",2),rep("akap95",2)), levels = c("control","akap95"))
# 获取count数据
> countData <- raw_count_filter[,1:4]
> colData <- data.frame(row.names=colnames(raw_count_filter), condition)
> dds <- DESeqDataSetFromMatrix(countData, colData, design= ~ condition)
# 查看一下dds的内容
> head(dds)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-712359e982854e80.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######4. DESeq标准化dds
```
# normalize 数据
> dds2 <- DESeq(dds)
# 查看结果的名称，本次实验中是 "Intercept"，"condition_akap95_vs_control"
> resultsNames(dds2)
# 将结果用results()函数来获取，赋值给res变量
res <- results(dds2)
# summary一下，看一下结果的概要信息
summary(res)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d5661f5bc0563a7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######5. 提取差异分析结果
```
# 获取padj（p值经过多重校验校正后的值）小于0.05，表达倍数取以2为对数后大于1或者小于-1的差异表达基因。
> table(res$padj<0.05)
> res <- res[order(res$padj),]
> diff_gene_deseq2 <-subset(res,padj < 0.05 & (log2FoldChange > 1 | log2FoldChange < -1))
> diff_gene_deseq2 <- row.names(diff_gene_deseq2)
> resdata <-  merge(as.data.frame(res),as.data.frame(counts(dds2,normalize=TRUE)),by="row.names",sort=FALSE)
# 得到csv格式的差异表达分析结果
> write.csv(resdata,file= "control_vs_akap95.cvs",row.names = F)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-69a8f60884646493.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######6. 参考文献
1. https://zhuanlan.zhihu.com/p/30350531（青山屋主）
2. http://www.jianshu.com/p/3bfb21d24b74 （lxmic）
3. http://www.bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html （DESeq2 官网） 

 
