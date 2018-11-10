####1. 什么是质控
- 质控的含义和目是指通过一定的标准，最大可能地剔除假阳性的结果，并尽可能地保留最多的正确数据
####2. 硬过滤范例
```
# 使用SelectVariants，选出SNP
time /Tools/common/bin/gatk/4.0.1.2/gatk SelectVariants \
    -select-type SNP \
    -V ../output/E.coli/E_coli_K12.vcf.gz \
    -O ../output/E.coli/E_coli_K12.snp.vcf.gz
# 为SNP作硬过滤
time /Tools/common/bin/gatk/4.0.1.2/gatk VariantFiltration \
    -V ../output/E.coli/E_coli_K12.snp.vcf.gz \
    --filter-expression "QD < 2.0 || MQ < 40.0 || FS > 60.0 || SOR > 3.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0" \
    --filter-name "Filter" \
    -O ../output/E.coli/E_coli_K12.snp.filter.vcf.gz
# 使用SelectVariants，选出Indel
time /Tools/common/bin/gatk/4.0.1.2/gatk SelectVariants \
    -select-type INDEL \
    -V ../output/E.coli/E_coli_K12.vcf.gz \
    -O ../output/E.coli/E_coli_K12.indel.vcf.gz
# 为Indel作过滤
time /Tools/common/bin/gatk/4.0.1.2/gatk VariantFiltration \
    -V ../output/E.coli/E_coli_K12.indel.vcf.gz \
    --filter-expression "QD < 2.0 || FS > 200.0 || SOR > 10.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0" \
    --filter-name "Filter" \
    -O ../output/E.coli/E_coli_K12.indel.filter.vcf.gz
# 重新合并过滤后的SNP和Indel
time /Tools/common/bin/gatk/4.0.1.2/gatk MergeVcfs \
    -I ../output/E.coli/E_coli_K12.snp.filter.vcf.gz \
    -I ../output/E.coli/E_coli_K12.indel.filter.vcf.gz \
    -O ../output/E.coli/E_coli_K12.filter.vcf.gz
# 删除无用中间文件
rm -f ../output/E.coli/E_coli_K12.snp.vcf.gz* ../output/E.coli/E_coli_K12.snp.filter.vcf.gz* ../output/E.coli/E_coli_K12.indel.vcf.gz* ../output/E.coli/E_coli_K12.indel.filter.vcf.gz*
```
######2.1 QualByDepth（QD）
QD是变异质量值（Quality）除以覆盖深度（Depth）得到的比值，一般控制在QD>2以上
> 通俗一些讲就是，不同的变异都有一个质量值，这些质量值除以覆盖深度，就变成标准化的质量值，QD越高一般来说变异的可信度也越高。这么算的主要目的是避免局部深度不均，带来有偏的质控结果

######2.2 FisherStrand（FS）
- 
