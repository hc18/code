![image.png](https://upload-images.jianshu.io/upload_images/6634703-a5f922080e050f3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d9ca598f0f6e37e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6d1391b284584cc3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 先填最靠边的两排，空位罚分为-5， 
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dcc8e320302594d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 然后填中间的格子，取F()最大的填
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9d54425ea0b83141.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/6634703-c5890d009e994dda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 从箭头返回，找到最优比对
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6b9d9e63c9a38ccb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####python 实现
```
import  numpy as np

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
    # 在字符串前面添加空格
    seq1=" "+seq1
    seq2=" "+seq2
    # 填充矩阵
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            list=[align(seq1[i],seq2[j])+Matrix[i-1,j-1],\
                  -5+Matrix[i-1,j],\
                  -5+Matrix[i, j-1]]
            Matrix[i,j]=max(list)
    return Matrix

#回溯
def traceback(seq1, seq2, match, n_match, gap, S, current_x, current_y, S1, S2, t1, t2):
    # 用if可以得到多解，elif 唯一解
    if current_x == 0 and current_y == 0:
        # S1纪录比对情况集合，t1纪录每种比对情况
        S1.append(t1[:])
        S2.append(t2[:])
        return
    # 回调函数，找回路径
    if S[current_x,current_y]-S[current_x-1,current_y] == gap:
        traceback(seq1, seq2, match, n_match, gap, S, current_x-1, current_y, S1, S2, seq1[current_x]+t1[:], "-"+t2[:])
    if S[current_x,current_y]-S[current_x,current_y-1] == gap:
        traceback(seq1, seq2, match, n_match, gap, S, current_x, current_y-1, S1, S2, "-" + t1[:], seq2[current_y] + t2[:])
    if S[current_x,current_y]-S[current_x-1,current_y-1] == align(seq1[current_x], seq2[current_y]):
        traceback(seq1, seq2, match, n_match, gap, S, current_x-1, current_y-1, S1, S2, seq1[current_x] + t1[:], seq2[current_y] + t2[:])

def main():
    seq1 = "AGC"
    seq2 = "AAG"
    Matrix=mark(seq1,seq2)
    print(Matrix)
    S1 = []
    S2 = []
    t1 = ""
    t2 = ""
    traceback(" AGC", " AAG", 2, -5, -5, Matrix, Matrix.shape[0] - 1, Matrix.shape[1] - 1, S1, S2, t1, t2)
    print(S1)
    print(S2)

if __name__=='__main__':
    main()
```
```
[[  0.  -5. -10. -15.]
 [ -5.   2.  -3.  -8.]
 [-10.  -3.  -3.  -1.]
 [-15.  -8.  -8.  -6.]]
['A-GC', '-AGC']
['AAG-', 'AAG-']
```
####参考文献
1. https://blog.csdn.net/jining11/article/details/81394021
