####1. 
- The average weight of a newborn child in the USA is 3.5 kg, with a standard deviation of 0.76 kg. If we want to check all children that are significantly different from the typical baby, what should we do with a child that is born with a weight of 2.6 kg?
```
from scipy import stats

nd = stats.norm(3.5, 0.76)

nd.cdf(2.6)
0.11816
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3b2c073295823630.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> If the baby is healthy, the chance that its weight deviates by at least 0.9 kg from the mean is 2*11.8 % = 23.6 %. This is not significant, so we do not have sufficient evidence to reject our hypothesis, and our baby is regarded as healthy

