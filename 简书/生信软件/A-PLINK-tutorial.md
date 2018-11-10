> 选取89个亚洲人的Hapmap(人类基因组单体型), 大约80,000个常染色体SNP, [软件资料下载](http://zzz.bwh.harvard.edu/plink/tutorial.shtml)
####1. Getting started
- 获取文件基本信息
```
plink --file hapmap1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5a64243e9c0574cc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 发现83534变异和89个人
####2. Making a binary PED file
- 做成2进制文件为了节省空间，加速后续分析

```
# 方法一
plink --file hapmap1 --make-bed --out hapmap1
# 方法二 如果您想创建一个只包含高基因分型（至少95％完成）的新文件，您可以运行：
plink --file hapmap1 --make-bed --mind 0.05 --out highgeno
```
- 这一步会多创造三个文件
    - highgeno.bed
    - highgeno.bim
    - highgeno.fam
####3. Working with the binary PED file
```
plink --bfile hapmap1
```
- 这次读取的是上面三个二进制文件，在处理速度上大大加速
####4. Summary statistics: missing rates
- 用missing 选项来查看数据丢失率
```
plink --bfile hapmap1 --missing --out miss_stat
```
- 看下面的输出，可以发现没有人丢失，并写出了两个文件
```
Before main variant filters, 89 founders and 0 nonfounders present.
Calculating allele frequencies... done.
Total genotyping rate is 0.99441.
--missing: Sample missing data report written to miss_stat.imiss, and
variant-based missing data report written to miss_stat.lmiss.
```
- 看一下输出的两个文件
```
head miss_stat.lmiss
head miss_stat.imiss
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-01a6b29bc3bd7407.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>N_MISS 丢失个体数量
F_MISS 丢失个体比例
- 如果文件行数过多，打不开，就一条chr一条chr 写
```
plink --bfile hapmap1 --chr 1 --out res1 --missing
plink --bfile hapmap1 --chr 2 --out res2 --missing
...
```
####5. Summary statistics: allele frequencies
- 寻找等位基因频率
- 以下命令会生成一个freq_stat 文件，查看等位基因的频率
```
plink --bfile hapmap1 --freq --out freq_stat
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-167dbc4690693e50.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- --within 用于分层分析，CLST1,2 用于区分中国人和日本人
```
plink --bfile hapmap1 --freq --within pop.phe --out freq_stat
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-cfc2e7aa3b9a7214.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 如果您只是对特定的SNP感兴趣，并且想知道两个人群中的频率是多少，则可以使用--snp选项来选择这个SNP：
```
plink --bfile hapmap1 --snp rs1891905 --freq --within pop.phe --out snp1_frq_stat
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-01e87273ff421cc3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####6. Basic association analysis
- 现在我们来对所有单个SNP的疾病特征进行基本关联分析
```
plink --bfile hapmap1 --assoc --out as1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6a54c7d36dc951c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>- CHR 染色体
>- SNP 标识符
>- 编码等位基因1
>- case 频率
>- control 频率
>- 编码等位基因2
>- 卡方统计量
>- P值
>- OR值
- 看一下前关联性最大的前10个
```
sort --key=8 -nr as1.assoc | head
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-423a14f0780620d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 13 有点诡异，case 的频率大于 control
- 要获得关联结果的排序列表，还包括针对多个测试调整的一系列重要值，请使用--adjust标志：
```
plink --bfile hapmap1 --assoc --adjust --out as2
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-11bf26fa525a0417.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 调整后发现，几乎没有显著差异的
>- 染色体
>- SNP标识符
>- 未调整的p值
>- 调整后的
>- Bonferroni adjusted significance value
>- Holm step-down adjusted significance value
>- Sidak single-step adjusted significance value
>- Sidak step-down adjusted significance value
>- Benjamini & Hochberg (1995) step-up FDR control
>- Benjamini & Yekutieli (2001) step-up FDR control
####7. Genotypic and other association models
```
plink --bfile hapmap1 --model --snp rs2222162 --out mod1
plink --bfile hapmap1 --model --cell 0 --snp rs2222162 --out mod2
```
####8. Stratification analysis
```

```
