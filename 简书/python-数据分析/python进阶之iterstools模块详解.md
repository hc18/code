>iterstools很强大,务必要掌握
https://docs.python.org/3/library/itertools.html

# 1. 概览
####无限迭代器
| 迭代器        | 参数          | 结果  |例|
| :-------------: |:-------------:| :-----:|:---:|
| count()      | start, [step] | start, start+step, start+2*step, ... |count(10) --> 10 11 12 13 14 ...|
| cycle()      | p      |   p0, p1, ... plast, p0, p1, ... |cycle('ABCD') --> A B C D A B C D ...|
| repeat() | elem [,n]     |    elem，elem，elem，...无休止或多达n次 |repeat(10, 3) --> 10 10 10|
####处理输入序列迭代器
| 迭代器 |参数| 结果|例|
| :-------------: |:-------------:| :-----:|:---:|
| accumulate() |p [,func]| p0, p0+p1, p0+p1+p2, ...|accumulate([1,2,3,4,5]) --> 1 3 6 10 15|
|chain()|p, q, ...| p0, p1, ... plast, q0, q1, ...|chain('ABC', 'DEF') --> A B C D E F|
| chain.from_iterable() |可迭代| 	p0, p1, ... plast, q0, q1, ...|chain.from_iterable(['ABC', 'DEF']) --> A B C D E F|
|compress() |数据，选择器| 	(d[0] if s[0]), (d[1] if s[1]), ...|compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F|
|dropwhile()|pred, seq| seq[n]，seq[n+1]，当pred失败时开始|dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1|
|filterfalse() |	pred, seq|pred(elem)为false的seq的元素|filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8|
| groupby() |iterable[, keyfunc]|通过keyfunc(v)的值分组的子迭代器|---|
| islice() |	seq, [start,] stop [, step]| 元素从seq[start:stop:step]|islice('ABCDEFG', 2, None) --> C D E F G|
| starmap() |功能报| func(*seq[0]), func(*seq[1]), ...|starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000|
| takewhile() |pred, seq| seq[0]，seq[1]，直到pred失败|takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4|
| tee() |it，n| it1，it2，... itn将一个迭代器拆分为n|---|
| zip_longest() |p, q, ...| (p[0], q[0]), (p[1], q[1]), ...|zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-|
####组合生成器
| 迭代器 |参数| 结果|
|:---: |:-------------:| :-----:|
|product() |p, q, ... [repeat=1]| 笛卡尔积，相当于嵌套for循环|
| permutations() |p[, r]| r长度元组，所有可能的顺序，没有重复的元素|
| combinations() |p, r| r长度元组，按排序顺序，没有重复的元素|
| combinations_with_replacement() |p, r| r长度元组，按排序顺序，具有重复的元素|
| product('ABCD', repeat=2) |---|AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD|
|permutations('ABCD', 2)|---| AB AC AD BA BC BD CA CB CD DA DB DC|
|combinations('ABCD', 2) |---| AB AC AD BC BD CD|
| combinations_with_replacement('ABCD', 2) |---| AA AB AC AD BB BC BD CC CD DD|
#2. itertools 函数(无限迭代器)
####2.1 itertools.count(start=0, step=1)
- 创建一个迭代器，生成从start开始的连续的数，start默认为0，step默认为1
- 源代码
```
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
```
- 使用
```
from itertools import *
for i in zip(count(1),['a','b','c']):
    print(i)

(1, 'a')
(2, 'b')
(3, 'c')
```
####2.2 itertools.cycle(iterable)
- 创建一个迭代器，对iterable中的元素遍历输出一次，内部会生成iterable中的元素的一个副本，反复循环该副本。
- 源代码
```
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    # 遍历一次生成器
    for element in iterable:
        yield element
        saved.append(element)
    # 反复执行副本
    while saved:
        for element in saved:
            yield element
```
- 使用
```
from itertools import *

i = 0
for item in cycle(['a', 'b', 'c']):
    i += 1
    if i == 7:
        break
    print (i, item)

1 a
2 b
3 c
4 a
5 b
6 c
```
####2.3 itertools.repeat(object[, times])
- 创建一个迭代器，重复生成object，times（如果已提供）指定重复计数，如果未提供times，将无止尽返回该对象。
- 源代码
```
def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    # 如果times=None，无限循环
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object
```
- 使用
```
from itertools import *
for i in repeat('sweet_honey', 3):
    print (i)

sweet_honey
sweet_honey
sweet_honey
```
#3. itertools 函数(处理输入序列迭代器)
####3.1 itertools.accumulate(iterable[, func])
- 创建一个迭代器，返回函数指定的操作方式，默认为累加和。
- 源代码
```
import operator
def accumulate(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    # 生成一个迭代器
    it = iter(iterable)
    try:
        # 获取下一个值
        total = next(it)
    # 遇到StopIteration，就返回空
    except StopIteration:
        return
    # 如果没有报错，就返回total
    yield total
    # 从2开始累加
    for element in it:
        total = func(total, element)
        yield total
```
- 使用
```
from itertools import accumulate
import operator
print(list(accumulate(range(10))))

[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
print(list(accumulate(range(1,5), func = operator.mul)))

[1, 2, 6, 24]
print(list(list(accumulate(range(5,1,-1), max))))

[5, 5, 5, 5]
```
####3.2 itertools.chain(*iterables)
- 将几个可迭代的容器依次迭代
- 源代码
```
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
```
- 使用
```
from itertools import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print (i)

1
2
3
a
b
c
```
####3.3 chain.from_iterable() 
- 将可迭代容器里面的元素再次进行迭代一次
- 源代码
```
def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
```
- 使用
```
from itertools import *

for i in chain([['abc', 'bca','cba'],'abcd']):
    print(i)

['abc', 'bca', 'cba']
abcd

for i in chain.from_iterable([['abc', 'bca','cba'],'abcd']):
    print(i)

abc
bca
cba
a
b
c
d
```
####3.4 itertools.compress(data, selectors)
- 两个参数分别为data, selectors, 根据selectors中的真假情况返回data中的元素
- 源代码
```
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in zip(data, selectors) if s)
```
- 使用
```
from itertools import *
for i in compress('ABCDEF', [1,0,1,0,1,1]) :
    print(i)

A
C
E
F
```
####3.5 itertools.dropwhile(predicate, iterable)
- 当predicate返回True时，跳过元素。一旦函数返回False，则开始收集剩下的所有元素到循环器
- 源代码
```
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    # 一直在找false
    for x in iterable:
        if not predicate(x):
            yield x
            break
    # 找到false 跳出上面的循环，进入这个循环直到结束
    for x in iterable:
        yield x
```
- 使用
```
from itertools import *

for i in dropwhile(lambda x: x<5, [1,4,6,4,1]) :
    print(i)

6
4
1
```
####3.6 itertools.filterfalse(predicate, iterable)
- 当predicate返回False时，才将iterable中的元素添加进循环器
- 源代码
```
def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x
```
- 使用
```
from itertools import *

for i in filterfalse(lambda x: x<5, [1,4,6,4,1]) :
    print(i)

6
```
####3.7 itertools.groupby(iterable[, key])
- 将key的结果作用于iterable中的元素，将拥有相同返回结果的元素加入到循环器中，该函数之前需要确保iterable是经过排序的
- 源代码
```
class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)
```
- 使用
```
from itertools import *

def height_classify(h):
    if h > 180:
        return 'tall'
    elif h < 160:
        return 'short'
    else:
        return 'middle'


friends = [192, 158, 168, 195, 185, 170, 135, 174, 182]
friends = sorted(friends, key=height_classify)
for m, n in groupby(friends, key=height_classify):
    print(m)
    print(list(n))

middle
[168, 170, 174]
short
[158, 135]
tall
[192, 195, 185, 182]
```
####3.7 itertools.islice(iterable, stop)
- 根据索引来选取迭代器的项
- 源代码
```
def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    it = iter(xrange(s.start or 0, s.stop or sys.maxint, s.step or 1))
    nexti = next(it)
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)
```
- 使用
```
from itertools import *

for i in islice(count(), 5, 10):
    print (i, end=' ')

5 6 7 8 9

for i in islice(count(), 0, 100, 10):
    print (i, end=' ')

0 10 20 30 40 50 60 70 80 90
```
####3.8 itertools.starmap(function, iterable)
- 用iterable 里面的项，构造function函数
```
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
```
-   使用
```
from itertools import *

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in starmap(lambda x,y:(x, y, x*y), values):
    print ('%d * %d = %d' % i)

0 * 5 = 0
1 * 6 = 6
2 * 7 = 14
3 * 8 = 24
4 * 9 = 36
```
####3.9 itertools.takewhile(predicate, iterable)
- 和dropwhile相反，当predicate返回False时，跳过元素。一旦函数返回True，则开始收集剩下的所有元素到循环器
- 源代码
```
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
```
- 使用
```
from itertools import *

for i in takewhile(lambda x: x<5, [1,4,6,4,1]) :
    print(i)
1
4

for i in dropwhile(lambda x: x<5, [1,4,6,4,1]) :
    print(i)

6
4
1
```
####3.10 itertools.tee(iterable[, n=2])
- 从单个的iterable返回n个独立的循环器
- 源代码
```
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                newval = next(it)       # fetch a new value and
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)
```
- 使用
```
from itertools import *

for i in tee([['abc', 'bca','cba'],'abcd']):
    for j in i:
        print(j)

['abc', 'bca', 'cba']
abcd
['abc', 'bca', 'cba']
abcd
```
####3.11 itertools.zip_longest(*iterables, fillvalue=None)
- 创建一个迭代器，聚合来自每个迭代器的元素。如果迭代的长度不均匀，那么缺失值将用 fillvalue 填充。迭代继续，直到最长可迭代被耗尽。
- 源代码
```
class ZipExhausted(Exception):
    pass

def zip_longest(*args, **kwds):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    counter = len(args) - 1
    def sentinel():
        nonlocal counter
        if not counter:
            raise ZipExhausted
        counter -= 1
        yield fillvalue
    fillers = repeat(fillvalue)
    iterators = [chain(it, sentinel(), fillers) for it in args]
    try:
        while iterators:
            yield tuple(map(next, iterators))
    except ZipExhausted:
        pass
```
- 使用
```
from itertools import *

for i in zip_longest('abcd','123',fillvalue='*'):
    print(i)

('a', '1')
('b', '2')
('c', '3')
('d', '*')
```
# 4. itertools 函数(组合生成器)
####4.1 itertools.product(*iterables, repeat=1)
- 笛卡尔乘积
- 源代码
```
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
```
- 使用
```
from itertools import *
for i in product('abc','xy'):
    print(i)

('a', 'x')
('a', 'y')
('b', 'x')
('b', 'y')
('c', 'x')
('c', 'y')
```
####4.2 itertools.permutations(iterable, r=None)
- 全排列
- 源代码
```
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```
- 使用
```
from itertools import *

for i in permutations('abcd', r=2):
    print(i, end='')

('a', 'b') ('a', 'c') ('a', 'd') ('b', 'a') ('b', 'c') ('b', 'd') ('c', 'a') ('c', 'b') ('c', 'd') ('d', 'a') ('d', 'b') ('d', 'c') 
```
####4.3 itertools.combinations(iterable, r)
- 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (不带重复)
- 源代码
```
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
```
- 使用
```
from itertools import *

for i in combinations('abcd',r=2):
    print(i, end=' ')

('a', 'b') ('a', 'c') ('a', 'd') ('b', 'c') ('b', 'd') ('c', 'd') 
```
####4.4 itertools.combinations_with_replacement(iterable, r)
- 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (带重复)
- 源代码
```
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
```
- 使用
```
from itertools import *

for i in combinations_with_replacement('abcd',r=2):
    print(i, end=' ')

('a', 'a') ('a', 'b') ('a', 'c') ('a', 'd') ('b', 'b') ('b', 'c') ('b', 'd') ('c', 'c') ('c', 'd') ('d', 'd') 
```
# 参考文献
1. https://docs.python.org/3/library/itertools.html#module-itertools
2. https://www.rddoc.com/doc/Python/3.6.0/zh/library/itertools/
3. http://www.wklken.me/posts/2013/08/20/python-extraitertools.html#itertoolsizip_longestiterables-fillvalue
4. http://blog.csdn.net/calling_wisdom/article/details/41219829
