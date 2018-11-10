#### 序列比对
如今序列比对已成为各种生物学分析中不可缺少的重要环节，通过将未知的基因片段与已知具体信息的基因或基因组进行比较，并分析其中的相同部分与差异部分，就可以得到该基因片段SNP位点、所属物种以及可能具有的生物学功能等重要信息。

#### sam与bam 格式
sam与bam是两种最常用的比对结果输出文件格式，如转录组Tophat分析软件输出的比对结果为.bam文件，而BWA、bowtie等比对软件则主要输出为.sam文件。bam文件格式是sam文件的二进制格式，占用的存储空间更小，更利于节省存储资源，而且bam文件的计算处理也更快，但二进制无法直接查看则是它的一个明显缺点。

#### Samtools 软件
顾名思义就是用于处理sam与bam格式的工具软件，能够实现二进制查看、格式转换、排序及合并等功能，结合sam格式中的flag、tag等信息，还可以完成比对结果的统计汇总。同时利用linux中的grep、awk等操作命令，还可以大大扩展samtools的使用范围与功能。

### Samtools 基本命令
####1 view
- 作用
查看sam文件（sam 格式转bam）
- 格式
```
$ samtools view [options] <输入bam文件>
```
- 主要参数
-b：以bam格式输出
-u：以未压缩的bam格式输出，一般与linux命令配合使用
-h：在sam输出中包含header信息
-H：只输出header信息
-f [INT]：只输出在比对flag中包含该整数的序列信息
-F [INT]：跳过比对flag中含有该整数的序列
-o [file]：标准输出结果文件
- 标准sam/bam 文件

![image.png](http://upload-images.jianshu.io/upload_images/6634703-231b2d70e71c91e9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. read名称，通常包括测序平台等信息
2. SAM标记（Flag），没有mapping的标记为“ * ”
3. chromosome
4. 比对上的位置，注意是从1开始计数。
5. MAPQ（mapping quality，描述比对的质量，数字越大，特异性越高，说明该read比对到参考基因组上的位置越唯一）
6. CIGAR字串，记录插入，删除，错配以及splice junctions（后剪切拼接的接头）
7. mate名称，记录mate pair信息
8. mate的位置
9. 模板的长度
10. read序列
11. read质量
12. 程序用标记
####2 flagstat
- 作用
统计bam文件中的比对flag信息，并输出比对统计结果
- 格式
```
$ samtools flagstat <输入bam文件>
```
- Flag 标签说明
在sam/bam文件中输出的比对falg信息，是这条reads符合含义的十进制数值之和，网上也有许多在线工具可以通过输入结果flag值来标识出其对应的所有含义。
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6913033c821c076f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-934af12a3c9801b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
total：分析的总reads数（bam文件所有行数）
mapped：比对上的reads数（总体比对率）
paired in sequencing：成对的reads总数
read1：属于reads1的reads数量
read2：属于reads2的reads数量
properly paired：正确配对的reads数量
with itself and mate mapped：一对reads均比对上的reads数
singletons：只有单条reads比对上的reads数
以上计数均以reads条数计，一对reads计为两条。
####3. sort
- 作用
根据左起位点对序列排序，并输出为bam文件
- 格式
```
$ samtools sort [options] <输入bam文件> <输出bam文件名>
```
- 主要参数
-n：以reads名称排序而不是以比对上染色体位置排序
-m [INT]：设定内存使用量（默认值为500000000）
####4. merge
- 作用
将多个排序后的序列文件合并为一个文件
- 格式
```
$ samtools merge [options] <输出bam文件> <输入bam文件1> <输入bam文件2>…
```
- 主要参数
-n：指定输入文件是以reads名称排序的（与sort中的-n参数配合使用）
-h [file]：将file文件中的header信息拷贝到输出的bam文件中
####5. index
- 作用
对排序后的序列建立索引，并输出为bai文件，用于快速随机处理。在很多情况下，特别是需要显示比对序列的时候，bai文件是必不可少的，例如之后的tview命令
- 格式
```
$ samtools index <排序后的bam文件>
```
####6. tview
- 作用
以文本定位查看器的方式来展示各条reads的比对情况
- 格式
```
$ samtools tview [options] <排序后的bam文件> [参考基因组fasta文件]
```
- 主要参数
-p [chr:position]：直接从该染色体上的该位置开始查看
-s [string]：只显示该样品或组别的reads

![image.png](http://upload-images.jianshu.io/upload_images/6634703-e9bb7b4c44f84ea2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
第一行为参考序列的碱基坐标，第二行为参考序列，第三行开始即为按排序顺序依次比对上参考序列的各条reads，其中仍以碱基字符表示的则是与参考序列有差异的部分。

![image.png](http://upload-images.jianshu.io/upload_images/6634703-96fb23f0dc2df04b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
同时，还可以在该界面中按g键，并在出现的方框内输入想要查看的参考序列名及对应位置信息就可以快速跳转到该位置上了。
####7. depth
- 作用
计算每个位点的深度值（所有reads中包含该点的总数）
- 格式
```
$ samtools depth [options] <排序后的bam文件1> <排序后的bam文件2>…
```
- 主要参数
-q [int]：基础reads质量阈值
-Q [int]：mapping质量阈值
-r [chr:from-to]：选择需要统计深度的区域
- 示例
从左到右依次为参考基因组、在基因组上的位置、深度值。

![image.png](http://upload-images.jianshu.io/upload_images/6634703-0e38386e6629efda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####8.cat
- 作用
将多个bam文件合并为一个bam文件（与之前merge命令的区别是cat不需要将bam文件提前进行排序）
-格式
```
$ samtools cat [options] <输入bam文件1> <输入bam文件2>…
```
- 主要参数
-h [sam文件]：将该文件中的header信息提取输出到结果文件中
-o [输出bam文件]：将结果输出到该文件中
###参考文献
1. https://mp.weixin.qq.com/s?src=3&timestamp=1509366175&ver=1&signature=YQpqTHl4WpYahQH2jvnkPWMm3-T9BnyoL5l9GZy2AhcBOn1qHmWpWm3u2w7E8gZFK-LHFNbyKxP7c0ZpkJ-hMK70KRS78H9ZCOKoiKdPRVMJzmxVlyG6whwPq2G2cwl2Z-zAlHAmVNlc4BAQSOkDevhuNwi*6AvI1jS9y-EoDEs=t
