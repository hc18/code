>刷题ROSALIND，练编程水平
http://rosalind.info/problems/list-view/
#1 Counting DNA Nucleotides(AGCT计数)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-e8edbea2bf1abecb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 题目解读： 
  - 给定一个DNA序列，数各碱基出现次数
```
#方法一
f = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
for i in f:
    b = list(f)    # 把‘AAA’变成 ['A','A'',A']
    c = {}
    for i in b:
        c[i] = b.count(i)   # 把key 和value 写入字典，如 A：1
print (c)  

{'A': 20, 'G': 17, 'C': 12, 'T': 21}
```
```
#方法二
f = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
counts = []
for i in ['A','C','G','T']:          # 把输出的顺序定好
    counts.append(f.count(i))
print ('\t'.join(map(str, counts)))  #map() 这里的意思是吧输出的[20,12,17,21]变为 20 12 17 21
```
#2. Transcribing DNA into RNA （DNA 转RNA）
![image.png](http://upload-images.jianshu.io/upload_images/6634703-80c995a5c0220bd0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 题目解读
  - 把T变成U
```
str = 'GATGGAACTTGACTACGTAAATT'
print (str.replace('T','U'))

GAUGGAACUUGACUACGUAAAUU
```
#3. Complementing a Strand of DNA（DNA 的互补链）
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b72324b16b9e0857.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 题目解读
  - 先把 AAAACCCGGT 读成 TTTTCCCGGA，然后用reverse函数转置成
ACCGGGTTTT
```
def reverse(seq):
    dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
 
    revSeqList = list(reversed(seq))                #['T', 'G', 'G', 'C', 'C', 'C', 'A', 'A', 'A', 'A']
    revComSeqList = [dict[k] for k in revSeqList]  # ['A', 'C', 'C', 'G', 'G', 'G', 'T', 'T', 'T', 'T']
    revComSeq = ''.join(revComSeqList)             # ACCGGGTTTT
    return revComSeq
seq = 'AAAACCCGGT'
 
print (reverse(seq))

ACCGGGTTTT
```
```
seq = 'AAAACCCGGT'
# [::-1] 倒着读seq
rev_seq=seq[::-1].replace('C', 'g').replace('G', 'c').replace('T', 'a').replace('A', 't').upper()
print(rev_seq)
```
#4. Rabbits and Recurrence Relations（兔子与递归关系？）
![image.png](http://upload-images.jianshu.io/upload_images/6634703-2b4dd35c4e762613.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 题目解读
- F1 = 1，  F2 = 1， F3 = F2+F1*2

| k        |  1  |  2  | 3|4|5|
    | :--------:    | :-----:   | :----: |:----: |:----: |:----: |
    | 总兔子        | 1      |   1    | 4|7|19|
```
方法一：
 
def fibonacciRabbits(n, k):
    F = [1, 1]
    generation = 2
    while generation <= n:
        F.append(F[generation - 1] + F[generation - 2] * k)
        generation += 1
    # 函数返回列表最后一项
    return (F[n - 1])

#调用函数并打印
print (fibonacciRabbits(5, 3))
 ```
```
方法二：
 # 迭代思想
def fibonacciRabbits(n,k):
    if n <= 2:
        return (1)
    else:
        return (fibonacciRabbits(n-1,k) + fibonacciRabbits(n-2,k)*k)
print (fibonacciRabbits(5,3))
```
#5. Computing GC Content （GC含量计算）
![image.png](http://upload-images.jianshu.io/upload_images/6634703-8676c17a056c2277.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 题目解读
  - 建立一个Computing_GC_Content.txt文件，和python 脚本放一起
  - 数GC含量
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5c2440f6bdaa02f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
### 5. Computing GC Content ###
from operator import itemgetter
from collections import OrderedDict
# 创建两个有序的字典
seqTest = OrderedDict()
gcContent = OrderedDict()

with open('Computing_GC_Content.txt', 'rt') as f:
    for line in f:
        # 去除右边的空格
        line = line.rstrip()
        if line.startswith('>'):
            # 读取名字，不要">",所以从1开始
            seqName = line[1:]
            # 把名字放入字典
            seqTest[seqName] = ''
            # 结束本次循环，进入下一个循环
            continue
        # 每行字母都大写加入字典
        seqTest[seqName] += line.upper()

for ke, val in seqTest.items():
    # 所有的碱基
    totalLength = len(val)
    # G和C的碱基和
    gcNumber = val.count('G') + val.count('C')
    # 算GC含量
    gcContent[ke] = (float(gcNumber) / totalLength) * 100
# 字典排序
sortedGCContent = sorted(gcContent.items(), key=itemgetter(1))
# 取字典最后一个的名字，即 Rosalind_0808
largeName = sortedGCContent[-1][0]
# 取GC含量的比值
largeGCContent = sortedGCContent[-1][1]

print('most GC ratio gene is %s and it is %s ' % (largeName, largeGCContent))

most GC ratio gene is Rosalind_0808 and it is 60.91954022988506
```
- 欢迎交流

