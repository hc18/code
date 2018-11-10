####1. 关键基因（hub gene）
- 关键基因（hub gene）是在生物学过程中发挥至关重要作用的基因，在相关通路中，其他基因的调控往往要受到该基因的影响
- 因此， hub gene 往往是重要的作用靶点和研究热点
- 可以通过共表达或蛋白相互作用构建互作网络，然后根据网络拓扑结构筛选关键基因
####2. Cytoscape 筛选关键基因
- 通过Cytoscaoe 构建蛋白/基因的互作网络后，较多的node 和edge 往往会掩盖真正的关键基因，影响筛选过程。
- 通过算法对网络结构和节点间加权重联系的计算分析，可以筛选出重要的hub gene
####3. CytoHubba
- CytoHubba 是Cytoscape 插件
- 通过12种算法，较为准确地找到hub gene
- 安装
![image.png](https://upload-images.jianshu.io/upload_images/6634703-64c86e4737e2ad39.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 导入差异表达基因
![image.png](https://upload-images.jianshu.io/upload_images/6634703-4abe712256d70858.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![颜色越深越重要](https://upload-images.jianshu.io/upload_images/6634703-2ec3161491e3a4bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. 点击export 导出12种算法数据比较
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d548482c4e87d557.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 如果12种算法都觉得这个基因重要，说明这个基因很有研究意义，下图是12种基因重要性排序
![image.png](https://upload-images.jianshu.io/upload_images/6634703-8022ada4d7821f4a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

