####1. 软件准备
![image.png](https://upload-images.jianshu.io/upload_images/6634703-34689c9803663678.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. 使用TASSEL 软件进行基因填补
- 打开tassel 软件
```
java -jar /Users/chengkai/Documents/01_NMR/003GWAS/GWAShandbook/software/tassel_v5/sTASSEL.jar
```
- 导入数据用KNN填补（Impute -- LD KNNi Imputation）
![填补前](https://upload-images.jianshu.io/upload_images/6634703-88aa9ba575efec1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![填补后](https://upload-images.jianshu.io/upload_images/6634703-f7fac80ccc338128.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 命令行参数（用于服务器运行）
```
perl run_pipeline.pl -Xms512m -Xmx5g -importGuess test.vcf -LDKNNiImputationPlugin -highLDSSites 50 - knnTaxa 5 -maxLDDistance 100000000 -endPlugin -export test.imputed.vcf -exportType VCF
```
####3. STRUCTURE与Admixture的使用方法
######3.1 按第二等位基因频率(minor allele frequency，MAF)和缺失率(missing rate)过滤
```
# maf 0.05 第二等位基因大于0.05
# geno 0.1 基因缺失率大于0.1
# recode 转出和vcf 一样的文件
# 产生test.impute.maf0.05.int0.9.vcf文件
plink --vcf ../data/test.impute.vcf --maf 0.05 --geno 0.1 --recode vcf-iid --out test.impute.maf0.05.int0.9 --allow-extra-chr
```
- less test.impute.maf0.05.int0.9.vcf 
![image.png](https://upload-images.jianshu.io/upload_images/6634703-b7a4848ce485e444.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- cat test.impute.maf0.05.int0.9.log
![总共20000，筛出19819](https://upload-images.jianshu.io/upload_images/6634703-5d98b124a39c6376.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######3.2 依据LD对标记进行筛选
- 产生test.impute.maf0.05.int0.9.prune.in和test.impute.maf0.05.int0.9.prune.out文件，in表示入选的标记，out表示被去除的标记，两个文件都只有 标记的ID
```
plink --vcf test.impute.maf0.05.int0.9.vcf --indep-pairwise 50 10 0.2 --out test.impute.maf0.05.int0.9 --allow-extra-chr
```
- 19819 删除了13569
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9acae4408e5da1ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######3.3 筛选结果的提取
```
plink --vcf test.impute.maf0.05.int0.9.vcf --make-bed --extract test.impute.maf0.05.int0.9.prune.in --out test.impute.maf0.05.int0.9.prune.in
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5d302b977782678e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 筛选后的数据可以转回vcf格式
```
plink --bfile test.impute.maf0.05.int0.9.prune.in --recode vcf-iid --out test.impute.maf0.05.int0.9.prune.in
```
######3.4 将筛选后的基因型转换为structure格式和admixture数据格式
```
../software/plink -bfile test.impute.maf0.05.int0.9.prune.in --recode structure --out test.impute.maf0.05.int0.9.prune.in
../software/plink -bfile test.impute.maf0.05.int0.9.prune.in --recode 12 --out test.impute.maf0.05.int0.9.prune.in
```
- test.impute.maf0.05.int0.9.prune.in.recode.strct_in为structure输入文件
- test.impute.maf0.05.int0.9.prune.in.ped为Admixture输入文件
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6b86dedd47f99794.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4 structure 软件使用
- mainparams 文件配置
```
#define OUTFILE struct/K2_result
#define INFILE test.impute.maf0.05.int0.9.prune.in.recode.strct_in
#define NUMINDS 300
#define NUMLOCI 6250
#define LABEL 1
#define POPDATA 1 
#define POPFLAG 0 
#define LOCDATA 0 
#define PHENOTYPE 0 
#define MARKERNAMES 1 
#define MAPDISTANCES 1 
#define ONEROWPERIND 1 
#define PHASEINFO 0 
#define PHASED 0
#define RECESSIVEALLELES 0 
#define EXTRACOLS 0 
#define MISSING 0
#define PLOIDY 2
#define MAXPOPS 2
#define BURNIN 50000
#define NUMREPS 500000 
#define RANDOMIZE 0
#define SEED 15
#define NOADMIX 0
#define LINKAGE 0
#define USEPOPINFO 0
#define LOCPRIOR 0
#define INFERALPHA 1
#define ALPHA 1.0
#define POPALPHAS 0
#define UNIFPRIORALPHA 1 
#define ALPHAMAX 10.0 
#define ALPHAPROPSD 0.025 
#define FREQSCORR 1
#define ONEFST 0
#define FPRIORMEAN 0.01 
#define FPRIORSD 0.05
#define INFERLAMBDA 0 
#define LAMBDA 1.0
#define COMPUTEPROB 1 
#define PFROMPOPFLAGONLY 0 
#define ANCESTDIST 0
#define STARTATPOPINFO 0 
#define METROFREQ 10
#define UPDATEFREQ 1
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-be0012ec1fdc7128.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
../software/structure -m mainparams -e extraparams
```
- 1,2,3,4,5,6 每个k 重复5次找最优的k
![image.png](https://upload-images.jianshu.io/upload_images/6634703-c42aa517ec7f0aa8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####5. STRUCTURE与Admixture的结果整理

1. 判断最优的K值
- [去网站找最优的K](http://taylor0.biology.ucla.edu/structureHarvester/completedJobs/icy-haze-10df/summary.html)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-32498cd1355db386.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![最好的点是k=2](https://upload-images.jianshu.io/upload_images/6634703-ff905404448e8577.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

 ```
# R 代码
devtools::install_github('royfrancis/pophelper')
library(pophelper) 
setwd("/Users/chengkai/Documents/01_NMR/003GWAS/GWAShandbook/structure_data/")
file_list <- list.files(path = "structure_output/", full.names = T)
qlist <- readQ(file_list)
evannoMethodStructure(summariseQ(tabulateQ(qlist)), exportplot=T,writetable=T,na.rm=T, imgtype = "pdf")
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-fb75e4b96f62fe4b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-946aeaa67142b98d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
file_list2 <- list.files("pop-both", pattern = "merge", full.names = T)
qlist2 <- readQ(file_list2)
##所有的K值结果画在一起
plotQ(qlist2[c(2:9,1)], sortind = "all", imgtype = "pdf", ordergrp = F, imgoutput = "join", width = 15, outputfilename = paste0("structure_barplot"), showindlab=F, indlabsize = 0.5, indlabheight = 0.1)
##画指定K值的结果
plotQMultiline(qlist2[9], imgtype = "pdf", sortind = "all", useindlab = T, width = 80, height = 15, indlabsize = 6, spl = 453)
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-7b1b8523dcc4b5dd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
