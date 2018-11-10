####1. 下载AxiomTM Analysis Suite 3.1 软件，注册账号
####2. 下载Axiom_PMRA.r2 
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e8de5f315bbf6d2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. cel_to_vcf 质控参数
![image.png](https://upload-images.jianshu.io/upload_images/6634703-075dea9dd37d8322.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####以下开始使用plink
####1. tassel 软件填补缺失值
```
# tassel 软件 KNN 填补 （也可以不填补）
perl /Users/chengkai/Documents/01_NMR/003GWAS/GWAShandbook/software/tassel_v5/run_pipeline.pl -Xms512m -Xmx5g -importGuess /Users/chengkai/Documents/01_NMR/00_NMR/csvd/csvd.vcf -LDKNNiImputationPlugin -highLDSSites 50 -knnTaxa 5 -maxLDDistance 100000000 -endPlugin -export csvd.imputed.vcf -exportType VCF
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d1bf918f2ea2ed64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. vcf 文件过滤
- 使用vcftools 过滤
```
# MAF<0.05 第二等位基因频率小于0.05
vcftools --vcf csvd.vcf --maf 0.05 --out csvd_005maf
# 缺失率不小于90%
vcftools --vcf csvd.vcf  --max-missing 0.9 --out csvd_missing0.9
# 平均深度大于5
vcftools --vcf csvd.vcf --min-meanDP 5 --out csvd_meanDP5 
```
- 使用plink 过滤
```
1. vcf转化plink格式, 生成ped 和 map 文件。
vcftools --vcf test.vcf --plink --out  xxx
```
- 生成两个文件，看下格式.ped

|Family|ID|Individual ID|Paternal ID |Maternal ID|Sex (1=male; 2=female; other=unknown)|Phenotype|
|---|---|---|---|---|---|---|
|1       |1303MR00001|     0| 0|       2|       2|  ```CC     CC     CC     CC     CC     CG ...```|
- 看下map 格式

|Chromosome|Marker ID|Genetic distance|Physical position|
|---|---|---|---| 
|10|AFFX-SP-000001|1.4527|123096468|

```
2. plink --noweb --file plink --geno 0.05 --maf 0.05 --hwe 0.0001 --make-bed
# plink 2.0 --file 报错，我用plink 1.9 跑
3. plink --noweb --file csvd --geno 0.05 --maf 0.05 --hwe 0.001 --make-bed --out csvd_005geno_005maf_0001hwe
```
- 性别检测
```
plink --noweb --file csvd --check-sex --out sex-check
```
- 亲缘关系检测
```

```
#####全基因组关联分析
```
plink --allow-no-sex --bfile csvd_005geno_005maf_0001hwe --pheno phone.txt --pheno-name phenotype --assoc --out csvd00
```
####曼哈顿图
```
csvd<-read.table('/Users/chengkai/Documents/01_NMR/prma_vcf_20180821/csvd_revise/data/csvd.assoc',header=TRUE)
library('RColorBrewer')
manhattan(csvd, main="csvd", chr = "CHR", bp = "BP", p = "P", snp = "SNP",
          col = c("blue4", "orange3"), chrlabs = NULL,
          suggestiveline = -log10(1e-05), genomewideline = -log10(1.25e-07),
          highlight = NULL, logp = TRUE, annotatePval = NULL,annotateTop = TRUE)

qq(csvd$P, main = "Q-Q plot of csvd p-values", xlim = c(0, 7), ylim = c(0, 12), pch = 18, col = "blue4", cex = 1.5, las = 1)
```
