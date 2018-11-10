>刷题ROSALIND，练编程水平
http://rosalind.info/problems/list-view/
#21. Locating Restriction Sites(查找限制位点)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-03bf09faeceb46eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 限制性核酸内切酶用于抵御外来病毒的DNA的进攻
  - 限制性核酸内切酶的酶切位点是回文片段——其反向互补链等于本身
  - 如GATATC | CTATAG
```
s="TCAATGCATGCGGGTCTATATGCAT"

def pa_re(s):
    l=[]
    for i in s:
        if i=="G":l.append("C")
        if i=="A":l.append("T")
        if i=="T":l.append("A")
        if i=="C":l.append("G")
    l.reverse()
    re_s="".join(l)
    #print re_s
    if s==re_s:
        return 1

print (len(s))
for i in range(len(s)):
    j=4
    while i+j<=len(s):
        n=s[i:i+j]
        if pa_re(n):print (i+1,j)
        j=j+2
pa_re(s)
```
```
string = 'TCAATGCATGCGGGTCTATATGCAT'

for start in range(0,len(string)-2):
    # 回文序列长度在4-12，所以当len大于12时取12，小于4时取4
    maxle = min(14,len(string)-start)
    if maxle <= 4:
        maxle = 6
    # 回文序列必须是偶数
    for length in range(4,maxle,2):
        reverse_seq = string[start:start+length]
        #print(reverse_seq)
        #判断回文序列
        for i in range(length):
            if (reverse_seq[i]=='A' and reverse_seq[-1-i]=='T') \
            or (reverse_seq[i]=='T' and reverse_seq[-1-i]=='A')\
            or (reverse_seq[i]=='C' and reverse_seq[-1-i]=='G') \
            or (reverse_seq[i]=='G' and reverse_seq[-1-i]=='C'):
                if i == length/2:
                    print (start+1,length)
                    break
            else:
                break
```
#22. RNA Splicing(RNA 剪切)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-4ee0fd4daf7c8aa1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 用第二条和第三条和第一条匹配，把匹配到的字符窜替换为空
```
def translate_rna(sequence):
    codonTable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
    'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
    }
    proUeinsequence = ''

    for n in range(0,len(sequence),3):
        if sequence[n:n+3] in codonTable.keys():
            proUeinsequence += codonTable[sequence[n:n+3]]
    return proUeinsequence


seq_list = []
stseq = ''
for line in open('22_RNA_splicing.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)
print(seq_list)

for intron in seq_list[1:]:
    # 把匹配到的字符窜替换为""（空）
    seq_list[0]=seq_list[0].replace(intron,'')

print (translate_rna(seq_list[0]))
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-685fd171b5fd91bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#23. Enumerating k-mers Lexicographically(枚举k-mers按字典顺序排列)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-92b7f2afd696dce3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 用itertools.permutations函数
```
import itertools
list1 = ['A','C','G','T']
k = 2
b = itertools.permutations(list1,k)
c = itertools.combinations_with_replacement(list1,k)
union = list(set(b).union(set(c)))
for one in list(union):
    print(''.join(map(str,list(one))))

GG
AA
AC
AT
CT
AG
CA
GA
TG
GC
TC
CG
GT
TA
TT
CC
```
```
import itertools
list1 = ['A','C','G','T']
k = 2
b = itertools.product(list1,repeat=k)
for i in list(b):
    print(i)
```
#24. Longest Increasing Subsequence(最长升序子序列)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-1c87ee1108c54884.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 两个函数一个找升序，一个找降序
```
def increase_seq(a):
    list_down = []
    i = 0
    while i < len(a):
        if a[i] >= max(a[i:]):
            list_down.append(a[i])
            i = i+1
        else:
            list_down.append(max(a[i+1:]))
            i = a.index(max(a[i+1:]))+1
    return list_down

def decrease_seq(a):
    j=0
    list_up =[]
    while j <= len(a)-1:
        if a[j] <= min(a[j:]):
            list_up.append(a[j])
            j = j+1
        else:
            list_up.append(min(a[j+1:]))
            j = a.index(min(a[j+1:]))+1
    return list_up

a = [5,1,4,2,3]
print(increase_seq(a))
print(decrease_seq(a))

[5, 4, 3]
[1, 2, 3]
```
#25. Genome Assembly as Shortest Superstring(寻找最小的超字符窜)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-8357cf9c0ca522a3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 两两之间比较，找最大的重叠
```
seq_list = []
stseq = ''
for line in open('25_Genome_Assembly_as_Shortest_Superstring'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)


def MergeMaxOverlap(str_list):
    max_length = -1

    for prefix_index in range(len(str_list)):
        # 不与自己匹配
        for suffix_index in [num for num in range(len(str_list)) if num != prefix_index]:
            prefix, suffix = str_list[prefix_index], str_list[suffix_index]
            i = 0
            # 如果没有找到相似序列，指针继续+1
            while prefix[i:] != suffix[0:len(prefix[i:])]:
                i += 1
            # 只要匹配大于-1，就改变max_length
            if len(prefix) - i > max_length:
                max_length = len(prefix) - i
                max_indicies = [prefix_index, suffix_index]

    return [str_list[j] for j in range(len(str_list)) if j not in max_indicies] + [
        str_list[max_indicies[0]] + str_list[max_indicies[1]][max_length:]]


def LongestCommonSuperstring(str_list):
    while len(str_list) > 1:
        str_list = MergeMaxOverlap(str_list)

    return str_list[0]


if __name__ == '__main__':
    dna_list = [i for i in seq_list]
    super_string = LongestCommonSuperstring(dna_list)

    print (super_string)

ATTAGACCTGCCGGAATAC
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-32ade0cc899e08d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

