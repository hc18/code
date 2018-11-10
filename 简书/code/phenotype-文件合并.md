> 1. 有两个不同格式的phenotype 合并， MRI_ID 对应 IID的后五位数字
>  2. 样本大小不一样（一个580，一个470）
>  3. 样本顺序也不一样
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d933fb9b5476de72.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d54280b85be5a6e9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import pandas as pd

# 读取 txt 文件
file1 = pd.read_table("phone.txt",sep='\t',header=0,na_values='.')
# 读取excel 文件，设置index
file2 = pd.read_table("phenotype.txt",sep='\t',header=0,na_values='.',index_col='MRI_ID')

# 把1303MR00001 读取 00001 作为index
MRI_ID=[]
for i in file1['IID']:
    MRI_ID.append(int(i[6:11]))
file1['MRI_ID']=MRI_ID

# file2 有580 人，file1 有475 人， 所以筛选
file3 = file2.loc[MRI_ID]

# 以MRI_ID 为index 拼接
results=pd.merge(file1,file3,how='left',on='MRI_ID')
# 去掉MRI_ID 这一列
results=results.drop('MRI_ID', axis=1)
results.to_csv('results.txt',sep='\t',index=False)
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-3fd26d000f478cf7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
