####序章
- “差异”是个统计学概念，获取差异表达基因就要用统计方法，R的统计功能很强大，适合做这样的事情。用前面的方法读取数据：
```
library(affy)
library(tcltk)
filters <- matrix(c("CEL file", ".[Cc][Ee][Ll]", "All", ".*"), ncol = 2, byrow = T)
cel.files <- tk_choose.files(caption = "Select CELs", multi = TRUE,
                             filters = filters, index = 1)
data.raw <- ReadAffy(filenames = cel.files)
n.cel <- length(cel.files)
# 查看样品名称
sampleNames(data.raw)

# 简化一下名称，设置pData
sampleNames(data.raw)  <- paste("S",1:n.cel, sep='')
pData(data.raw)$treatment <- rep(c("0h", "1h", "24h", "7d"), each=2)
pData(data.raw)

# 使用rma和mas5方法进行预处理：
eset.rma <- rma(data.raw)
eset.mas5 <- mas5(data.raw)
```
####1. 计算基因表达量
- 很简单，用一个exprs函数就可以从eset数据中提取出表达量，得到的数据类型是矩阵。但是应该注意rma的eset结果是经过对数变换的，而mas5的eset结果是原始信号强度。虽然表达量是用对数变换的信号值表示的，但是有些计算过程要用到未经变换的原始值，应该把它们都计算出来：
```
> emat.rma.log2 <- exprs(eset.rma)
> emat.mas5.nologs <- exprs(eset.mas5)
> class(emat.rma.log2)
[1] "matrix"
> head(emat.rma.log2, 1)
               S1       S2       S3       S4       S5       S6       S7      S8
244901_at 4.04049 4.348442 4.047649 4.051616 4.019483 3.962069 4.030375 4.06245
> head(emat.mas5.nologs, 1)
                S1       S2       S3       S4       S5       S6       S7       S8
244901_at 39.78854 94.94076 57.35433 60.22522 61.08426 55.57075 53.95297 85.98412
> emat.rma.nologs <- 2^emat.rma.log2
> emat.mas5.log2 <- log2(emat.mas5.nologs)
```
- 下面我们仅使用rma的结果做演示。计算平均表达量和差异表达倍数（和0h对照比）：
```
> rm(eset.mas5)
> rm(emat.mas5.nologs)
> rm(emat.mas5.log2)
> #计算平均值，并做对数转换
> results.rma <- data.frame((emat.rma.log2[,c(1,3,5,7)] + emat.rma.log2[,c(2,4,6,8)])/2)
> #计算表达量差异倍数
> results.rma$fc.1h <- results.rma[,2]-results.rma[,1]
> results.rma$fc.24h <- results.rma[,3]-results.rma[,1]
> results.rma$fc.7d <- results.rma[,4]-results.rma[,1]
> head(results.rma, 2)
                S1       S3       S5       S7      fc.1h     fc.24h      fc.7d
244901_at 4.194466 4.049632 3.990776 4.046412 -0.1448335 -0.2036901 -0.1480534
244902_at 4.292817 4.158843 4.061261 3.937140 -0.1339739 -0.2315562 -0.3556771
```
- 用逻辑向量取子集::比如我们要选取results.rma中fc.7d大于0的所有行，分两步：先产生一个逻辑向量，然后用这个逻辑向量取子集，也可以一步完成。
```
subset.logic <- results.rma$fc.7d>0
subset.data <- results.rma[subset.logic,]
length(subset.logic); nrow(results.rma)
head(subset.logic)
```
####2. 选取“表达”基因
- 选取“表达”基因的方法常见的有两种，一是使用genefilter软件包，另外一种是调用affy包的mas5calls()函数。使用 genefilter需要设定筛选阈值，不同的人可能有不同的标准.mas5calls方法使用探针水平数据（AffyBatch类型数据）进行处理，一般使用没经过预处理的芯片数据通用性强些，其他参数用默认就可以：
```
> data.mas5calls <- mas5calls(data.raw)
Getting probe level data...
Computing p-values
Making P/M/A Calls
```
- 继续用exprs计算“表达”量，得到的数据只有三个值P/M/A。对于这三个值的具体解释可以用?mas5calls查看帮助。P为present，A为absent，M为marginal（临界值）。
```
> eset.mas5calls <- exprs(data.mas5calls)
> head(eset.mas5calls)
          S1  S2  S3  S4  S5  S6  S7  S8 
244901_at "A" "P" "P" "A" "P" "P" "A" "P"
244902_at "A" "P" "P" "M" "A" "A" "P" "A"
244903_at "P" "P" "P" "P" "P" "P" "P" "P"
244904_at "A" "A" "A" "A" "A" "A" "A" "A"
244905_at "A" "A" "A" "A" "A" "A" "A" "A"
244906_at "A" "A" "A" "A" "A" "A" "A" "A"
```
- 下面我们把至少一个芯片中有表达的基因选出来：从22810中选出了16005个。
```
> AP <- apply(eset.mas5calls, 1, function(x)any(x=="P"))
> present.probes <- names(AP[AP])
> paste(length(present.probes),"/",length(AP))
[1] "16005 / 22810"
```
```
# 删掉一些中间数据很必要
rm(data.mas5calls)
rm(eset.mas5calls)
# present.probes是名称向量，用它进行数据子集提取
results.present <- results.rma[present.probes,]
```
####3. 获取差异表达基因
- 生物学数据分析时的"差异"应该有两个意思，一是统计学上的差异，另外一个是生物学上的差异。一个基因在两个条件下的表达量分别有3个测量值：99,100,101 和 102,103,104。统计上两种条件下的基因表达数值是有差异的，后者比前者表达量要大。但生物学上有意义吗？未必。按平均值计算表达变化上升了3%，能产生什么样的生物学效应？这得看是什么基因了。所以差异表达基因的选取一般设置至少两个阈值：基因表达变化量和统计显著性量度（p值、q值等）。
######3.1 简单t-测验
- 这种方法不用太多的统计学知识，生物专业的人很容易想到，而且确实有不少人在用。经常使用的筛选阈值是表达量变化超过2倍，即|log2(fc)|>=log(2)。先简单看看有没有：
```
> apply(abs(results.present[,5:7]), 2, max)
   fc.1h   fc.24h    fc.7d 
5.309234 6.688065 6.844233 
```
- 表达变化超过2倍的基因共有842个：
```
> sum(abs(results.present[,"fc.7d"])>=log2(2))
[1] 842
```
- 选出这842个基因：
```
results.st <- results.present[abs(results.present$fc.7d)>=log2(2),]
sel.genes <- row.names(results.st)
```
- t测验，并选出p<0.05的差异表达基因：
```
> p.value <- apply(emat.rma.log2[sel.genes,], 1, function(x){t.test(x[1:2], x[7:8])$p.value})
> results.st$p.value <- p.value
> names(results.st)
[1] "S1"      "S3"      "S5"      "S7"      "fc.1h"   "fc.24h"  "fc.7d"   "p.value"
```
```
> results.st <- results.st[, c(1,4,7,8)]
> results.st <- results.st[p.value<0.05,]
> head(results.st, 2)
                S1       S7    fc.7d    p.value
245042_at 8.153410 7.020710 -1.13270 0.01004456
245088_at 7.040988 5.418848 -1.62214 0.03380786
```
- 通过简单t测验方法得到347个表达倍数变化超过2倍的差异表达基因。
```
> nrow(results.st)
[1] 347
```
######3.2 Wilcoxon's signed-rank test
- 这个方法发表在 Liu, W.-m. et al, Analysis of high density expression microarrays with signed-rank call algorithms. Bioinformatics, 2002, 18, 1593-1599。R软件包simpleaffy的detection.p.val函数有实现，可以通过pairwise.comparison函数调用：
```
library(simpleaffy)
#注意下面语句中的数据顺序
sa.fit <- pairwise.comparison(eset.rma, "treatment", c("7d", "0h"))
```
- pairwise.comparison返回的数据为simpleaffy自定义的"PairComp"类型，提取数据要用它专门的函数：平均值用means函数获得，变化倍数（log2）用fc函数获得，t测验的p值用tt函数获得：
```
> class(sa.fit)
[1] "PairComp"
attr(,"package")
[1] "simpleaffy"
> results.sa <- data.frame(means(sa.fit), fc(sa.fit), tt(sa.fit))
> #选择有表达的基因
> results.sa <- results.sa[present.probes,]
> head(results.sa, 2)
               X7d      X0h fc.sa.fit. tt.sa.fit.
244901_at 4.046502 4.202667 -0.1561655 0.43981642
244902_at 3.937869 4.294883 -0.3570136 0.05824285
> colnames(results.sa) <- c("7d", "0h", "fold.change", "p.val")
> head(results.sa, 2)
                7d       0h fold.change      p.val
244901_at 4.046502 4.202667  -0.1561655 0.43981642
244902_at 3.937869 4.294883  -0.3570136 0.05824285
```
- 应用表达倍数筛选得到表达倍数超过2倍的基因数量有862个，应用p值筛选后得到562个差异表达基因：
```
> results.sa <- results.sa[abs(results.sa$fold.change)>=log2(2), ]; nrow(results.sa)
[1] 862
> results.sa <- results.sa[results.sa$p.val<0.05,]; nrow(results.sa)
[1] 562
```
######3.4 Moderated T statistic
- 这种方法在R软件包limma里面实现得最好。limma最初主要用于双色（双通道）芯片的处理，现在不仅支持单色芯片处理，新版还添加了对RNAseq数据的支持，很值得学习使用。安装方法同前面其他Bioconductor软件包的安装。载入limm软件包后可以用limmaUsersGuide()函数获取pdf格式的帮助文档。
- limma的功能很多，这里只看看差异表达基因的分析流程，具体算法原理请参考limma在线帮助和这篇文献：Smyth G K. Linear models and empirical bayes methods for assessing differential expression in microarray experiments[J]. 
- limma需要先产生一个design矩阵，用于描述RNA样品：
```
> treatment <- factor(pData(eset.rma)$treatment)
> design <- model.matrix(~ 0 + treatment)
> colnames(design) <- c("C0h", "T1h", "T24h", "T7d")
> design
  C0h T1h T24h T7d
1   1   0    0   0
2   1   0    0   0
3   0   1    0   0
4   0   1    0   0
5   0   0    1   0
6   0   0    1   0
7   0   0    0   1
8   0   0    0   1
attr(,"assign")
[1] 1 1 1 1
attr(,"contrasts")
attr(,"contrasts")$treatment
[1] "contr.treatment"
```
- 可以看到：矩阵的每一行代表一张芯片，每一列代表一种RNA来源（或处理）。此外，你可能还需要另外一个矩阵，用来说明你要进行哪些样品间的对比分析：
```
> contrast.matrix <- makeContrasts(T1h-C0h, T24h-C0h, T7d-C0h, levels=design)
> contrast.matrix
      Contrasts
Levels T1h - C0h T24h - C0h T7d - C0h
  C0h         -1         -1        -1
  T1h          1          0         0
  T24h         0          1         0
  T7d          0          0         1
```
- 下一步建立线性模型，并进行分组比较和p值校正：
```
fit <- lmFit(eset.rma[present.probes,], design)
fit2 <- contrasts.fit(fit, contrast.matrix)
fit2 <- eBayes(fit2)
```
- 先统计一下数量。可以看到：对于T7d-C0h比较组（coef=3），表达变化超过2倍（lfc参数）的基因数为842个，而变化超过2倍、p<0.05的基因总数为740个：
```
> nrow(topTable(fit2, coef=3, adjust.method="fdr", lfc=1, number=30000))
[1] 842
> nrow(topTable(fit2, coef=3, adjust.method="fdr", p.value=0.05, lfc=1, number=30000))
[1] 740
```
- 把toTable函数的返回结果存到其他变量就可以了，它是数据框类型数据，可以用write或write.csv函数保存到文件：
```
> results.lim <- topTable(fit2, coef=3, adjust.method="fdr", p.value=0.05, lfc=1, number=30000)
> class(results.lim)
[1] "data.frame"
> head(results.lim)
              logFC   AveExpr         t      P.Value    adj.P.Val         B
254818_at  6.215048 10.363131  41.37718 7.303865e-10 1.168984e-05 11.537789
254805_at  6.844233  7.280364  30.81357 6.095156e-09 4.877648e-05 10.431352
245998_at  2.777596 10.010953  25.44024 2.410520e-08 9.545438e-05  9.527827
265119_at  4.380304  8.281855  24.06503 3.588353e-08 9.545438e-05  9.240001
256114_at  4.461129  7.668175  23.92133 3.745465e-08 9.545438e-05  9.208321
265722_at -2.912644  9.275506 -23.90851 3.759850e-08 9.545438e-05  9.205480
```
>为什么以上几种方法仅用表达倍数（2倍）筛选得到的数字不大一样？limma和直接计算的结果都是842个，而simpleaffy和SAM为862/861个。这是对eset信号值取对数和求平均值的先后导致的，limma先取对数再求平均值，而simpleaffy和SAM是先求平均值再取对数。
####4. 保存数据，下次使用
```
#所有表达基因的名称
write(present.probes, "genes.expressed.txt")
#处理7天的差异表达基因
write.csv(results.lim, "results.lim.7d.csv")
#emat.rma.log2
write.csv(emat.rma.log2[present.probes,], "emat.rma.log2.csv")
```
- 如果要全部结果：
```
> results.lim.all <- topTable(fit2, coef=1:3, adjust.method="fdr", p.value=1, lfc=0, number=30000)
> head(results.lim.all, 3)
            T1h...C0h T24h...C0h T7d...C0h   AveExpr         F      P.Value    adj.P.Val
254818_at  0.34085176   6.023600  6.215048 10.363131 1047.9758 6.703708e-10 1.072929e-05
245998_at -0.13674890   3.675797  2.777596 10.010953  630.2975 4.191638e-09 3.025400e-05
265119_at -0.02535532   6.061235  4.380304  8.281855  579.5578 5.670853e-09 3.025400e-05
```
```
> ## 仅保存logFC供后面的分析使用
> results.lim.all <- results.lim.all[, 1:3]
> colnames(results.lim.all) <- c('T1h', 'T24h', 'T7d')
> head(results.lim.all, 3)
                  T1h     T24h      T7d
254818_at  0.34085176 6.023600 6.215048
245998_at -0.13674890 3.675797 2.777596
265119_at -0.02535532 6.061235 4.380304
```
```
> write.csv(results.lim.all, 'results.lim.all.csv')
```
####参考文献
1. http://blog.csdn.net/u014801157/article/details/24372385


