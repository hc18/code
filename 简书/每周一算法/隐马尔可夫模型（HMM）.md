####马尔可夫链
![image.png](https://upload-images.jianshu.io/upload_images/6634703-30251b77b8c1237e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-14817c373f97c578.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####隐马尔可夫
- 一个直观的例子
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9bbc677305c743a7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1ca3dc3de4d5b324.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 找概率高的那条线
- 同过观察值（Kiss,Beat,do nothing）推断出女友三天的心情是（happy,happy,unhappy）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-67ffa84db2e667d2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d4af30418503c242.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-0ae82d64d6282c90.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-af2a8003de4a9a08.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-43ec252043bf41bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9ab040d3928ba555.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####用隐马尔可夫模型建模
- 给一条序列预测其中的编码区
![image.png](https://upload-images.jianshu.io/upload_images/6634703-523aa8f430b0158f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-0509beb43dd21cea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d1e9fd98b0dee80c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-065487cf6f69a381.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ec1bb5cdc626e606.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 这里用log,把 n*c 变成了a+c
![](https://upload-images.jianshu.io/upload_images/6634703-35b345679a06f691.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 找回溯
![image.png](https://upload-images.jianshu.io/upload_images/6634703-078c43f7b8a002f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 得到最终结果
![image.png](https://upload-images.jianshu.io/upload_images/6634703-7f5ca88de379d66a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####python 简单实现
```
import numpy as np

seq="CGAAAAAATCG"
# nocoding ,coding
states = ('N', 'C')
observations = ('A', 'C', 'G','T')
# 状态转移矩阵A
transition_probability = {
    'N': {'N': 0.8, 'C': 0.2},
    'C': {'N': 0.4, 'C': 0.6},
}
# 观测概率矩阵B
emission_probability = {
    'N': {'A': 0.2, 'C': 0.3, 'G': 0.3,'T':0.2},
    'C': {'A': 0.4, 'C': 0.2, 'G': 0.2,'T':0.2},
}

array =np.zeros((len(states),len(seq)+1))

array[0,0]=0.8
array[1,0]=0.2
for i in range(1,array.shape[1]):
    if array[0,i-1]>array[1,i-1]:
        array[0,i]=array[0,i-1]*emission_probability['N'][seq[i-1]]
        array[1,i]=array[0,i-1]*emission_probability['C'][seq[i-1]]
    else:
        array[0, i] = array[1,i-1] * emission_probability['N'][seq[i - 1]]
        array[1, i] = array[1,i-1] * emission_probability['C'][seq[i - 1]]
    print(array)
list=[]
for i in range(1,array.shape[1]):
    if array[0,i]>array[1,i]:
        list.append('N')
    else:
        list.append('C')

print(seq)
print("".join(list))
```
```
[[8.000000e-01 2.400000e-01 7.200000e-02 1.440000e-02 5.760000e-03
  2.304000e-03 9.216000e-04 3.686400e-04 1.474560e-04 5.898240e-05
  1.769472e-05 5.308416e-06]
 [2.000000e-01 1.600000e-01 4.800000e-02 2.880000e-02 1.152000e-02
  4.608000e-03 1.843200e-03 7.372800e-04 2.949120e-04 5.898240e-05
  1.179648e-05 3.538944e-06]]
CGAAAAAATCG
NNCCCCCCCNN
```

