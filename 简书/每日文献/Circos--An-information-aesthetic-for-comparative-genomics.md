![image.png](https://upload-images.jianshu.io/upload_images/6634703-8c30e6cb09830188.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######1. 作者为什么要创造Circos软件？（1-2段）
- 因为随着人们快速的收集基因组序列相关的数据，比如（甲基化,组蛋白修饰,snp,indel,sv,基因表达），数据的储存，加工，分析和可视化也暴露出了很多问题，所以，这位大神，就以可视化为落脚点，发明了这个Circos.
- 作者创造这个可视化工具的三个原则：
1. adapt to the density and dynamic range of the data
2. maintain complexity and detail in the data
3. scale well without sacrificing clarity and specificity.
######2. 举例加强论证（3段）
- 很多东西，不是自己觉得好就是好的。所以作者举例了以前大牛们发明了一些可视化工具，都很好的解决了可视化问题，所以发明这个可视化工具是很有意义，也很有必要的。（我个人觉得，这段其实可以省略，占篇幅）
######3.  目前这个领域的问题 （4 段）
- 以前人们用 “线性排列” 看二维数据， 色彩空间（色相，饱和度，明亮）看三维数据(Baran et al. 2007).
- 如果线条数据少，就用线性排列; 如果线条数据多了，会显得很乱，就用不同颜色的色彩区块对应不同的线，来减轻视觉压力;但是色彩空间减少了数据文理和丰富度，所以作者发明了Circos
- 与此同时，2004年也有一篇论文指出，需要用循环的圆圈来显示基因关系结构 (告诉编辑，我这软件是有市场需求的~)
######4. Circos 软件介绍 （5-7段）
- 应用：解决大基因组的挑战
- 功能强大，可用于大规模多试样基因组数据
- circos 已经是一个成熟的软件包，并在可以在网上调试
######5. 结果展示
![image.png](https://upload-images.jianshu.io/upload_images/6634703-baf73d173caf78c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 最外圈是染色体的示意图，数字表示染色体的长度，以第一条染色体为例，由于chr1的length=249250621，我们以1Mbp为单位，那刻度范围就为0~249。
2. A-E 是1个肿瘤样本全基因图谱的5个copy
3. 把 F区放大到图像的中心，G 表示穿过250个相邻探针的平均探针值，绿色为正值，红色为负值，H为最大值，L为最小值
> 从图中可见，5个拷贝总体上一样，但是D copy 的第六号染色体上拷贝数突然变化，而且B copy 的第17号染色体峰值突然增加。 为了更详细地探索这些区域，请看下图~

![image.png](https://upload-images.jianshu.io/upload_images/6634703-513a9f8fb0c9bab1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 把染色体6和17放大
2. 把A 区域 和 B区域 放大10倍映射到 C区域和D区域（F →G（5倍），H→J，I→K（40倍） ）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e467fbb11a225a56.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 把放大后的A, B, J, K 再拼起来
######6. 讨论
1. Circos 可以生成清晰和信息丰富的图像，对研究者有很大的吸引力。
2. Circos 基因位置可拓展，可以灵活的重现排列图像，每个图像都有详细特征
######7. 我的总结
1. Circos 是GWAS 分析的利器之一。许多人都选择它来展示测序数据。每一个切块代表一个染色体，每一层代表染色体的一类信息。另外它具有可个性化展示SNP密度、基因密度、基因组多样性、GC比例、染色体共线性等优点，因而备受广大科研工作者的追捧。
######8. 参考文献
1. https://www.ncbi.nlm.nih.gov/pubmed/19541911
2. https://mp.weixin.qq.com/s?src=3&timestamp=1526003592&ver=1&signature=7cqWbymcWEdgAhVSiZIhmCwuqaxKtL8jGsy6IyOdBVZZvIyExHq-50FBP2PW6iClKHsgBO2D21ypmbbiIni1M2V11wvRguHdBFHwe80D1jDKHWgziBbZiDTQVLtx-vamNBOPow2LTQZGWBbgf94O21ZVcTW3OTW2hSQJBHIFmFQ=
3. http://circos.ca/ (官网)
4. https://mp.weixin.qq.com/s?src=11&timestamp=1526003513&ver=869&signature=H1Z0afQMWpT8TOHgVa3oe6IV3yPxOUvPlgR4KJWZQJkm9RFZa7SQEAjIzM090eGxKVEFrqG*dvAU0XZFRRQ1pbQO2EgXR2QHuvDp11eiDzNAEn6wj-ULmyutg6AmYKTa&new=1
