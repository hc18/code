####序章
- 基因列表的分析一般都会涉及GO和KEGG分析，Bioconductor提供了很多这方面的R工具包。
- 选择工作目录，读入上一次分析和保存的数据：
```
> results.sig <- read.csv("results.lim.7d.csv", header=TRUE, as.is=TRUE)
> head(results.sig)
          X     logFC   AveExpr         t      P.Value    adj.P.Val         B
1 254818_at  6.215048 10.363131  41.37718 7.303865e-10 1.168984e-05 11.537789
2 254805_at  6.844233  7.280364  30.81357 6.095156e-09 4.877648e-05 10.431352
3 245998_at  2.777596 10.010953  25.44024 2.410520e-08 9.545438e-05  9.527827
4 265119_at  4.380304  8.281855  24.06503 3.588353e-08 9.545438e-05  9.240001
5 256114_at  4.461129  7.668175  23.92133 3.745465e-08 9.545438e-05  9.208321
6 265722_at -2.912644  9.275506 -23.90851 3.759850e-08 9.545438e-05  9.205480
```
```
colnames(results.sig)[1] <- "probe_id" ;
genes.sig <- results.sig[, 1]
```
####1 获取AGI、GO和KEGG注释
```
source("https://bioconductor.org/biocLite.R")
biocLite("ath1121501.db")
```
```
> library(org.At.tair.db)
> library(ath1121501.db)
> ls("ath1121501.db")
> ls("package:ath1121501.db")
 [1] "ath1121501"             "ath1121501_dbconn"      "ath1121501_dbfile"     
 [4] "ath1121501_dbInfo"      "ath1121501_dbschema"    "ath1121501.db"         
 [7] "ath1121501ACCNUM"       "ath1121501ARACYC"       "ath1121501ARACYCENZYME"
[10] "ath1121501CHR"          "ath1121501CHRLENGTHS"   "ath1121501CHRLOC"      
[13] "ath1121501CHRLOCEND"    "ath1121501ENTREZID"     "ath1121501ENZYME"      
[16] "ath1121501ENZYME2PROBE" "ath1121501GENENAME"     "ath1121501GO"          
[19] "ath1121501GO2ALLPROBES" "ath1121501GO2PROBE"     "ath1121501MAPCOUNTS"   
[22] "ath1121501ORGANISM"     "ath1121501ORGPKG"       "ath1121501PATH"        
[25] "ath1121501PATH2PROBE"   "ath1121501PMID"         "ath1121501PMID2PROBE"  
[28] "ath1121501SYMBOL" 
```
- ath1121501GO为拟南芥基因的GO数据库，ath1121501PATH为KEGG pathway数据库。但不是每一个基因（probeset）都有GO或KEGG注释，哪些基因有注释可以用mappedkeys函数获得：
```
> length(mappedkeys(ath1121501PATH))
[1] 3018
> length(mappedkeys(ath1121501GO))
[1] 20170
> head(mappedkeys(ath1121501PATH))
[1] "245035_at" "245037_at" "245060_at" "245076_at" "245086_at" "245089_at"
```
- 有PATH注释的probesets只有3018个，而有GO注释的有2万多个。
- 通过ath1121501XXXX获得的数据是AnnotationDbi软件包定义的ProbeAnnDbBimap类型数据，它们可以用as.list转成列表形式。列表内每一个基因的注释内容也是列表形式：
```
> all.path <- ath1121501PATH[mappedkeys(ath1121501PATH)]
> class(all.path)
[1] "ProbeAnnDbBimap"
attr(,"package")
[1] "AnnotationDbi"
> as.list(all.path)[1]
$`245035_at`
[1] "00270" "01100"
```
- 转换成列表类型的ProbeAnnDbBimap数据仍然是列表，但PATH和ACCNUM数据是二级列表（列表下只有一级列表），而GO数据是三级列表（列表下还有两级的列表）。所以得先编写get.GO函数，它把as.list产生的GO三级列表转成二级结构，和AGI和KEGG的列表类似，方便后面的统一处理：
```
get.GO <- function(the.keys, goList){
        results <- NULL
        for (i in 1:length(the.keys)){
                n <- length(goList[[i]])
                info <- NULL
                for(j in 1:n){info <- c(info, goList[[i]][[j]]$GOID)}
                info <- list(info)
                names(info) <- the.keys[i]
                results <- c(results, info)
        }
        results
}
```
- 使用这个函数和下列代码就可以获得AGI、GO和KEGG注释：
```
library(plyr)
results.anno <- results.sig[,1:2]
for(i in 1:3){
    anno <- switch(i, ath1121501ACCNUM, ath1121501GO, ath1121501PATH)
    anno.label <- switch(i, "AGI", "GO", "PATH")
    mapped.probes <- mappedkeys(anno)
    mapped.present <- intersect(genes.sig, mapped.probes)
    mapped.anno <- as.list(anno[mapped.present])
    if(anno.label=="GO") mapped.anno <- get.GO(mapped.present, mapped.anno)
        mapped.anno <- llply(mapped.anno, unique)
    mapped.anno <- ldply(mapped.anno, paste, collapse="; ")
    colnames(mapped.anno) <- c("probe_id", anno.label)
    results.anno <- merge(results.anno, mapped.anno, by.x = "probe_id", all = TRUE)
}
```
- 上面代码有两点要注意：
    - switch()函数使用。switch()是非常神奇的条件转向开关函数，它的参数（列表）可以是各种类型，变量、表达式、函数等都可以使用。
    - 列表到数据框类型数据的转换，我们使用了plyr软件包的llply和ldply函数。plyr是很著名的软件包，用于数据糅合。这不属于本节的讨论范围，先不介绍，请自行学习使用。
- 由于探针id是唯一的，上面的代码用它作为关键字糅合数据。得到的结果是数据框：
```
> str(results.anno)
'data.frame':	740 obs. of  5 variables:
 $ probe_id: chr  "245015_at" "245042_at" "245088_at" "245196_at" ...
 $ logFC   : num  1.37 -1.13 -1.62 -1.71 1.44 ...
 $ AGI     : chr  "ATCG00490" "AT2G26540" "AT2G39850" "AT1G67750" ...
 $ GO      : chr  "GO:0006091; GO:0006354; GO:0009737; GO:0015977; GO:0015979; GO:0018119; GO:0046686; GO:0005618; GO:0009507; GO:"| __truncated__ "GO:0006779; GO:0006780; GO:0009507; GO:0004852" "GO:0006508; GO:0008152; GO:0005576; GO:0009505; GO:0004252" "GO:0005576; GO:0030570" ...
 $ PATH    : chr  NA NA NA "00040" ...
```
- 这样每一个探针都得到了对应的AGI、GO和KEGG途径注释（如果有）。其他类型数据如Pubmed ID可以使用类似方法获得，但编程之前得先了解它们的数据结构，最直接的方法就是使用head，summary和str等函数查看。
- 得到的结果用write.csv或其他存盘函数保存。
####2. GO和KEGG富集分析
- Bioconductor中有不少软件包可以进行GO和KEGG统计分析和作图，如GOstats和KEGGgraph，但我不建议使用它们。
- 对于这类分析，我推荐使用另外一个不是R软件包的网络分析软件：Cytoscape。它是免费的开源软件，由多所大学和几个公司联合开发和维护，已经逐渐成为网络分析的标准工具，软件网址为：[http://www.cytoscape.org/](http://www.cytoscape.org/)
- R软件包RCytoscape可以把R的分析结果推送到Cytoscape，充分利用R的统计功能和Cytoscape的可视化能力。但是RCytoscape不一定能跟上Cytoscape的软件更新步伐，所以最好还是把R分析的结果保存成文件，再用Cytoscape直接分析。
- 事实上，如果使用Cytoscape进行GO和KEGG富集或网络分析，我们只需要获得AGI列表，而不需要获得GO和KEGG注释。
####参考文献
1. http://blog.csdn.net/u014801157/article/details/24372393
