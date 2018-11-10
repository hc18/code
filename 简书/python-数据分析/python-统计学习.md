```
import pandas
data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")
# 查看数据
data
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d1db51b28be7314b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
data.shape  # 40行8列
data.column # 有几列
# 简单选择器
data[data['Gender'] == 'Female']['VIQ'].mean() # 109
```
- groupby: 根据类别变量的值拆分dataframe:
