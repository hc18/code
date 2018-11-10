####1. 材料获取
```
http://www.well.ox.ac.uk/ggeu/NPanalysis/
# 解压
tar -xvzf cg-data.tgz
tar -xvzf gwa-data.tgz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-eef2d1ce947c6d56.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 数据已经过滤了
> The simulated data used here have passed standard quality control: all individuals have a missing data rate of <10%. SNPs with a missing rate >10%, a MAF <1% or an HWE *P* value <1 × 10<sup>−5</sup> have already been excluded. These filters were selected in accordance with procedures described elsewhere<sup>[3](https://www.nature.com/articles/nprot.2010.182#ref3 "Anderson, C.A. et al. Data quality control in genetic-case control association studies. Nat. Protoc. 5, 1564–1573 (2010).")</sup> to minimize the influence of genotype-calling artifacts in a GWA study.
####2. Basic descriptive summary
```
# to obtain a summary of MAFs
plink --file cg --assoc --out data
# 如果是二进制文件
‘--file cg’ 改为 ‘--bfile gwa’
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f220bc36c48d4742.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> Open the output file 'data.assoc'. It has one row per SNP containing the chromosome [CHR], the SNP identifier [SNP], the base-pair location [BP], the minor allele [A1], the frequency of the minor allele in the cases [F_A] and controls [F_U], the major allele [A2] and statistical data for an allelic association test including the χ2-test statistic [CHISQ], the asymptotic P value [P] and the estimated OR for association between the minor allele and disease [OR].

####3. Single SNP tests of association
######3.1 Simple χ2 tests of association
```
plink --file cg --model --out data
plink --bfile gwa --model --out data
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-237f5bae7ab24b4e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>Open the output file 'data.model'. It contains five rows per SNP, one for each of the association tests described in Table 2. Each row contains the chromosome [CHR], the SNP identifier [SNP], the minor allele [A1], the major allele [A2], the test performed [TEST: GENO (genotypic association); TREND (Cochran-Armitage trend); ALLELIC (allelic association); DOM (dominant model); and REC (recessive model)], the cell frequency counts for cases [AFF] and controls [UNAFF], the χ2 test statistic [CHISQ], the degrees of freedom for the test [DF] and the asymptotic P value [P].
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1766ca81f7e05f77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######3.2 Test of association using logistic regression
```
plink --bfile gwa --logistic --covar gwa.covar --out data
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-2a85df6bc37d513a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. Data visualization
######4.1 Quantile-quantile plot
```
# 此源代码我跑不通
library(car)
data <- read.table("/Users/chengkai/Downloads/case/cg/data.model")
pdf("/Users/chengkai/Downloads/case/cg/chisq.qq.plot.pdf")
obs <- data[data$TEST== "[model]",]$CHISQ
qqPlot(obs, distribution="chisq", df=1, xlab="Expected chi-squared values", ylab= "Observed test statistic", grid=FALSE)
dev.off()

# 修改后的代码
data <- read.table("/Users/chengkai/Downloads/case/cg/data.model")
pdf("/Users/chengkai/Downloads/case/cg/chisq.qq.plot.pdf")
library(car)
obs <- as.numeric(data[data$V5== "GENO",]$V8)
qqPlot(obs, distribution="chisq", df=2, xlab="Expected chi-squared values", ylab= "Observed test statistic", grid=FALSE)
dev.off()
```
>where [path_to] is the appropriate directory path and [model] identifies the association test output to be displayed, and where [model] can be TREND (Cochran-Armitage trend); ALLELIC (allelic association); DOM (dominant model); or REC (recessive model). For simple χ2 tests of association based on a genotypic model, in which test statistics have a χ2 distribution with 2 d.f. under the null hypothesis of no association, use the option [df] = 2 and [model] = GENO.

![image.png](https://upload-images.jianshu.io/upload_images/6634703-25243a3ae7100401.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-939ee4e7d19a9a01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- Create a quantile-quantile plot 'pvalue.qq.plot.pdf' based on −log10 P values from tests of association using logistic regression described in Step 4B by typing
```
data <- read.table("/Users/chengkai/Downloads/case/gwa/data.PHENO1.glm.logistic", header=TRUE)
pdf("/Users/chengkai/Downloads/case/gwa/pvalue.qq.plot.pdf")
obs <- -log10(sort(data[data$TEST=="ADD",]$P))
exp <- -log10(c(1:length(obs)) /(length(obs)+1))
plot(exp, obs, ylab= "Observed (-logP)", xlab="Expected(-logP)", ylim=c(0,20), xlim=c(0,7))
lines(c(0,7), c(0,7), col=1, lwd=2)
dev.off()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-32aee0c1a767424c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######4.2 Manhattan plot
>1. Start Haploview. In the 'Welcome to Haploview' window, select the 'PLINK Format' tab. Click the 'browse' button and select the SNP association output file created in Step 4. We select our GWA study χ2 tests of association output file 'data.model'. Select the corresponding MAP file, which will be the '.map' file for the pedigree file format or the '.bim' file for the binary file format. We select our GWA study file 'gwa.bim'. Leave other options as they are (ignore pairwise comparison of markers >500 kb apart and exclude individuals with >50% missing genotypes). Click 'OK'.
>2. Select the association results relevant to the test of interest by selecting 'TEST' in the dropdown tab to the right of 'Filter:', '=' in the dropdown menu to the right of that and the PLINK keyword corresponding to the test of interest in the window to the right of that. We select PLINK keyword 'ALLELIC' to visualize results for allelic tests of association in our GWA study. Click the gray 'Filter' button. Click the gray 'Plot' button. Leave all options as they are so that 'Chromosomes' is selected as the 'X-Axis'. Choose 'P' from the drop-down menu for the 'Y-Axis' and '-log10' from the corresponding dropdown menu for 'Scale:'. Click 'OK' to display the Manhattan plot.
>3. To save the plot as a scalable vector graphics file, click the button 'Export to scalable vector graphics:' and then click the 'Browse' button (immediately to the right) to select the appropriate title and directory.

![image.png](https://upload-images.jianshu.io/upload_images/6634703-4c14c3fef6df216f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

######4.3 LD plot
```
cg.map <- read.table("/Users/chengkai/Downloads/case/cg/cg.map")
write.table(cg.map[,c(2,4)],"/Users/chengkai/Downloads/case/cg/cg.hmap", col.names=FALSE, row.names=FALSE, quote=FALSE)
```
> Start Haploview. In the 'Welcome to Haploview' window, select the 'LINKAGE Format' tab. Click the 'browse' button to enter the 'Data File' and select the PED file 'cg.ped'. Click the 'browse' button to enter the 'Locus Information File' and select the file 'cg.hmap'. Leave other options as they are (ignore pairwise comparison of markers >500 kb apart and exclude individuals with >50% missing genotypes). Click 'OK'. Select the 'LD Plot' tab.

![image.png](https://upload-images.jianshu.io/upload_images/6634703-d7f9232940f8d10e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)































































































































































































