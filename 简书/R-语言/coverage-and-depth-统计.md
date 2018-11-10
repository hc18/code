####方法1
1. 假设有比对好的bam 文件
2. 把chr1 覆盖度提出来
```
samtools depth deduped_MA605.bam | awk '$1 == chr1 {print $0}'  >chr1.coverage
```
3. 画图看看 
```
MA605.chr2<-read.table("chr1.coverage",header=FALSE, sep="", na.strings="NA", dec=".", strip.white=TRUE)
library(reshape)
MA605.chr2<-rename(MA605.chr2,c(V1="Chr", V2="locus", V3="depth"))
png(file="chr1.png")
plot(MA605.chr2$locus, MA605.chr2$depth)
dev.off()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f218808ccbb68c0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. 用ggplot
```
coverage=read.table("chr1", sep="", header=F)
install.packages('reshape')
library(reshape)
library(ggplot2)
coverage=rename(coverage,c(V1="Chr", V2="locus", V3="depth")) # renames the header
ggplot(coverage, aes(x=locus, y=depth)) +
  geom_point(colour="red", size=1, shape=20, alpha=1/3) +
  scale_y_continuous(trans = scales::log10_trans(), breaks = scales::trans_breaks("log10", function(x) 10^x))
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d32b9b3a35afce21.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####方法二
