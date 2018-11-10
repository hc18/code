> 本文学习[GATK4.0和全基因组数据分析实践](http://www.huangshujia.me/2018/02/20/2018-02-20-WGS-Best-Practics.html)
####1. 项目目录结构
```
201807_wgs_practice/
├── bin
├── input
└── output
```
####2.下载E.coli K12的参考基因组序列
```
ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz
# 为了接下来表达上的清晰和操作上的方便，我们使用bgzip将这个序列文件进行解压并把名字重命名为E.coli_K12_MG1655.fa，这样就一目了然了。
gzip -dc GCF_000005845.2_ASM584v2_genomic.fna.gz > E.coli_K12_MG1655.fa
# 用samtools为它创建一个索引
/Tools/common/bin/samtools faidx E.coli_K12_MG1655.fa
```
####3. 下载E.coli K12的测序数据
```
wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR177/SRR1770413/SRR1770413.sra
# sratoolkit 把 SRA 文件变为fastq
/home/chengkaizhu/zhuchengkai/software/sratoolkit.2.9.1-1-centos_linux64/bin/fastq-dump --split-files SRR1770413.sra
# 下载完成后，我们最好用bgzip（不推荐gzip）将其压缩为.gz文件，这样可以节省空间，而且也不会对接下来的数据分析产生影响。 （我没有bzip ,所以用gzip 压缩了）
gzip -f SRR1770413_1.fastq
gzip -f SRR1770413_2.fastq
```
- 项目目录
```
201807_wgs_practice/
├── bin
├── input
│   └── E_coli
│       ├── fasta
│       │   ├── E.coli_K12_MG1655.fa
│       │   └── E.coli_K12_MG1655.fa.fai
│       └── fastq
│           ├── SRR1770413_1.fastq.gz
│           ├── SRR1770413_2.fastq.gz
│           └── SRR1770413.sra
└── output
```
#### 4. 质控
######4.1 bwa 构建比对索引
```
# bwa 构建比对索引
bwa index E.coli_K12_MG1655.fa
```
######4.2 比对 (bwa_and_markdup.sh)
```
#1 比对, 输出一个E_coli_K12.bam文件
time bwa mem -t 4 -R '@RG\tID:foo\tPL:illumina\tSM:E.coli_K12' /home/chengkaizhu/zhuchengkai/201807_wgs_practice/input/E_coli/fasta/E.coli_K12_MG1655.fa /home/chengkaizhu/zhuchengkai/201807_wgs_practice/input/E_coli/fastq/SRR1770413_1.fastq.gz /home/chengkaizhu/zhuchengkai/201807_wgs_practice/input/E_coli/fastq/SRR1770413_2.fastq.gz | samtools view -Sb - > /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.bam && echo "** bwa mapping done **"

#2 排序, 输出E_coli_K12.sorted.bam ，并删除 E_coli_K12.bam文件
time samtools sort -@ 16 -m 16G -O bam -o /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.sorted.bam /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.bam && echo "** BAM sort done"
rm -f /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.bam

# 3 标记PCR重复
time /opt/gatk-4.0.6.0/gatk MarkDuplicates -I /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.sorted.bam -O /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.sorted.markdup.bam -M /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.sorted.markdup_metrics.txt && echo "** markdup done **"

# 4 删除不必要文件(可选)
rm -f /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.bam
rm -f /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.sorted.bam

# 5 创建比对索引文件
time samtools index /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.sorted.markdup.bam && echo "** index done **"
```
####5. 变异检测 (gatk.sh)
```
# 先生成一个 dict 文件
/opt/gatk-4.0.6.0/gatk CreateSequenceDictionary -R E.coli_K12_MG1655.fa -O E.coli_K12_MG1655.dict && echo "** dict done **"
```
```
#1 生成中间文件gvcf
time /opt/gatk-4.0.6.0/gatk HaplotypeCaller -R /home/chengkaizhu/zhuchengkai/201807_wgs_practice/input/E_coli/fasta/E.coli_K12_MG1655.fa --emit-ref-confidence GVCF -I /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.sorted.markdup.bam -O /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.g.vcf && echo "** gvcf done **"

#2 通过gvcf检测变异
time /opt/gatk-4.0.6.0/gatk GenotypeGVCFs -R /home/chengkaizhu/zhuchengkai/201807_wgs_practice/input/E_coli/fasta/E.coli_K12_MG1655.fa -V /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.g.vcf -O /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.vcf && echo "** vcf done **"

```
```
#1 压缩 
time bgzip -f /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.vcf
#2 构建tabix索引
time tabix -p vcf /home/chengkaizhu/zhuchengkai/201807_wgs_practice/output/E_coli/E_coli_K12.vcf.gz
```
>如果用gzip 压缩，就不能用tabix构建索引。
- 目录
```201807_wgs_practice/
├── bin
│       ├── bwa_and_markdup.sh
│       └── gatk.sh
├── input
│   └── E_coli
│       ├── fasta
│       │   ├── E.coli_K12_MG1655.dict
│       │   ├── E.coli_K12_MG1655.fa
│       │   ├── E.coli_K12_MG1655.fa.amb
│       │   ├── E.coli_K12_MG1655.fa.ann
│       │   ├── E.coli_K12_MG1655.fa.bwt
│       │   ├── E.coli_K12_MG1655.fa.fai
│       │   ├── E.coli_K12_MG1655.fa.pac
│       │   └── E.coli_K12_MG1655.fa.sa
│       └── fastq
│           ├── SRR1770413_1.fastq.gz
│           ├── SRR1770413_2.fastq.gz
│           └── SRR1770413.sra
└── output
    └── E_coli
        ├── E_coli_K12.g.vcf
        ├── E_coli_K12.g.vcf.idx
        ├── E_coli_K12.sorted.markdup.bam
        ├── E_coli_K12.sorted.markdup.bam.bai
        ├── E_coli_K12.sorted.markdup_metrics.txt
        ├── E_coli_K12.vcf.gz
        └── E_coli_K12.vcf.idx
```
