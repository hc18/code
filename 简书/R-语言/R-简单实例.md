>本文参考《R语言与Bioconductor生物信息学应用》第三章
####1. 课题背景
- 在自然界中，有些环境是普通生物不能生存的，如极端的温度、酸碱盐、压力、辐射等。然而，这里仍然有一些微生物在顽强的生活着，他们就是***极端微生物***。这些微生物对环境的特殊适应性都具有重要的研究价值，本文研究的就是***极端嗜盐古菌***，通过他的蛋白质水平寻找一些特征序列。
####2. 实验设计
  A. 将蛋白质序列批量导入
  B. 统计每条序列的氨基酸百分比
  C. 特定模序匹配与统计， 提取包含模序2此以上的蛋白质序列
  D. 对提取的序列进行两两比对
  E.  根据比对结果构建系统发生树
####3.数据的获取
![image.png](http://upload-images.jianshu.io/upload_images/6634703-7a1334797f54f6c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_genbank/Bacteria/Halobacterium_sp_uid217/AE004437.faa
```
####4. 
