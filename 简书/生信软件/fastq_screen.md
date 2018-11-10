####1. 什么是fastq_screen?
- FastQ screen is a tool from Babraham Bionformatics group and is found [here](https://www.bioinformatics.babraham.ac.uk/projects/fastq_screen/). FastQ screen allows user to screen for contaminations (artifacts) in fastq files. They may be from other organisms of your interest or from vector or primers.
####2. 需要的材料
- Source files (.fastq, .fq and gzipped files) 
- Indexed reference genome and genomes you want to look for (for eg. mouse, pig etc)
- Indexed contaminant sequences (for eg primer sequences or vector sequences)
- Aligners- currently it supports 3 aligners: bwa, bowtie and bowtie2.
- Configuration file with reference genome index and any other indexes (primer, vector) 
####3. Step 1: Index reference file.
```
 bowtie2-build -f Homo_sapiens.GRCh38.dna.alt.fa.gz Homo_sapiens_GRCh38
```
> 如果没有下载bowtie2, `conda install bowtie2`
> Homo_sapiens.GRCh38.dna.alt.fa.gz   [官网地址](http://ftp.ensembl.org/pub/current_fasta/mus_musculus/dna/)
> 生成6个index 文件

![image.png](https://upload-images.jianshu.io/upload_images/6634703-3da4c60b0fa9ae33.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
