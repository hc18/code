###作业要求
1. 实现这个功能的软件也很多，还是烦请大家先自己搜索几个教程，入门请统一用htseq-count，对每个样本都会输出一个表达量文件。
2. 需要用脚本合并所有的样本为表达矩阵。参考：生信编程直播第四题：多个同样的行列式文件合并起来。
3. 对这个表达矩阵可以自己简单在excel或者R里面摸索，求平均值，方差。看看一些生物学意义特殊的基因表现如何，比如GAPDH,β-ACTIN等等。
###分析前解读
原文中人类293cell的数据只有3个（SRR3589956-58）, 缺少一个对照重复。所以后续我只分析小鼠的四个样品（SRR3589959-62）
###理论基础
- 因表达定量有以下三个水平： 
  - 基因水平
  - 转录水平
  - 外显子水平

![image.png](http://upload-images.jianshu.io/upload_images/6634703-ee98072e986d2a1c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 标准化
   - reads计数后得到的基因定量结果（count matrix），在进行不同维度的比较时需要进行不同的处理
   -  比较同一个样本(within-sample)不同基因之间的表达情况---主要考虑转录本长度的影响 
   - 比较不同样本（across-sample）同一个基因的表达情况---主要考虑测序深度的影响 
   - 标准化的算法：RPKM（SE）, FPKM（PE），TPM, TMM，RSEM等等。 
   - 标准化之后才能进行差异表达分析
####1. 下载小鼠index 文件和基因组注释文件
```
axel ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/mm10.tar.gz
axel ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_mouse/release_M10/gencode.vM10.chr_patch_hapl_scaff.annotation.gtf.gz
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-12e65af43070eb0b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####2. 序列与index比对
```
for i in `seq 59 62`
do
    hisat2 -t -x mouse/mm10/genome -1 RNA-Seq/SRR35899${i}.sra_1.fastq.gz -2 RNA-Seq/SRR35899${i}.sra_2.fastq.gz -S RNA-Seq/aligned/SRR35899${i}.sam 
done
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-04c2a4aac9a7dd74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####3. 用reads 排序bam 文件
- 先将sam 文件转成bam文件，bam 文件用 read name (-n)排序，再转回到sam文件。
```
for i in `seq 59 62`
do
    samtools view -S SRR35899${i}.sam -b > SRR35899${i}.bam
    samtools sort -n SRR35899${i}.bam -o SRR35899${i}_nsorted.bam
    samtools view -h SRR35899${i}_nsorted.bam > SRR35899${i}_count.sam
done
```
####4. HTSeq 进行基因水平的定量
#####HTSeq 详解
- htseq-count 是一款用于reads计数的软件，他能对位于基因组上的一些单位的reads数进行统计，这里所说的单位主要是指染色体上的一组位置区间（我们常见的就是gene exon）
######基本用法
***
```
htseq-count [options] <alignment_file> <gff_file>
```
1.  <alignment_file>:   比对到基因组后得到的SAM文件 （[SAMtools](http://samtools.sourceforge.net/)包含一些perl 脚本可以将大多数的比对文件转换成SAM格式 ），注意基因组mapping时一定要用支持剪接的比对软件（splicing-aware aligner）进行比对软件如TopHat.  HTSeq-count 需要用到SAM格式中的 CIGAR 区域的信息。
2.  想要通过标准输入来传入 基因组mapping得到SAM文件，用 – 替换 <alignment_file> 即可
3.  如果你是双端测序，必须要对SAM进行排序（单端可不必排序，但这里我也推荐对单端测序结果排序已减少内存消耗并提高软件效率），对read name或 染色体位置 进行排序皆可（这里我推荐按read name排序，因为通过位置排序我遇到过错误）。具体需要通过 -r 参数指定，所以排序请详见参数 -r
4.  <gff_file>:  包含单位信息的gff/GTF文件（[gff文件格式](http://gmod.org/wiki/GFF2)），大多数情况下就是指注释文件;   由于GTF文件其实就是gff文件格式的变形，在这里同样可以传入GTF格式文件。
######模型
- 如何判断一个reads属于某个基因， htseq-count 提供了union, intersection_strict, intersection_nonempty 3 种模型，如图（大多数情况下作者推荐用union模型）：
![image.png](http://upload-images.jianshu.io/upload_images/6634703-10f85c6577893ca9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######参数
- 指定输入文件的格式，<format> 可以是 sam (for text SAM files) 或 bam (for binary BAM files)格式，默认是sam.
```
-f <format>, –format=<format> ：
```
- 对于双端测序数据，必须要对SAM文件进行排序，对read name或 位置 进行排序皆可，通过 -r 可以指定您的数据是以什么方式排序的： <order> 可以是 name 或 pos ， 默认是name.
如果您的数据没有排序，可以通过samtools sort(推荐)或msort 排序， 命令：
```
-r <order>, –order=<order>
```
- 如果你指定name（按read name 排序）, htseq-count 期望输入的文件中的read pair是紧邻的2行；而指定pos (按位置排序) ，则不需要这样，进一步说，如果指定pos , 可以不排序，但这样会耗费更多的内存和效率。
```
samtools sort -n accepted_hits_unique.bam -o accepted_hits_unique_name_sorted.bam   # -n 按read name 排序 ，如果不指定则按染色体位置排序
```
- 是否这个数据是来自链特异性建库（默认 yes)
```
-s <yes/no/reverse>, –stranded=<yes/no/reverse>
```
For stranded=no, a read is considered overlapping with a feature regardless of whether it is mapped to the same or the opposite strand as the feature. For stranded=yesand single-end reads, the read has to be mapped to the same strand as the feature. For paired-end reads, the first read has to be on the same strand and the second read on the opposite strand. For stranded=reverse, these rules are reversed.
- 指定一个最低 read mapping质量值，低于<minaqual>值会被过滤掉（默认是10，0.5.4版本以前默认值是 
```
-a <minaqual>, –a=<minaqual>
```
- 指定最小计数单位类型（gff文件的第3列中的类型如： exon）, 指定后其他单位类型将被忽略（默认情况下，对于rna-seq分析采用 [Ensembl GTF](http://mblab.wustl.edu/GTF22.html) 文件类型时,默认值是：exon）。
```
-t <feature type>, --type<feature type>
```
- GFF文件的一类属性，最终的技术单位，默认情况下，对于rna-seq分析采用 [Ensembl GTF](http://mblab.wustl.edu/GTF22.html) 文件类型时,默认值是：gene_id）。
```
-i <id attribute>, --idattr=<id attribute>
```
- 判断一个reads属于某个基因的模型，用来判断统计reads的时候对一些比较特殊的reads定义是否计入。 <mode> 包括：默认的union和intersection-strict、 intersection-nonempty  （默认：union）。
```
-m <mode>, --mode=<mode>
```
- 输出所有alignment的reads到一个叫 <samout>的sam文件中，通过一个可选的sam标签 ‘ XF ’来标注每一行对应的单位和计数，可以不设置。
```
-o <samout>, --samout=<samout>
```
- 屏蔽程序报告和警告
```
-q, --quiet
```
- 打印帮助
```
-h, --help
```
***
####5. reads 计数
- 数据准备已经完成，接下来要使用htseq-count 对数据进行reads计数。
```
# 安装HTSeq
conda install HTSeq
# 语法
Usage: htseq-count [options] <sam_file> <gff_file>
```
```
mkdir -p RNA-Seq/matrix/
htseq-count RNA-Seq/aligned/SRR3589959_count.sam mouse/gencode.vM10.annotation.gtf > RNA-Seq/matrix/SRR3589959.count
htseq-count RNA-Seq/aligned/SRR3589960_count.sam mouse/gencode.vM10.annotation.gtf > RNA-Seq/matrix/SRR3589960.count
htseq-count RNA-Seq/aligned/SRR3589961_count.sam mouse/gencode.vM10.annotation.gtf > RNA-Seq/matrix/SRR3589961.count
htseq-count RNA-Seq/aligned/SRR3589962_count.sam mouse/gencode.vM10.annotation.gtf > RNA-Seq/matrix/SRR3589962.count
```
- 我是分四个终端一起跑，相当于四个进程同时跑
![image.png](http://upload-images.jianshu.io/upload_images/6634703-7877c0e990b6739d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 最后生成四个文件
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f0d9def2badf585c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- count文件的格式：基因名一列（ENSMUSG00000000001.4）+reads计数一列(1648)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-fd40e57b62e9af19.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####6. 合并表达矩阵
- 使用R将这四个文件进行合并（59 和 61 是对照， 60和62是处理），得到最后的融合表达矩阵，R语言代码如下
```
options(stringsAsFactors = FALSE)
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
# 将ENSEMBL重新添加到raw_count_filter矩阵
row.names(raw_count_filter) <- ENSEMBL
# 看一些基因的表达情况，在UniProt数据库找到AKAP95的id，并从矩阵中找到访问，并赋值给AKAP95变量
AKAP95 <- raw_count_filter[rownames(raw_count_filter)=="ENSMUSG00000024045",]
# 查看AKAP95
AKAP95
```
####7. 简单分析 
- 合并后的数据框
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b3261a847b049c30.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- AKAP95 处理组明显比对照组高，说明这个基因在小鼠的表达量变高
![image.png](http://upload-images.jianshu.io/upload_images/6634703-3f6b02cbf267fc59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 总的概况
![image.png](http://upload-images.jianshu.io/upload_images/6634703-29bb15297d0a7275.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####8. 参考文献
1. http://www.jianshu.com/p/e9742bbf83b9 （hoptop 大神）
2. http://www.jianshu.com/p/24cf44b610a7  （lxmic 大神）
3. http://fbb84b26.wiz03.com/share/s/3XK4IC0cm4CL22pU-r1HPcQQ3ouv263iAk012b-9tU2UXRgt（青山屋主大神）
####bingo,祝君好运~!


