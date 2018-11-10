####1. GOALS
- To learn how to use VCFtools to filter a VCF file for missing data, genotype depth, locus quality score, minor allele frequency, and genotype call depth
- To learn how to use vcflib to filter FreeBayes VCF files generated with RAD data
- To filter a VCF file for HWE within populations
- How to decompose a VCF into SNPs and INDELs and
- How to use a haplotyping script to further filter SNPs for paralogs and genotyping errors.
####2. 材料准备
```
mkdir filtering
cd filtering
wget https://www.dropbox.com/sh/bf9jxviaoq57s5v/AAD2Kv5SPpHlZ7LC7sBz4va8a?dl=1
unzip FilterData.zip
ChengkaideMacBook-Pro:filtering chengkai$ ls -lhrt
total 331240
-rwxr--r--@ 1 chengkai  staff    65M Mar  6  2015 raw.vcf.gz
-rwxr--r--@ 1 chengkai  staff   134K Mar  6  2015 stats.out
-rwxr--r--@ 1 chengkai  staff   1.0M Mar  6  2015 reference.fasta.ann
-rwxr--r--@ 1 chengkai  staff   1.0M Mar  6  2015 reference.fasta.amb
-rwxr--r--@ 1 chengkai  staff   6.5M Mar  6  2015 reference.fasta
-rwxr--r--@ 1 chengkai  staff   3.0M Mar  6  2015 reference.fasta.sa
-rwxr--r--@ 1 chengkai  staff   1.5M Mar  6  2015 reference.fasta.pac
-rwxr--r--@ 1 chengkai  staff   954K Mar  6  2015 reference.fasta.fai
-rwxr--r--@ 1 chengkai  staff   345K Mar  6  2015 reference.fasta.clstr
-rwxr--r--@ 1 chengkai  staff   6.1M Mar  6  2015 reference.fasta.bwt
-rwxr--r--@ 1 chengkai  staff   107K Mar  6  2015 BR_004-RG.bam
-rwxr--r--@ 1 chengkai  staff   242K Mar  6  2015 BR_004-RG.bam.bai
-rwxr--r--@ 1 chengkai  staff   399B Mar  6  2015 popmap
-rwxr--r--@ 1 chengkai  staff   117K Mar  6  2015 BR_006-RG.bam
-rwxr--r--@ 1 chengkai  staff   242K Mar  6  2015 BR_006-RG.bam.bai
-rw-r--r--@ 1 chengkai  staff    75M Jul 27 12:28 FilterData.zip
drwxr-xr-x@ 3 chengkai  staff   102B Jul 27 12:31 __MACOSX
``` 
####3. 过滤
######3.1 过滤至少50%的个体成功被snp calling的位点，最低质量分数为30的位点，次要等位基因计数为3的位点。
```
vcftools --gzvcf raw.vcf.gz --max-missing 0.5 --mac 3 --minQ 30 --recode --recode-INFO-all --out raw.g5mac3
```
> --max-missing 0.5 过滤完整度低于50%的基因
> --mac 3 过滤次要等位基因小于3的
> --minQ 30 只要质量高于30的
> --recode-INFO-all 保留所有INFO信息
```
After filtering, kept 40 out of 40 Individuals
Outputting VCF file...
After filtering, kept 78434 out of a possible 147540 Sites
Run Time = 55.00 seconds
```
> 这个output给了你一些基本的信息，这里你所用到的40个个体，全部被保留下来，然后147540中的78434个变异位点经过过滤后被保留下来（几乎一半的变异位点被过滤掉）。运行时间：55秒。
######3.2 接下来过滤的标准是基因型调用的最小深度和最小平均深度。
```
vcftools --vcf raw.g5mac3.recode.vcf --minDP 3 --recode --recode-INFO-all --out raw.g5mac3dp3 
```
> --minDP 3 最小深度至少大于3
```
After filtering, kept 40 out of 40 Individuals
Outputting VCF file...
After filtering, kept 78434 out of a possible 78434 Sites
Run Time = 50.00 seconds
```
######3.3 去除那些没有被测序的很好的个体
```
vcftools --vcf raw.g5mac3dp3.recode.vcf --missing-indv
```
- 这会生成一个out.imiss的文件，看看他里面是什么：
```
INDV    N_DATA  N_GENOTYPES_FILTERED    N_MISS  F_MISS
BR_002  78434   0       13063   0.166548
BR_004  78434   0       16084   0.205064
BR_006  78434   0       25029   0.319109
BR_009  78434   0       30481   0.38862
BR_013  78434   0       69317   0.883762
BR_015  78434   0       8861    0.112974
BR_016  78434   0       29789   0.379797
BR_021  78434   0       17422   0.222123
BR_023  78434   0       43913   0.559872
BR_024  78434   0       24220   0.308795
BR_025  78434   0       21998   0.280465
BR_028  78434   0       26786   0.34151
BR_030  78434   0       74724   0.952699
BR_031  78434   0       26488   0.337711
BR_040  78434   0       19492   0.248515
BR_041  78434   0       17107   0.218107
BR_043  78434   0       16384   0.208889
BR_046  78434   0       28770   0.366805
BR_047  78434   0       13258   0.169034
BR_048  78434   0       24505   0.312428
WL_031  78434   0       22566   0.287707
WL_032  78434   0       22604   0.288191
WL_054  78434   0       32902   0.419486
WL_056  78434   0       34106   0.434837
WL_057  78434   0       37556   0.478823
WL_058  78434   0       31448   0.400949
WL_061  78434   0       35671   0.45479
WL_064  78434   0       47816   0.609634
WL_066  78434   0       10062   0.128286
WL_067  78434   0       47940   0.611215
WL_069  78434   0       38260   0.487799
WL_070  78434   0       21188   0.270138
WL_071  78434   0       16692   0.212816
WL_072  78434   0       46347   0.590904
WL_076  78434   0       78178   0.996736
WL_077  78434   0       55193   0.703687
WL_078  78434   0       54400   0.693577
WL_079  78434   0       19457   0.248068
WL_080  78434   0       30076   0.383456
WL_081  78434   0       30334   0.386746
```
> F_miss 有些个体miss 很高（0.996736）需要剔除
```
# 把第五列miss 大于0.5的个体的名称取出来
mawk '$5 > 0.5' out.imiss | cut -f1 > lowDP.indv
```
```
INDV
BR_013
BR_023
BR_030
WL_064
WL_067
WL_072
WL_076
WL_077
WL_078
```
```
# 删除这些人
vcftools --vcf raw.g5mac3dp3.recode.vcf --remove lowDP.indv --recode --recode-INFO-all --out raw.g5mac3dplm
```
######3.4 将变异限制为在高百分比的个体中，并通过基因型的平均深度进行过滤。
```
vcftools --vcf raw.g5mac3dplm.recode.vcf --max-missing 0.95 --maf 0.05 --recode --recode-INFO-all --out DP3g95maf05 --min-meanDP 20
```
> MAF是最小等位基因频率通常是指在给定人群中的不常见的等位基因发生频率，例如TT，TC，CC三个基因型，在人群中C的频率=0.36，T的频率=0.64，则等位基因C就为最小等位基因频率，MAF=0.36。
######4 加入表型数据过滤
######4.1 表型数据
```
cat popmap

BR_002    BR
BR_004    BR
BR_006    BR
BR_009    BR
BR_013    BR
BR_015    BR
BR_016    BR
BR_021    BR
BR_023    BR
BR_024    BR
BR_025    BR
BR_028    BR
BR_030    BR
BR_031    BR
BR_040    BR
BR_041    BR
BR_043    BR
BR_046    BR
BR_047    BR
BR_048    BR
WL_031    WL
WL_032    WL
WL_054    WL
WL_056    WL
WL_057    WL
WL_058    WL
WL_061    WL
WL_064    WL
WL_066    WL
WL_067    WL
WL_069    WL
WL_070    WL
WL_071    WL
WL_072    WL
WL_076    WL
WL_077    WL
WL_078    WL
WL_079    WL
WL_080    WL
WL_081    WL
```
- 现在我们需要创建两个列表，这些列表只包含每个个体的个别名称。
```
mawk '$2 == "BR"' popmap > 1.keep && mawk '$2 == "WL"' popmap > 2.keep
```
- 接下来，我们使用VCFtools来估计每个群体中基因座的缺失数据。
```
vcftools --vcf DP3g95maf05.recode.vcf --keep 1.keep --missing-site --out 1
vcftools --vcf DP3g95maf05.recode.vcf --keep 2.keep --missing-site --out 2 
```
> **基因座**（英语：**locus**），也称为“基因位点”或“位点”，是指染色体上的固定位置，例如某个[基因](https://zh.wikipedia.org/wiki/%E5%9F%BA%E5%9B%A0 "基因")的所在。而基因座上的DNA序列可能有许多不同的变化，各种变化形式称为[等位基因](https://zh.wikipedia.org/wiki/%E7%AD%89%E4%BD%8D%E5%9F%BA%E5%9B%A0 "等位基因")（allele）

> 这会生成两个文件分别是 1.lmiss 和2.lmiss
```
head -3 1.lmiss
CHR	POS	N_DATA	N_GENOTYPE_FILTERED	N_MISS	F_MISS
E1_L101	9	34	0	0	0
E1_L101	15	34	0	0	0
```
> 看最后的F_MISS 率， 低于10%的删除
```
cat 1.lmiss 2.lmiss | mawk '!/CHR/' | mawk '$6 > 0.1' | cut -f1,2 >> badloci
```
- 然后，我们将此文件反馈到VCFtools以删除质量低的基因座。
```
vcftools --vcf DP3g95maf05.recode.vcf --exclude-positions badloci --recode --recode-INFO-all --out DP3g95p5maf05
```
