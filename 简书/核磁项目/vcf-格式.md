![image.png](https://upload-images.jianshu.io/upload_images/6634703-18191084682789d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- CHROM 染色体编号
- POS 位置
- ID 基因ID
- REF 参考基因组碱基
- ALT 样本碱基
- QUAL 变异可信度，越高越好
- FILTER 是否通过过滤，pass 为通过
- INFO 
1. AC, 等位基因数量；AF，等位基因频率；AN，所有等位基因数量
2. DB，flag 判断是否属于dbsnp menbership
3. dels, 进行SNP和INDEL calling的结果中，有该TAG并且值为0表示该位点为SNV，没有则为INDEL。
4. FS，使用F检验来检验测序是否存在链偏好性。链偏好性可能会导致变异等位基因检测出现错误。输出值Phred-scaled p-value，值越大越可能出现链偏好性。
5. MQ，表示覆盖序列质量的均方值RMS Mapping Quality
- FORMAT & Pickrell
1. GT 0/1 ，样品的基因型（genotype），0/0表示sample中该位点为纯合的，和ref一致； 0/1 表示sample中该位点为杂合的，有ref和variant两个基因型； 1/1 表示sample中该位点为纯合的，和variant一致。
2. AD 和 DP：AD(Allele Depth)为sample中每一种allele的reads覆盖度,在diploid中则是用逗号分割的两个值，前者对应ref基因型，后者对应variant基因型；DP（Depth）为sample中该位点的覆盖度(一些reads被过滤掉的覆盖度)。
3. **GQ**：基因型的质量值(Genotype Quality)。Phred格式(Phred_scaled)的质量值，表示在该位点该基因型存在的可能性；该值越高，则Genotype的可能性越大；计算方法：Phred值 = -10 * log (1-p) p为基因型存在的概率。

4. **PL** 指定三种基因型的质量值。这三种指定的基因型为(0/0,0/1,1/1)，这三种基因型的概率总和为1。该值越大，表明为该种基因型的可能性越小。 Phred值 = -10 * log (p) p为基因型存在的概率。

