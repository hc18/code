> 本文主要目的是识别IMDB top100 电影的剧情简介的隐藏结构
- 主要教程包括
*   对所有剧情简介分词（tokenizing）和词干化（stemming）
*   利用 [tf-idf](http://en.wikipedia.org/wiki/Tf%E2%80%93idf) 将语料库转换为向量空间（vector space）
*   计算每个文档间的余弦距离（cosine distance）用以测量相似度
*   利用 [k-means 算法](http://en.wikipedia.org/wiki/K-means_clustering)进行文档聚类
*   利用[多维尺度分析（multidimensional scaling）](http://en.wikipedia.org/wiki/Multidimensional_scaling)对语料库降维
*   利用 [matplotlib](http://matplotlib.org/) 和 [mpld3](http://mpld3.github.io/) 绘制输出的聚类
*   对语料库进行[Ward 聚类算法](http://en.wikipedia.org/wiki/Ward%27s_method)生成层次聚类（hierarchical clustering）
*   绘制 Ward 树状图（Ward dendrogram）
*   利用 [隐含狄利克雷分布（LDA）](http://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) 进行主题建模
#### 代码实现
######1. 导入所有的库
```
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
```


