####1. 删除行和列
>需求：发现样本有7个男女性别不符，需要剔除
```
import pandas as pd
import numpy as np

csvd = pd.read_table("test.vcf",header=10,na_values='.')
for i in ['BH170560-1_1303MR00098.CEL','BH170560-1_1303MR00156.CEL','BH170560-1_1303MR00385.CEL','BH170560-1_1303MR00386.CEL','BH170560-1_1303MR00488.CEL','BH170560-1_1403MR00512.CEL','BH170560-1_1403MR00578.CEL']:
    csvd.drop([i], axis=1,inplace=True)

csvd.to_csv("csvd2.vcf", sep="\t",index=False)
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-37b523558f001195.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 接着把前面10行跳过的注释文件写回来
```
head -n 10 csvd.vcf >csvd2.vcf
cat csvd1.vcf >>csvd2.vcf
```

####删除行
> 需求 把REF大于
####2 vcf 替换ID
![image.png](https://upload-images.jianshu.io/upload_images/6634703-fa973a0b0ba032ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
import vcf

with open("../PMRA.annot") as f1:
    file1 = f1.readlines()
list=[]
with open("test.vcf") as f2:
    for i in f2.readlines():
        if i.startswith("#"):
            list.append(i)
        else:
            ID=i.split()[2]
            for line in file1:
                if ID in line:
                    new_ID=(line.split()[1][1:-1])
                    line_new = i.replace(ID, new_ID)
                    list.append(line_new)

with open("test1.vcf", 'w') as f:
    for i in list:
        f.write(i)
```
