##作业要求
需要用安装好的sratoolkit把sra文件转换为fastq格式的测序文件，并且用fastqc软件测试测序文件的质量！
作业，理解测序reads，GC含量，质量值，接头，index，fastqc的全部报告，搜索中文教程，并发在论坛上面。
来源于生信技能树：http://www.biotrainee.com/forum.php?mod=viewthread&tid=1750#lastpost
##实验步骤
###1. 将 sra 数据转化成 fastq 格式
先建立一个SRR_fastqc.sh 文件，写入代码
```javascript
#!/usr/bin/env bash
for i in {56..62}
do
fastq-dump --gzip --split-3 -O /Users/chengkai/Desktop/zhuanlu_files -A SRR35899${i}.sra
done
```
- --gzip 压缩格式为gzip
- --split-3 如果是双端测序输出两个文件，如果不是只输出一个文件
- -0 输出文件路径
- “/Users/chengkai/Desktop/zhuanlu_files” 这里改成你自己的文件路径
- -A 输入文件路径 
###2. 在终端运行
```javascript
# 这一步很慢，我跑了2小时，泡杯咖啡，欣赏一部电影吧
$ bash SRR_fastqc.sh 
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-097ee4876f5eec4d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###3. fastqc 检测测序文件质量

创建一个文件夹
```javascript
mkdir fastqc/
```
创建一个fastqc.sh脚本，写入如下代码
```javascript
#!/usr/bin/env bash
fastqc -o ./fastqc/ -t 8 SRR3589956_1.fastq.gz SRR3589956_2.fastq.gz
fastqc -o ./fastqc/ -t 8 SRR3589957_1.fastq.gz SRR3589957_2.fastq.gz
fastqc -o ./fastqc/ -t 8 SRR3589958_1.fastq.gz SRR3589958_2.fastq.gz
fastqc -o ./fastqc/ -t 8 SRR3589959_1.fastq.gz SRR3589959_2.fastq.gz
fastqc -o ./fastqc/ -t 8 SRR3589960_1.fastq.gz SRR3589960_2.fastq.gz
fastqc -o ./fastqc/ -t 8 SRR3589961_1.fastq.gz SRR3589961_2.fastq.gz
fastqc -o ./fastqc/ -t 8 SRR3589962_1.fastq.gz SRR3589962_2.fastq.gz
```
- -o: 输出路径
- -t: 线程数，和电脑配置有关，每个线程需要250MB 的内存
```javascript
bash fastqc.sh
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-0200f149e4affda5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###4. 质量解读
html 格式用浏览器打开
#### 基本信息
- Enconding: 测序平台版本号
- Total Sequence: reads 的数量
- Sequence length: 总的序列数
- %GC GC比，这个指标有物种意义，用于区别物种，一般人类42%
![image.png](http://upload-images.jianshu.io/upload_images/6634703-03a0984f156babeb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 每个read各位置碱基的测序质量
- 横轴碱基的位置（1-51），纵轴是质量分数，20表示1%的错误率，30表示0.1%
- 红色线代表中位数，蓝色代表平均数，黄色是25%-75%区间，触须是10%-90%区间
- Warning 报警 如果任何碱基质量低于10,或者是任何中位数低于25
- Failure 报错 如果任何碱基质量低于5,或者是任何中位数低于20

![image.png](http://upload-images.jianshu.io/upload_images/6634703-82d7efc3e193e0f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 偏离度
- 横轴碱基的位置（1-51）
- 纵轴是tail的Index编号
- 检查reads中每一个碱基位置在不同的测序小孔之间的偏离度，蓝色代表偏离度小，质量好，越红代表偏离度越大，质量越差。
- 这个图主要是为了防止，在测序过程中，某些tail受到不可控因素的影响而出现测序质量偏低
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f667619f70cca093.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####reads质量的分布
- 横轴表示Q值，0-40
- 纵轴是每个值对应的reads数目
- 当峰值小于27时，警告；当峰值小于20时，fail。我的报告峰值在38

![image.png](http://upload-images.jianshu.io/upload_images/6634703-20c21d93334f7171.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####GC 含量统计
- 横轴碱基的位置（1-51）
- 纵轴是碱基含量百分比
- 图中四条线代表A T C G在每个位置平均含量
- 当部分位置碱基的比例出现bias时，即四条线在某些位置纷乱交织，往往提示我们有overrepresented sequence的污染。
- 本结果前10个位置，每种碱基频率有明显的差别，说明有污染。
- 当任一位置的A/T比例与G/C比例相差超过10%，报"WARN"；当任一位置的A/T比例与G/C比例相差超过20%，报"FAIL"

![image.png](http://upload-images.jianshu.io/upload_images/6634703-e006fcaf29350b32.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####序列平均GC含量分布图
- 横轴是百分比； 纵轴是每条序列GC含量对应的数量

- 蓝色的线是程序根据经验分布给出的理论值，红色是真实值，两个应该比较接近才比较好
- 当红色的线出现双峰，基本肯定是混入了其他物种的DNA序列
- 偏离理论分布的reads超过15%时，报"WARN"；偏离理论分布的reads超过30%时，报"FAIL"
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6538d868b87e9a79.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 各位置N的reads比率
- 当测序仪器不能辨别某条reads的某个位置到底是什么碱基时，就会产生“N”，统计N的比率
- 正常情况下，N值非常小
- 当任意位置的N的比例超过5%，报"WARN"；当任意位置的N的比例超过20%，报"FAIL"

![image.png](http://upload-images.jianshu.io/upload_images/6634703-788592f0afc434d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### reads 长度分布
- 每次测序仪测出来的长度在理论上应该是完全相等的
- 当reads长度不一致时报"WARN"；当有长度为0的read时报“FAIL”
- 当测序的长度不同时，如果很严重，则表明测序仪在此次测序过程中产生的数据不可信 

![image.png](http://upload-images.jianshu.io/upload_images/6634703-f9d10c08c3729741.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 统计不同拷贝数的reads的频率
- 横坐标是duplication的次数，纵坐标是duplicated reads的数目,以unique reads的总数作为100%
- 测序深度越高，越容易产生一定程度的duplication，这是正常的现象，但如果duplication的程度很高，就提示我们可能有bias的存在

- 当非unique的reads占总数的比例大于20%时，报"WARN"；当非unique的reads占总数的比例大于50%时，报"FAIL"

![image.png](http://upload-images.jianshu.io/upload_images/6634703-43cabd22aa140125.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-7eb770e44bd93b4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 接头含量
- 此图衡量的是序列中两端adapter的情况
- 如果在当时fastqc分析的时候-a选项没有内容，则默认使用图例中的四种通用adapter序列进行统计
- 本例中adapter都已经去除，如果有adapter序列没有去除干净的情况，在后续分析的时候需要先使用cutadapt软件进行去接头

![image.png](http://upload-images.jianshu.io/upload_images/6634703-b59d9e8181d22c78.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 重复短序列
- 这个图统计的是，在序列中某些特征的短序列重复出现的次数
- 我们可以看到1-8bp的时候图例中的几种短序列都出现了非常多的次数，一般来说，出现这种情况，要么是adapter没有去除干净，而又没有使用-a参数；要么就是序列本身可能重复度比较高，如建库PCR的时候出现了bias
- 对于这种情况，我的办法是可以cut掉前面的一些长度，可以试着cut 1bp
![image.png](http://upload-images.jianshu.io/upload_images/6634703-0198b6d5eb3ec6d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##参考文献
1. [http://fbb84b26.wiz03.com/share/s/3XK4IC0cm4CL22pU-r1HPcQQ2irG2836uQYm2iZAyh1Zwf3_](http://fbb84b26.wiz03.com/share/s/3XK4IC0cm4CL22pU-r1HPcQQ2irG2836uQYm2iZAyh1Zwf3_) （青山屋主）
2. [www.biotrainee.com/thread-2034-1-1.html](http://www.biotrainee.com/thread-2034-1-1.html) (laofuzi)
3. [http://www.jianshu.com/p/14fd4de54402](http://www.jianshu.com/p/14fd4de54402) （lxmic）
4. [https://zhuanlan.zhihu.com/p/20731723](https://zhuanlan.zhihu.com/p/20731723) (孟浩巍)
