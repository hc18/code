> 本文是# [GATK4全基因组数据分析最佳实践,我以这篇文章为标志,终结当前WGS系列数据分析的流程主体问题 | 完全代码](http://www.huangshujia.me/2018/05/11/2018-05-11-Code-For-GATK4-Best-Practice.html) 的重复，感谢一下作者-解螺旋的矿工
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3b3932577f98057b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```
#!/usr/bin/bash

## 这是多样本变异检测流程的前半部分，这个部分假设你的每个样本只有一对用Illumina测序仪测序的PE fastq

# 一些软件和工具的路径, 根据实际可以另行添加
trimmomatic=/root/anaconda3/bin/trimmomatic 
bwa=/root/anaconda3/bin/bwa
samtools=/root/anaconda3/bin/samtools
gatk=/opt/gatk-4.0.6.0/gatk

#reference
reference=/share/public/reference/Homo_sapiens/hg38/reference/Homo_sapiens_assembly38.fasta
GATK_bundle=/share/public/reference/Homo_sapiens/hg38/reference

## 这一步不是必须的，取决于GATK_bundle中的这4份文件是否已经有建索引，如没有再执行
#$gatk IndexFeatureFile --feature-file $GATK_bundle/hapmap_3.3.hg38.vcf  
#$gatk IndexFeatureFile --feature-file $GATK_bundle/1000G_omni2.5.hg38.vcf  
#$gatk IndexFeatureFile --feature-file $GATK_bundle/1000G_phase1.snps.high_confidence.hg38.vcf  
#$gatk IndexFeatureFile --feature-file $GATK_bundle/Mills_and_1000G_gold_standard.indels.hg38.vcf
#$gatk IndexFeatureFile --feature-file $GATK_bundle/dbsnp_146.hg38.vcf  

## shell执行参数
fq1=/share/public/reference/Homo_sapiens/hg38/hg38_bwa_index/CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1_R1_001.fastq.gz
fq2=/share/public/reference/Homo_sapiens/hg38/hg38_bwa_index/CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1_R2_001.fastq.gz
RGID=CHB000012  ## Read Group，一般用Lane ID代替
#library=$4  ## 测序文库编号
sample=1303MR00002WJ1  ## 样本ID
outdir=/share/public/reference/Homo_sapiens/hg38/hg38_bwa_index/ ## 输出目录的路径

## 按样本设置目录
outdir=${outdir}/${RGID}

## 通过fastq1获得fastq的前缀名字，这里假设了原始的fastq1和fastq2有相同的前缀名字
## 并且假设fastq1的文件名格式为*.1.fq.gz;
fq_file_name=`basename $fq1`
fq_file_name=${fq_file_name%%_R1_001.fastq.gz}

########################################以下代码建议不要改动#####################################
# output diretory
if [ ! -d $outdir/cleanfq ]
then mkdir -p $outdir/cleanfq
fi

if [ ! -d $outdir/bwa ]
then mkdir -p $outdir/bwa
fi

if [ ! -d $outdir/gatk ]
then mkdir -p $outdir/gatk
fi
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dfb22de7828e3f2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
## 使用Trimmomatic对原始数据进行质控，ILLUMINACLIP中的一个关键参数 keepBothReads设为True。
time ${trimmomatic} PE \
       $fq1 $fq2 \
       $outdir/cleanfq/${fq_file_name}.paired.1.fq.gz ${fq_file_name}.unpaired.1.fq.gz \
       $outdir/cleanfq/${fq_file_name}.paired.2.fq.gz ${fq_file_name}.unpaired.2.fq.gz \
       ILLUMINACLIP:/root/anaconda3/pkgs/trimmomatic-0.36-5/share/trimmomatic/adapters/TruSeq3-PE-2.fa:2:30:10:8:True \
       SLIDINGWINDOW:5:15 LEADING:5 TRAILING:5 MINLEN:50 && echo "** fq QC done **"
```
> 接头和引物序列在 TruSeq3-SE 中，第一步 seed 搜索允许2个碱基错配，palindrome 比对分值阈值 30，simple clip 比对分值阈值 10，palindrome 模式允许切除的最短接头序列为 8bp（默认值），palindrome 模式去除与 R1 完全反向互补的 R2（默认去除）
> TruSeq3-PE-2.fa : 接头序列
> 2 : 是比对时接头序列时所允许的最大错配数
> 30 : 指的是要求PE的两条read同时和PE的adapter序列比对，匹配度加起来超30%，那么就认为这对PE的read含有adapter，并在对应的位置需要进行切除
> 10 : 10和前面的30不同，它指的是，我就什么也不管，反正只要这条read的某部分和adpater序列有超过10%的匹配率，那么就代表含有adapter了，需要进行去除
>SLIDINGWINDOW:5:20代表窗口长度为5，窗口中的平均质量值至少为15，否则会开始切除；
> LEADING，规定read开头的碱基是否要被切除的质量阈值；
> TRAILING，规定read末尾的碱基是否要被切除的质量阈值；
> MINLEN，规定read被切除后至少需要保留的长度，如果低于该长度，会被丢掉。
```
## 使用bwa mem完成数据比对，bwa mem对任何长度大于40bp小于2000bp的read都是非常有效的; PL:ILLUMINA是我默认的
time $bwa mem -t 40 -M -Y -R "@RG\tID:$RGID\tPL:ILLUMINA\tSM:$sample" $reference \
	$outdir/cleanfq/${fq_file_name}.paired.1.fq.gz $outdir/cleanfq/${fq_file_name}.paired.2.fq.gz | $samtools view -Sb - > $outdir/bwa/${sample}.bam && \
	echo "** BWA MEM done **" && \
time $samtools sort -@ 16 -m 4G -O bam -o $outdir/bwa/${sample}.sorted.bam $outdir/bwa/${sample}.bam && echo "** sorted raw bamfile done "
```
> -M      将 shorter split hits 标记为次优，以兼容 Picard’s markDuplicates 软件。
> -Y Use soft clipping CIGAR operation for supplementary alignments. By default, BWA-MEM uses soft clipping for the primary alignment and hard clipping for supplementary alignments.
> -@，用于设定排序时的线程数；-m，每个线程排序时最大的内存消耗；-O 指定输出为bam格式；-o 是输出文件的名字
```
CHB000012
├── bwa
│   └── 1303MR00002WJ1.bam
├── cleanfq
│   ├── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.1.fq.gz
│   └── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.2.fq.gz
└── gatk

```
```
## 这一步不是必须的 
# time $samtools index $outdir/bwa/${sample}.sorted.bam && echo "** ${sample}.sorted.bam index done **"

## 标记重复序列 
$gatk MarkDuplicates \
  -I $outdir/bwa/${sample}.sorted.bam \
  -M $outdir/bwa/${sample}.markdup_metrics.txt \
  -O $outdir/bwa/${sample}.sorted.markdup.bam && echo "** ${sample}.sorted.bam MarkDuplicates done **"
```

```
# 为${sample}.sorted.markdup.bam构建Index，这是继续后续步骤所必须的
time $samtools index -@ 64 $outdir/bwa/${sample}.sorted.markdup.bam && echo "** ${sample}.sorted.markdup.bam index done **"
```
```
[chengkaizhu@Server-Sugon CHB000012]$ tree
.
├── bwa
│   ├── 1303MR00002WJ1.bam
│   ├── 1303MR00002WJ1.markdup_metrics.txt
│   ├── 1303MR00002WJ1.sorted.bam
│   ├── 1303MR00002WJ1.sorted.markdup.bam
│   └── 1303MR00002WJ1.sorted.markdup.bam.bai
├── cleanfq
│   ├── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.1.fq.gz
│   └── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.2.fq.gz
├── gatk
└── nohup.out
```
```
## 执行BQSR
## [注]Does your vcf file have an index? GATK4 does not support on the fly indexing of VCFs anymore.
time $gatk BaseRecalibrator \
    -R $reference/Homo_sapiens_assembly38.fasta \
    -I $outdir/bwa/${sample}.sorted.markdup.bam \
    --known-sites $GATK_bundle/1000G_phase1.indels.hg38.vcf \
    --known-sites $GATK_bundle/Mills_and_1000G_gold_standard.indels.hg38.vcf \
    --known-sites $GATK_bundle/dbsnp_146.hg38.vcf \
    -O $outdir/bwa/${sample}.sorted.markdup.recal_data.table && echo "** ${sample}.sorted.markdup.recal_data.table done **" 

time $gatk ApplyBQSR \
    --bqsr-recal-file $outdir/bwa/${sample}.sorted.markdup.recal_data.table \
	-R $reference/Homo_sapiens_assembly38.fasta \
	-I $outdir/bwa/${sample}.sorted.markdup.bam \
	-O $outdir/bwa/${sample}.sorted.markdup.BQSR.bam && echo "** ApplyBQSR done **"
```
```
CHB000012
├── bwa
│   ├── 1303MR00002WJ1.bam
│   ├── 1303MR00002WJ1.markdup_metrics.txt
│   ├── 1303MR00002WJ1.sorted.bam
│   ├── 1303MR00002WJ1.sorted.markdup.bam
│   ├── 1303MR00002WJ1.sorted.markdup.bam.bai
│   ├── 1303MR00002WJ1.sorted.markdup.BQSR.bai
│   ├── 1303MR00002WJ1.sorted.markdup.BQSR.bam
│   └── 1303MR00002WJ1.sorted.markdup.recal_data.table
├── cleanfq
│   ├── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.1.fq.gz
│   └── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.2.fq.gz
├── gatk
└── nohup.out
```
```
## 为${sample}.sorted.markdup.BQSR.bam构建Index，这是继续后续步骤所必须的
time $samtools index $outdir/bwa/${sample}.sorted.markdup.BQSR.bam && echo "** ${sample}.sorted.markdup.BQSR.bam index done **"

## 输出样本的gVCF，有两个方式来完成，结果一样，速度不同。
## 输出样本的全gVCF，面对较大的输入文件时，速度较慢
time $gatk HaplotypeCaller \
        --emit-ref-confidence GVCF \
        -R $reference \
        -I $outdir/bwa/${sample}.sorted.markdup.BQSR.bam \
        -O $outdir/gatk/${sample}.HC.g.vcf.gz && echo "** GVCF ${sample}.HC.g.vcf.gz done **"
# gvcf 转为vcf 
time $gatk GenotypeGVCFs \
        -R $reference \
        -V $outdir/gatk/${sample}.HC.g.vcf.gz \
        -O $outdir/gatk/${sample}.HC.vcf.gz && echo "** ${outname}.HC.vcf.gz done ** "
```
```
[chengkaizhu@Server-Sugon CHB000012]$ tree
.
├── bwa
│   ├── 1303MR00002WJ1.bam
│   ├── 1303MR00002WJ1.markdup_metrics.txt
│   ├── 1303MR00002WJ1.sorted.bam
│   ├── 1303MR00002WJ1.sorted.markdup.bam
│   ├── 1303MR00002WJ1.sorted.markdup.bam.bai
│   ├── 1303MR00002WJ1.sorted.markdup.BQSR.bai
│   ├── 1303MR00002WJ1.sorted.markdup.BQSR.bam
│   ├── 1303MR00002WJ1.sorted.markdup.BQSR.bam.bai
│   └── 1303MR00002WJ1.sorted.markdup.recal_data.table
├── cleanfq
│   ├── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.1.fq.gz
│   └── CHB000012-CHB000012D-1303MR00002WJ1-ATTACTCG-AGGCTATA_S1.paired.2.fq.gz
├── gatk
│   ├── 1303MR00002WJ1.HC.g.vcf.gz
│   ├── 1303MR00002WJ1.HC.g.vcf.gz.tbi
│   └── 1303MR00002WJ1.HC.vcf.gz
└── nohup.out
```
```
# 可以被删除清理的文件，这不是必须执行的
# 对于比对文件只有最终的${sample}.sorted.markdup.BQSR.bam值得留下来
rm -f $outdir/bwa/${sample}.bam $outdir/bwa/${sample}.sorted.bam $outdir/bwa/${sample}.sorted.markdup.bam*
```
```
## 首先是SNP mode
--resource dbsnp,known=true,training=false,truth=false,prior=6.0:$GATK_bundle/dbsnp_146.hg38.vcf \
-tranche 100.0 -tranche 99.9 -tranche 99.0 -tranche 95.0 -tranche 90.0 \
time $gatk VariantRecalibrator \
--resource hapmap,known=false,training=true,truth=true,prior=15.0:$GATK_bundle/hapmap_3.3.hg38.vcf \
--resource omini,known=false,training=true,truth=false,prior=12.0:$GATK_bundle/1000G_omni2.5.hg38.vcf \
-an DP -an QD -an FS -an SOR -an ReadPosRankSum -an MQRankSum \
-mode SNP \
-tranche 100.0 -tranche 99.9 -tranche 99.0 -tranche 95.0 -tranche 90.0 \
--rscript-file $outdir/population/${outname}.HC.snps.plots.R \
--tranches-file $outdir/population/${outname}.HC.snps.tranches \
-O $outdir/population/${outname}.HC.snps.recal && echo "**snps recal done**"

time $gatk ApplyVQSR \
-R $reference \
-V $outdir/${outname}.HC.vcf.gz \
--recal-file $outdir/population/${outname}.HC.snps.recal \
-mode SNP \
-O $outdir/population/${outname}.HC.snps.VQSR.vcf.gz && echo "** SNPs VQSR done **"

## 然后是Indel mode
time $gatk VariantRecalibrator \
-R $reference \
-V $outdir/population/${outname}.HC.snps.VQSR.vcf.gz \
--resource mills,known=true,training=true,truth=true,prior=12.0:$GATK_bundle/Mills_and_1000G_gold_standard.indels.hg38.vcf \
-an DP -an QD -an FS -an SOR -an ReadPosRankSum -an MQRankSum \
-mode INDEL \
--max-gaussians 6 \
--rscript-file $outdir/population/${outname}.HC.snps.indels.plots.R \
--tranches-file $outdir/population/${outname}.HC.snps.indels.tranches \
-O $outdir/population/${outname}.HC.snps.indels.recal && echo "** indels recal done**"

time $gatk ApplyVQSR \
-R $reference \
-V $outdir/population/${outname}.HC.snps.VQSR.vcf.gz \
--ts-filter-level 99.0 \
--tranches-file $outdir/population/${outname}.HC.snps.indels.tranches \
--recal-file $outdir/population/${outname}.HC.snps.indels.recal \
-mode INDEL \
-O $outdir/population/${outname}.HC.VQSR.vcf.gz && echo "** SNPs and Indels VQSR (${outname}.HC.VQSR.vcf.gz finish) done **"

```
```
CHB000013
├── bwa
│   ├── 1303MR00003WJ1.markdup_metrics.txt
│   ├── 1303MR00003WJ1.sorted.markdup.BQSR.bai
│   ├── 1303MR00003WJ1.sorted.markdup.BQSR.bam
│   ├── 1303MR00003WJ1.sorted.markdup.BQSR.bam.bai
│   └── 1303MR00003WJ1.sorted.markdup.recal_data.table
├── cleanfq
│   ├── CHB000013-CHB000013D-1303MR00003WJ1-TCCGGAGA-AGGCTATA_S2.paired.1.fq.gz
│   └── CHB000013-CHB000013D-1303MR00003WJ1-TCCGGAGA-AGGCTATA_S2.paired.2.fq.gz
└── gatk
    ├── 1303MR00003WJ1.HC.g.vcf.gz
    ├── 1303MR00003WJ1.HC.g.vcf.gz.tbi
    ├── 1303MR00003WJ1.HC.vcf.gz
    ├── 1303MR00003WJ1.HC.vcf.gz.tbi
    └── population
        ├── 1303MR00003WJ1.HC.snps.indels.plots.R
        ├── 1303MR00003WJ1.HC.snps.indels.plots.R.pdf
        ├── 1303MR00003WJ1.HC.snps.indels.recal
        ├── 1303MR00003WJ1.HC.snps.indels.recal.idx
        ├── 1303MR00003WJ1.HC.snps.indels.tranches
        ├── 1303MR00003WJ1.HC.snps.plots.R
        ├── 1303MR00003WJ1.HC.snps.plots.R.pdf
        ├── 1303MR00003WJ1.HC.snps.recal
        ├── 1303MR00003WJ1.HC.snps.recal.idx
        ├── 1303MR00003WJ1.HC.snps.tranches
        ├── 1303MR00003WJ1.HC.snps.tranches.pdf
        ├── 1303MR00003WJ1.HC.snps.VQSR.vcf.gz
        ├── 1303MR00003WJ1.HC.snps.VQSR.vcf.gz.tbi
        ├── 1303MR00003WJ1.HC.VQSR.vcf.gz
        └── 1303MR00003WJ1.HC.VQSR.vcf.gz.tbi

```
