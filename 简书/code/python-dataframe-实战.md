####1
> 需求，把NAN值大于50%的行与列删除，剩下的NAN用这一列最小值的1/2填补
```
import pandas as pd
import numpy as np
df=pd.read_csv('ost20180713.csv',header=None,sep=',')
rows,cols=df.shape

# 删除行
for i in range(rows):
    if df.loc[i].count()<int(cols/2):
        df.drop([i],inplace=True)
#删除列
for i in range(cols):
    if df[i].count()<int(rows/2):
        df.drop([i],inplace=True,axis=1)
#重新编号行与列
new_rows,new_cols=df.shape
df.reset_index(drop=True, inplace=True)
df.columns=[num for num in range(new_cols)]
#取最小的1/2 填充
for i in range(1,new_cols):
    a=df[i][1]
    for j in df[i][1:6]:
        if j == 0 or a == 0:
            pass
        elif j is np.nan:
            pass
        elif a > j:
            a = j
    c = float(a) / 2
    df = df.fillna({i: c}, inplace=True)
print(df)

df.to_csv("ost_laomei.csv")
```
