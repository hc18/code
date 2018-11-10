- 有些蛋白质功能域上的序列相似，不需要全局比对
- 全局比对不能处理内含子污染问题
- 所以引入局部比对
- 局部比对就是在全局比对公式中加了一个0，不出现负分
![image.png](https://upload-images.jianshu.io/upload_images/6634703-0d487f1a3ecbcf39.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/6634703-a18f53726bb29d25.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 局部比对的最优解可能不是在最下角和最上角
![image.png](https://upload-images.jianshu.io/upload_images/6634703-2cc86f31d3903598.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-7a3c845c9eed401f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import numpy as np

# match =1, gap=-2, unmatch=-1
def align(a,b):
    if a==b:
        return 2
    elif a == " " or b ==" ":
        return -5
    else:
        return -5

def mark(seq1,seq2):
    len1=len(seq1)
    len2=len(seq2)
    # 初始化举证
    Matrix=np.zeros((len1+1,len2+1))
    # 第一行和第一列赋值
    Matrix[0,:]=[-5*x for x in range(len2+1) ]
    Matrix[:,0]=[-5*x for x in range(len1+1) ]
    # 把负数变为0
    Matrix[Matrix<0]=0
    # 在字符串前面添加空格
    seq1 = " " + seq1
    seq2 = " " + seq2
    # 填充矩阵
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            list = [align(seq1[i], seq2[j]) + Matrix[i - 1, j - 1],\
                    -5 + Matrix[i - 1, j],\
                    -5 + Matrix[i, j - 1]]
            Matrix[i, j] = max(list) if max(list)>0 else 0
    return Matrix

def back(seq1,seq2,Matrix,i,j,S1,S2,t1,t2):
        max1=max(Matrix[j-1,i-1], Matrix[j-1,i],Matrix[j,i-1])
        if max1 == 0:
            S1.append(seq1[j]+t1[:])
            S2.append(seq2[i]+t2[:])
            return
        if max1==Matrix[j-1,i-1]:
            back(seq1,seq2,Matrix,i-1,j-1,S1,S2,seq1[j] + t1[:], seq2[i] + t2[:])
        if max1==Matrix[j-1,i]:
            back(seq1,seq2,Matrix, i, j-1,S1,S2,seq1[j] + t1[:], "-" + t2[:])
        if max1 == Matrix[j,i-1]:
            back(seq1,seq2,Matrix, i-1, j,S1,S2, "-" + t1[:], seq2[i] + t2[:])

def main():
    seq1 = "ATCGATC"
    seq2 = "ATC"
    Matrix=mark(seq1, seq2)
    print(Matrix)
    list = np.where(Matrix == np.max(Matrix))
    S1=[]
    S2=[]
    t1=""
    t2=""
    # i=col,j=row
    for i,j in list:
        back(" ATCGATC"," ATC",Matrix,i,j,S1,S2,t1,t2)
    print(S1)
    print(S2)
if __name__=='__main__':
    main()
```
```
[[0. 0. 0. 0.]
 [0. 2. 0. 0.]
 [0. 0. 4. 0.]
 [0. 0. 0. 6.]
 [0. 0. 0. 1.]
 [0. 2. 0. 0.]
 [0. 0. 4. 0.]
 [0. 0. 0. 6.]]
['ATC', 'ATC']
['ATC', 'ATC']
```
