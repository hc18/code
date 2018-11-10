
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e5b0af311019d23c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e4739efd515295ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
具体原理见https://blog.csdn.net/BlackJack_/article/details/73801003
> 1: L列的第一个元素就是原文本最后一个元素**
> 2: 对原文本来说，F列每个元素，都是对应L列元素的下一个元素**（除首个元素）

####python 实现
```
import argparse
seq="abcbbcab#"

def bw_transform(s):
    n = len(s)
    # ['#abcbbcab', 'ab#abcbbc', 'abcbbcab#', 'b#abcbbca', 'bbcab#abc', 'bcab#abcb', 'bcbbcab#a', 'cab#abcbb', 'cbbcab#ab']
    m = sorted([s[i:n]+s[0:i] for i in range(n)])
    #纪录原始序列位置，2
    I = m.index(s)
    # bc#acbabb
    L = ''.join([q[-1] for q in m])
    return (I, L)

from operator import itemgetter

def bw_restore(I, L):
    n = len(L)
    # [(2, '#'), (3, 'a'), (6, 'a'), (0, 'b'), (5, 'b'), (7, 'b'), (8, 'b'), (1, 'c'), (4, 'c')]
    # key=itemgetter(1),用后面的字母排序
    X = sorted([(i, x) for i, x in enumerate(L)], key=itemgetter(1))
    # [None, None, None, None, None, None, None, None, None]
    T = [None for i in range(n)]
    # T=[3, 7, 0, 1, 8, 4, 2, 5, 6] （#aabbbbcc）
    for i, y in enumerate(X):
        j, _ = y
        T[j] = i
    Tx = [I]
    # Tx=[2, 0, 3, 1, 7, 5, 4, 8, 6] (#bacbbcba)
    for i in range(1, n):
        Tx.append(T[Tx[i-1]])
    # S=['#', 'b', 'a', 'c', 'b', 'b', 'c', 'b', 'a']
    S = [L[i] for i in Tx]
    S.reverse()
    # abcbbcab#
    return ''.join(S)
```
