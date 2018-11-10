# 转录组入门二，读文献下数据
- 在NCBI查文章：

AKAP95 regulates splicing through scaffolding RNAs and RNA processing factors. Nat Commun 2016 Nov 8;7:13347. PMID: 27824034

- 找数据地址
![image.png](http://upload-images.jianshu.io/upload_images/6634703-cbd82c97a59618ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 去GSE网站，搜GSE81916
![image.png](http://upload-images.jianshu.io/upload_images/6634703-c8753ca8477a396d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9cb38eaee48e7df3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 下载代码

```javascript
# 在终端运行
#用axel下载会快一些
brew install axel
for i in {56..62}
do
# 也可以用wget 下载
axel ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByStudy/sra/SRP/SRP075/SRP075747/SRR35899$i/SRR35899$i.sra
done
```
##参考文献：
1. http://www.biotrainee.com/thread-1908-1-1.html
