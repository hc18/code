>图代码来源《R数据可视化手册》
####1. 条形图
```
library(ggplot2)
library(gcookbook)

csub <- subset(climate, Source=="Berkeley" & Year >= 1900)
csub$pos <-csub$Anomaly10y >=0
ggplot(csub, aes(x=Year, y = Anomaly10y, fill=pos))+geom_bar(stat="identity", position="identity")
``` 
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f3144226763f738a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
library(ggplot2)
library(gcookbook)
csub <- subset(climate, Source=="Berkeley" & Year >= 1900)
csub$pos <-csub$Anomaly10y >=0
ggplot(csub, aes(x=Year, y = Anomaly10y, fill=pos))+geom_bar(stat="identity", position="identity", colour="black", size=0.25)+scale_fill_manual(values=c("#CCEEFF","#FFDDDD"), guide=FALSE)
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-e43780392b251c24.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
