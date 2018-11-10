####任务
- 比对软件很多，首先大家去收集一下，因为我们是带大家入门，请统一用hisat2，并且搞懂它的用法。 直接去hisat2的主页下载index文件即可，然后把fastq格式的reads比对上去得到sam文件。 接着用samtools把它转为bam文件，并且排序(注意N和P两种排序区别)索引好，载入IGV，再截图几个基因看看！ 顺便对bam文件进行简单QC，参考直播我的基因组系列。
####下载 index
```
axel ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/hg19.tar.gz
tar -zxvf hg19.tar.gz  #解压
```
- ps.下了我19个小时。。。
#### 正式比对
- 命令行目录：Desktop/zhuanlu_files
- hg19目录：Desktop/zhuanlu_files／hg19
- RNA-Seq Data: Desktop/zhuanlu_files/RNA-Seq
- 注释：
-t 记录时间
-x hg19(index)文件路径
-1 -2 测序的两个fastq文件
-S 比对结果输出路径 
```
mkdir -p RNA-Seq/aligned
for i in `seq 56 58`
do
    hisat2 -t -x hg19/genome -1 RNA-Seq/SRR35899${i}.sra_1.fastq.gz -2 RNA-Seq/SRR35899${i}.sra_2.fastq.gz -S RNA-Seq/aligned/SRR35899${i}.sam 
done
```
- i7处理器，内存16G 运行结果如下，如果你在服务器上跑，内存大于64G，上面代码.sam后加一个‘&’  那就是6个线程同时跑了，大大提升速度，
![image.png](http://upload-images.jianshu.io/upload_images/6634703-cf6bcd404f41c8fe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 比对解读
    - 总共比对了28856780条，7.4%一次都没有比对到，77.18%比对到一次，15.41%大于一次
    - 没有匹配上的7.4%，不按照顺序再匹配，有4.3%匹配了
    - 之后把剩余部分用单端数据进行比对，64.28%没有比对上，26.16比对了一次，9.56%大于一次
    - 总共比对到95.45% 
![image.png](http://upload-images.jianshu.io/upload_images/6634703-a225442c39180928.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####SAMtools
SAMtools 详解：
http://www.jianshu.com/p/15f3499a6469
SAM 数据格式是目前高通量测序中存放比对数据的标准格式，但是SAM 文件都很大，非常占空间，所以需要转到bam文件，而用的就是SAMtools软件。
- 注释
-S 输入sam文件
-b 指定输出的文件为bam
- 排序默认是根据染色体的位置
```
for i in `seq 56 58`
do
    samtools view -S SRR35899${i}.sam -b > SRR35899${i}.bam
    samtools sort SRR35899${i}.bam -o SRR35899${i}_sorted.bam
    samtools index SRR35899${i}_sorted.bam
done
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-4f1fff3c53f4b62e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####IGV 可视化
- 文件导入“详见转录组入门四”

![image.png](http://upload-images.jianshu.io/upload_images/6634703-788ce332392b75fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
