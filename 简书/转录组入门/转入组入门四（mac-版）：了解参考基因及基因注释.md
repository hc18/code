##作业要求
在UCSC下载hg19参考基因组，从gencode数据库下载基因注释文件，并且用IGV去查看你感兴趣的基因的结构，比如TP53,KRAS,EGFR等等。
作业，截图几个基因的IGV可视化结构！还可以下载ENSEMBL，NCBI的gtf，也导入IGV看看，截图基因结构。了解IGV常识。
###转录组文章分析思路
- 好的文章不是靠写出来的，而是设计出来的。没有开始实验之前，就要先用一系列的假设去推导可能出现的结论，进行整体的构思。
- 转录组测序的文章的核心内容是实验组与对照组的差异基因分析，无论是常见的发育调控、环境适应、免疫互作都离不开这部分核心的分析。
1. 研究结果第一部分：转录组测序的实验设计中一般都会有一部分生理生化的实验结果，可能是电镜图片，可能是生理指标的变化，可能是有效物质的含量。
2. 研究结果第二部分：根据生理生化指标选择了几个样本进行转录组测序？测了4G,6G数据量? 测序质量是否良好？检测到3000个基因表达？样本特异表达的基因有多少？
3. 研究结果第三部分：差异分析组合间有多少差异基因？不同差异组合共有和特有的基因数量有多少？不同样本表达模式的差异怎样？
4. 研究结果第四部分：差异分析组合间差异基因主要是那些基因家族？转录因子？KEGG通路？GO分类？这些研究结果需要去解释这生理生化指标的变化的原因
###下载参考基因组
- 登陆网站 http://genome.ucsc.edu/index.html 下载hg19参考基因组

![image.png](http://upload-images.jianshu.io/upload_images/6634703-8e0fa13985e21cb9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](http://upload-images.jianshu.io/upload_images/6634703-7186b357e49d38f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-05c1646ecb1ac804.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-a2856bd2e9d1b54b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- hg下载前是900M 左右，解压后是3G大小
```javascript
# 下载文件
axel http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/chromFa.tar.gz
#  解压文件
tar -zxvf chromFa.tar.gz
#解压后可以发现，参考序列是按照染色体号分开列出的，我们还需要把所有的序列写入到一个文件中。
cat *.fa > hg19.fa
#最后删除其他无用的文件
rm chr*.fa
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-acb24565ba212b93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 下载注释文件
- 官网：http://www.gencodegenes.org

![image.png](http://upload-images.jianshu.io/upload_images/6634703-58bd46397638648f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](http://upload-images.jianshu.io/upload_images/6634703-352de52401eba1dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![image.png](http://upload-images.jianshu.io/upload_images/6634703-cfbe0d2d0e99f851.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```javascript
# GTF格式主要是用来描述基因的注释
axel ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_27/GRCh37_mapping/gencode.v27lift37.annotation.gtf.gz
# GFF文件是一种用来描述基因组特征的文件，现在我们所使用的大部分都是第三版）（GFF3）
axel ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_27/GRCh37_mapping/gencode.v27lift37.annotation.gff3.gz
# 解压并删除原来的文件
gzip -d gencode.v27lift37.annotation.gtf.gz
gzip -d gencode.v27lift37.annotation.gff3.gz
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-28c040390ad706d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###IGV软件的下载和安装
- IGV软件全称：Intergrative Genomics Viewer 是一个高效的查看基因数据的可视化软件。
- 官网：http://software.broadinstitute.org/software/igv/home

![image.png](http://upload-images.jianshu.io/upload_images/6634703-1a5ca22e6f1e20ca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 安装igv 之前需要先安装java 8 以上版本
- 官网：https://java.com/en/download/mac_download.jsp

![image.png](http://upload-images.jianshu.io/upload_images/6634703-5f170402a5849cf8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### IGV软件的使用
#### 窗口

![image.png](http://upload-images.jianshu.io/upload_images/6634703-a28453c530982e6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
主窗口布局： 
1. tool bar（工具栏），menu bar（菜单栏），pop-up menus（弹出式菜单）
2. 染色体上的红色盒子表示显示这部分染色体，显示完整染色体是红框会消失
3. 尺度显示了染色体的可见部分，刻度线显示了染色体的位置，跨度列表显示了当前显示的碱基的数量 
4. IGV在水平行显示的数据称为tracks。通常,每个tracks代表一个样本或实验。这个例子展示了甲基化、基因表达、拷贝数，LOH和突变数据 
5. IGV也显示某些特性,比如在tracks中的基因。默认情况下,IGV在一个面板显示数据，在另一个面板显示数据特性。拖放一个track名称，将一个track从一个面板移动到另一个地方 
6. Track名称列在最左边面板。名字的易读性取决于 tracks的高度，例如，track越小，它的名字的可读性越小
7. 属性名称被列在顶部的属性面板。彩色块代表属性值,每个独特的值被都有一个独特的颜色。鼠标放在一个颜色块的附近来查看其属性值
#### 导入参考基因组及注释信息，查看感兴趣基因的结构
- 导入前面的 hg19.fa

![image.png](http://upload-images.jianshu.io/upload_images/6634703-4349b35c322dee2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 接着导入gtf文件，需要先sort，才能导入

![image.png](http://upload-images.jianshu.io/upload_images/6634703-cbf9bfd9fb04334e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![image.png](http://upload-images.jianshu.io/upload_images/6634703-4e2a902d55496843.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

-现在可以导入sort 后的gtf 文件了。

![image.png](http://upload-images.jianshu.io/upload_images/6634703-28184bfa1a8adc7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 高通量测序图解见下章分析
###参考文献
1. http://www.jianshu.com/p/48b5a0972301  (GTF/GFF文件的差异及其相互转换)
2. http://www.jianshu.com/p/3e545b9a3c68   （hoptop）
3. http://fbb84b26.wiz03.com/share/s/3XK4IC0cm4CL22pU-r1HPcQQ1lZQRc2nKQhn2SthRW24I8CZ  （greenhillman）
