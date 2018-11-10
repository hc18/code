![image.png](https://upload-images.jianshu.io/upload_images/6634703-990ca6b6663a7a1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- “坏字符规则”。这个规则说，当我们做字符比较，并且发生错配时，一旦发生错配，我们就跳过下面的比对，直到发生以下这两件事之一：要么“错配”变成了一个“匹配”，或者模式“P”完全跳过了这个错配的字符。
- step1 没匹配上，P向前条两格，直到上下C 匹配，step2 没匹配上，如果A 不再P里面，直接跳过所有的P
![image.png](https://upload-images.jianshu.io/upload_images/6634703-fc7273d9d9de1816.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- Boyer-Moore算法的后一个组成部分，是另一个规则，它被称为“好后缀规则”。这个规则说，让“t”等于内部循环中，匹配的子字符串，所以，我们用小写的“t”来代表这个匹配上的子字符串。
- step1 有错配， 把“TAC” 看成一个整体，P里面下一个TAC和这个比较，有的话就是step2，没有的话直接跳过
> 一般都是两个原则一起来的

![image.png](https://upload-images.jianshu.io/upload_images/6634703-1a393a29a218c500.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 哪个跳过的多，用哪个。
step1: bc ==6, gs==0, 用bc
step2: bc==0, gs==2, 用gs
step3: bc==2,gs==7, 用gs
- 代码实现
```
def string_match_boyer_moore(string,match,start=0):
    string_len = len(string)
    match_len  = len(match)
    end = match_len - 1
    if string_len < match_len or match_len==0:
        print ('Not Found')
        return start;
    while string[end] == match[end]:
        end -= 1
        if end == 0:
            print ('Success Position:' + str(start))
            return
    idx = contain_char(match,string[end])
    shift = match_len
    if idx > -1:
        shift = end - idx
    start += shift
    string_match_boyer_moore(string[shift:],match,start)

def contain_char(s,c):
   for i in range(len(s)):
      if c == s[i]:
          return i
   return -1

string_match_boyer_moore('here is a simple example','example')

```

```
def find_boyer_moore(T,P):
    n,m=len(T),len(P)
    if m==0:return 0
    last = {}
    for k in range(m):
        last[P[k]]=k
    i=m-1
    k=m-1
    while i<n:
        if T[i]==P[k]:
            if k==0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i],-1)
            i+=m-min(k,j+1)
            k=m-1
    return -1

T='here is a simple example'
p='example'
i=find_boyer_moore(T,p)
print(i)
```
