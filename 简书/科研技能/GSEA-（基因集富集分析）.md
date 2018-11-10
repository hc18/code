####1. GSEA 介绍
- 基因集富集分析（Gene Set Enrichment Analysis，GSEA）是麻省理工学院和哈佛大学的broad institute研究团队开发的一个针对全基因组表达谱芯片数据进行分析的工具。基本思想是使用预定义的基因集，将基因按照在两类样本中的差异表达程度排序，然后检验预先设定的基因集合是否在这个排序表的顶端或者底端富集。基因集合富集分析检测基因集合而不是单个基因的表达变化，因此可以包含这些细微的表达变化，预期得到更为理想的结果。
![我们原来是双边检验，只要显著差异表达基因](https://upload-images.jianshu.io/upload_images/6634703-f0652a104459209f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![基因set 可以优化预期结果](https://upload-images.jianshu.io/upload_images/6634703-2b8796f2bfa5dcd3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. 下载安装
- 官网 ： （http://software.broadinstitute.org/gsea/register.jsp）
- 需要java环境
####3. 使用
![](https://upload-images.jianshu.io/upload_images/6634703-0a81fdc34225644f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. 实现
1. 表达谱矩阵
![](https://upload-images.jianshu.io/upload_images/6634703-537ad57a4080c112.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 样本表型文件
![23个样本，2个groups，1 是固定的](https://upload-images.jianshu.io/upload_images/6634703-e05cbdfcb2f66963.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 导入这两个数据集
![image.png](https://upload-images.jianshu.io/upload_images/6634703-28bed2992a86c9c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-eee456cdb1eb541a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. 结构展示
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6d40031e5b0bfe73.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-43dc6ef104299d03.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/6634703-1fd24aca11052fd4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





