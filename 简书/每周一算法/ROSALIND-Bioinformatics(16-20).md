>刷题ROSALIND，练编程水平
[http://rosalind.info/problems/list-view/](http://rosalind.info/problems/list-view/)
#16. Finding a Protein Motif (寻找蛋白质模体)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-7129eca0b43d61d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 为表示蛋白质模体的多种形式，设计以下表示形式：[XY]表示"既可以是X也可以是Y"，{X}表示"可以是除了X以外的任何一种氨基酸"。N-糖基化模体表示为 N{P}[ST]{P}
```
import urllib
from urllib.request import urlopen
import re
list = ['A2Z669','B5ZC00','P07204_TRBM_HUMAN','P20840_SAG1_YEAST']
for name in list:
    # url地址拼接找蛋白质序列
    url = 'http://www.uniprot.org/uniprot/'+name+'.fasta'
    # 获取url页面
    req = urllib.request.Request(url)
    # 打开获取的 页面
    response = urlopen(req)
    # 解读获取的页面
    the_page = response.read()
    # 返回匹配到的'\n'的位置
    start = the_page.find(b'\nM')
    # 把蛋白质序列拼接
    seq = the_page[start+1:].replace(b'\n',b'')
    seq = ' '+str(seq)
    # 正则表达式编译
    regex = re.compile(r'N(?=[^P][ST][^P])')
    index = 0
    out = []

    while(index<len(seq)):
        index += 1
        # 如果没有匹配到，跳出循环
        if re.search(regex,seq[index:]) == None:
            break
        # 如果匹配到了，加入到字典
        if re.match(regex,seq[index:]) != None:
            out.append(index)
    # 如果字典不为零，把匹配到的index 输出
    if out != []:
        print (name)
        print (' '.join([ str(i) for i in out]))

B5ZC00
87 120 144 308 397
P07204_TRBM_HUMAN
49 117 118 384 411
P20840_SAG1_YEAST
81 111 137 250 308 350 366 404 487 503 616
```
- 不了解urllib的看这里
>把下面的数据粘贴到rosalind_mprt.txt，和python脚本放在一个文件夹下
```
>A2Z669
MRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAP
GTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYAL
LVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATA
MAFISWFALAPSCVLNFWSMASR
>B5ZC00
MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQ
KDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSS
NEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVN
FKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKY
LNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYD
LSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILM
DLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIY
CLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK
>P07204_TRBM_HUMAN
MLGVLVLGALALAGLGFPAPAEPQPGGSQCVEHDCFALYPGPATFLNASQICDGLRGHLM
TVRSSVAADVISLLLNGDGGVGRRRLWIGLQLPPGCGDPKRLGPLRGFQWVTGDNNTSYS
RWARLDLNGAPLCGPLCVAVSAAEATVPSEPIWEEQQCEVKADGFLCEFHFPATCRPLAV
EPGAAAAAVSITYGTPFAARGADFQALPVGSSAAVAPLGLQLMCTAPPGAVQGHWAREAP
GAWDCSVENGGCEHACNAIPGAPRCQCPAGAALQADGRSCTASATQSCNDLCEHFCVPNP
DQPGSYSCMCETGYRLAADQHRCEDVDDCILEPSPCPQRCVNTQGGFECHCYPNYDLVDG
ECVEPVDPCFRANCEYQCQPLNQTSYLCVCAEGFAPIPHEPHRCQMFCNQTACPADCDPN
TQASCECPEGYILDDGFICTDIDECENGGFCSGVCHNLPGTFECICGPDSALARHIGTDC
DSGKVDGGDSGSGEPPPSPTPGSTLTPPAVGLVHSGLLIGISIASLCLVVALLALLCHLR
KKQGAARAKMEYKCAAPSKEVVLQHVRTERTPQRL
>P20840_SAG1_YEAST
MFTFLKIILWLFSLALASAININDITFSNLEITPLTANKQPDQGWTATFDFSIADASSIR
EGDEFTLSMPHVYRIKLLNSSQTATISLADGTEAFKCYVSQQAAYLYENTTFTCTAQNDL
SSYNTIDGSITFSLNFSDGGSSYEYELENAKFFKSGPMLVKLGNQMSDVVNFDPAAFTEN
VFHSGRSTGYGSFESYHLGMYCPNGYFLGGTEKIDYDSSNNNVDLDCSSVQVYSSNDFND
WWFPQSYNDTNADVTCFGSNLWITLDEKLYDGEMLWVNALQSLPANVNTIDHALEFQYTC
LDTIANTTYATQFSTTREFIVYQGRNLGTASAKSSFISTTTTDLTSINTSAYSTGSISTV
ETGNRTTSEVISHVVTTSTKLSPTATTSLTIAQTSIYSTDSNITVGTDIHTTSEVISDVE
TISRETASTVVAAPTSTTGWTGAMNTYISQFTSSSFATINSTPIISSSAVFETSDASIVN
VHTENITNTAAVPSEEPTFVNATRNSLNSFCSSKQPSSPSSYTSSPLVSSLSVSKTLLST
SFTPSVPTSNTYIKTKNTGYFEHTALTTSSVGLNSFSETAVSSQGTKIDTFLVSSLIAYP
SSASGSQLSGIQQNFTSTSLMISTYEGKASIFFSAELGSIIFLLLSYLLF
```
```
from collections import OrderedDict
import re

seqTest = OrderedDict()
with open('rosalind_mprt.txt', 'rt') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            seqName = line[1:]
            seqTest[seqName] = ''
            continue
        seqTest[seqName] += line.upper()

for i,seq in seqTest.items():
    #print (type(i))
# 正则表达式编译
    regex = re.compile(r'N(?=[^P][ST][^P])')
    index = 0
    out = []

    while(index<len(seq)):
        index += 1
        # 如果没有匹配到，跳出循环
        if re.search(regex,seq[index:]) == None:
            break
        # 如果匹配到了，加入到字典
        if re.match(regex,seq[index:]) != None:
            out.append(index)
    # 如果字典不为零，把匹配到的index 输出
    if out != []:
        print (i)
        print (' '.join([ str(i) for i in out]))

B5ZC00
84 117 141 305 394
P07204_TRBM_HUMAN
46 114 115 381 408
P20840_SAG1_YEAST
78 108 134 247 305 347 363 401 484 500 613
```
#17. Inferring mRNA from Protein(从蛋白质推断mRNA的种类)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-ecc83eaf1a7496cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 由于密码子的简并性，例如编码丙氨酸（字符A）的密码子就有4种。
  - 现在给定一个蛋白字符串，要求其可能的编码RNA的种数。
```
translate_table={
    "UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
    "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
    "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
    "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
    "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
    "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
    "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
    "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
    "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
    "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
    "UAA":"*",  "CAA":"Q", "AAA":"K", "GAA":"E",
    "UAG":"*",  "CAG":"Q", "AAG":"K", "GAG":"E",
    "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
    "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
    "UGA":"*",  "CGA":"R", "AGA":"R", "GGA":"G",
    "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"
}
#改变密码子字典{'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1, 'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2, 'H': 2, 'N': 2, 'D': 2, 'Q': 2, 'K': 2, 'E': 2, 'C': 2, 'R': 6, 'G': 4, 'W': 1}
translate_count_table={}
for aminoacid,pro in translate_table.items():
    if pro =="*":
        pass
    elif pro not in translate_count_table.keys():
        translate_count_table[pro] = 1
    else:
        translate_count_table[pro] += 1

def modfind(protein):
	possiblerna = 1
	for aminoacid in protein:
		possiblerna *= translate_count_table[aminoacid]
	return 3*possiblerna % 1000000

# Test
print (modfind("MA"))

12
```
#18. Open Reading Frames (开放阅读框)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-92355a53fafa6d26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 开放阅读框[open reading frame，ORF] 是结构基因的正常核苷酸序列，从起始密码子到终止密码子的阅读框可编码完整的多肽链，其间不存在使翻译中断的终止密码子。
  - 在mRNA序列中，每三个连续碱基(即三联“ 密码子”） 编码相应的氨基酸。其中有一个起始密码子AUG和三个终止密码子UAA，UAG，UGA。核糖体从起始密码子开始翻译，沿着mRNA序列合成多肽链并不断延伸，遇到终止密码子时，多肽链的延伸反应终止。由于读写位置不同，ORF在两条链上具有六种可能性。

```
def orf(sequence):
    # 读互补链
    rev_seq = sequence[::-1].replace('C','g').replace('G','c').replace('T','a').replace('A','t').upper()
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
    pro_list = []
    for start in range(len(sequence)-3):
        proUeinsequence = ''
        # ATG 是启动子
        if codonTable[sequence[start:start+3]] == 'M':
            # 开始遍历翻译
            for n in range(start,len(sequence),3):
                if sequence[n:n+3] in codonTable.keys():
                    # 拼接出字符窜
                    proUeinsequence += codonTable[sequence[n:n+3]]
                    # 遍历到最后为空
                    if codonTable[sequence[n:n+3]] == '':
                        # 如果字符窜不为空
                        if proUeinsequence != '':
                            # 把字符窜加入字典
                            pro_list.append(proUeinsequence)
                        break
    # 遍历互补链
    for start in range(len(rev_seq)-3):
        proUeinsequence = ''
        if codonTable[rev_seq[start:start+3]] == 'M':
            for n in range(start,len(rev_seq),3):
                if rev_seq[n:n+3] in codonTable.keys():
                    proUeinsequence += codonTable[rev_seq[n:n+3]]
                    if codonTable[rev_seq[n:n+3]] == '':
                        if proUeinsequence != '':
                            pro_list.append(proUeinsequence)
                        break
    # 返回找到启动子的正反链的集合
    return set(pro_list)

# 创建一个list，
seq_list = []
stseq = ''
for line in open('18_Open_reading_frames.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)

proteins = orf(seq_list[0])

for one in proteins:
    print (one)

M
MLLGSFRLIPKETLIQVAGSSPCNLS
MGMTPRLGLESLLE
MTPRLGLESLLE
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f0cd5292fe494e46.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 19. Enumerating Gene Orders(穷举排列)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9d28054ea9337d94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
   - 给定n，要求给出所有排列。
   - 第一行给出排列数目，接下去输出所有排列组合
```
import itertools
set1 = []
n = int(input("请输入一个整数："))
a = n*(n-1)
print(a)
for i in range(1,n+1):
    set1.append(i)
b = itertools.permutations(set1,n)
for one in list(b):
    print (' '.join(map(str,list(one))))
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d6f436680669784f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 20. Calculating Protein Mass(计算蛋白质质量)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d5dbf3a3e33728eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解题思路
  - 参考蛋白质质量表
```

table = {
    'A':   71.03711,
'C':   103.00919,
'D':  115.02694,
'E':   129.04259,
'F':   147.06841,
'G':   57.02146,
'H':   137.05891,
'I':   113.08406,
'K':   128.09496,
'L':   113.08406,
'M':   131.04049,
'N':   114.04293,
'P':   97.05276,
'Q':   128.05858,
'R':   156.10111,
'S':   87.03203,
'T':   101.04768,
'V':   99.06841,
'W':   186.07931,
'Y':   163.06333
}

string ='SKADYEK'
weight = 0
for i in string:
    if i in table.keys():
        weight += table[i]
print (weight)

821.3919199999999
```


