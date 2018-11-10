####序章
>1. GWAS全基因组关联分析，近年来一直为研究的热点，不管是研究复杂疾病或是遗传育种，均有广泛的用途。但是GWAS的数据动辄上千的样本数据，如何对这庞大的数据进行分析？于是就有了一个强大的分析工具--PLINK。
>2. **主要的功能模块包括：**数据处理，质量控制的基本统计，群体分层分析，单位点的基本关联分析，家系数据的传递不平衡检验，多点连锁分析，单倍体关联分析，拷贝数变异分析，Meta分析等等。
>3. **全基因组关联分析 GWAS (Genome-wide association study;GWAS)：**应用基因组中数以百万计的单核苷酸多态；SNP为分子遗传标记，进行全基因组水平上的对照分析或相关性分析，通过比较发现影响复杂性状的基因变异的一种新策略。
> 4. **GWAS的基本原理**: 借助于SNP分子遗传标记，进行总体关联分析，在全基因组范围内选择遗传变异进行基因分析，比较异常和对照组之间每个遗传变异及其频率的差异，统计分析每个变异与目标性状之间的关联性大小，选出最相关的遗传变异进行验证，并根据验证结果最终确认其与目标性状之间的相关性。
####1 .ped 格式
- ped文件包含了基因型信息，每一行为一个样本
- ped 有7列

|Family ID| Individual ID|Paternal ID|Maternal ID|Sex|Phenotype|Genotypes
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
家族ID|个人ID|父亲ID|母亲ID|性别|表型|基因型|
- Sex (1=male; 2=female; other=unknown)
- Phenotype (1 = case; 2 = control)
- 7以后是基因型，可以有很多列，但基因型必须是成对存在的。
```
# 举例
FAM001  1  0 0  1  2  A A  G G  A C 
HCB181  1  0 0  1  1  2 2  2 2  2 2
```
####2 .map 格式
- MAP文件主要是用来记录每个maker（一般为SNP）的位置信息。
- map有4列

chr | snp identifier| morgans| bp units|
|:---:|:---:|:---:|:---:|
|染色体|snp标识|基因距离|碱基距离|
```
# 举例
1  rs0   0   1000
1  rs10  0	 1001
```
####参考文献
1. http://zzz.bwh.harvard.edu/plink/data.shtml
2. http://zzz.bwh.harvard.edu/plink/metaanal.shtml
