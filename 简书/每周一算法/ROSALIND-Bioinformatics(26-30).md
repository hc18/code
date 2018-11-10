>刷题ROSALIND，练编程水平
http://rosalind.info/problems/list-view/
# 26. Perfect Matchings and RNA Secondary Structures(RNA二级结构的完美匹配)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6876a568832a414f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - A与U，C与G出现的次数相等，求完全匹配总数
  - 求出A与U匹配的总数乘以C与G匹配的总数
```
import math
stseq = ''
for line in open('26_Perfect_Matchings_and_RNA_Secondary_Structures.txt'):
    if line[0] == '>':
        if stseq != '':
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')

n1 = stseq.count('A')
n2 = stseq.count('C')
# 求阶乘
print (math.factorial(n1)*math.factorial(n2))

12
```
# 27. Partial Permutations(部分排列)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-c119387444948123.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 从n 个数中提取k个排列然后取模

```
import math
n = 21
k = 7
print (round(math.factorial(n)/math.factorial(n-k)%1000000))

51200
```
# 28.  Introduction to Random String(介绍随机字符窜)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d553baf7698f894b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 第一行为给定DNA字符串，不长于100bp
  - 第二行为不多于20个的0~1之间的浮点数，表示GC含量
  - 为方便表示，要求输出log10后的值,保留三位小数
```
from math import log10

with open('28_Introduction_to_Random_Strings.txt') as input_data:
	dna, gc_content = input_data.readlines()

gc_content = map(float, gc_content.split())

codon_count = [0, 0]
for codon in dna:
	if codon in ['C', 'G']:
		codon_count[0] += 1
	elif codon in ['A', 'T']:
		codon_count[1] += 1

gc_prob = []
for gc_value in gc_content:
    # 例如GC含量为0.4，则A、T的概率为0.3，C、G的概率为0.2
	log_prob = codon_count[0]*log10(0.5*gc_value) + codon_count[1]*log10(0.5*(1-gc_value))
	gc_prob.append(str(round(log_prob,3)))

print(gc_prob)

['-5.737', '-5.217', '-5.263', '-5.36', '-5.958', '-6.628', '-7.009']
```
# 29. Enmuerating Oriented Gene Orderings(双向基因排序)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-1b994b4494983ae2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 1～n个数+（+，-）的任意排列
```
from itertools import product, permutations

n = 2

signed_ints = []
for i in range(1, n + 1):
    signed_ints.append([-1 * i, i])
# '*'的作用是把列表解开生成两个独立的参数
# product 将两个参数重新组合
product_list = map(list, list(product(*signed_ints)))
signed_perm_list = []

for ordered_perm in product_list:
    signed_perm_list += map(list, list(permutations(ordered_perm)))
print(len(signed_perm_list))

for signed_perm in signed_perm_list:
    print(' '.join(map(str,signed_perm)))
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9456110b5b8f8be2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#30. Finding a Spliced Motif(找到不连续的模版)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-2276fda3e8b02a1e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 找到不连续的模版
```
import regex
str ='ACGTACGTGACG'
match1 = regex.finditer(r"(G)\w+(T)\w+(A)",str, overlapped=True)
for match in match1:
    print(match)

<regex.Match object; span=(2, 10), match='GTACGTGA'>
```
- 感觉题目明显变难，逻辑跟不上了，去补充一些知识，回头再补上这个系列

