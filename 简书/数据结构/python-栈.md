- 栈(stack)又称之为堆栈是一个特殊的有序表，其插入和删除操作都在栈顶进行操作，并且按照先进后出，后进先出的规则进行运作。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1fad05f333abf66d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####1. 定义一个栈
```
class ArrayStack:
    def __init__(self):
        # create an empty stack
        self._data=[]
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push (self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self._data.pop()
```
####2栈实现逆序打印字符串
```
list=[1,2,3,4,5]
list2=[]
def reverse(list):
    S=ArrayStack()
    for i in list:
        S.push(i)
    while not S.is_empty():
        list2.append(S.pop())
    return list2
print(reverse(list))
```
####3栈实现括号匹配
```
str="[1+2]+[2+3*(4+5)]"
def is_match(expr):
    # 括号匹配正确，回复True,错误回复False
    lefty='({['
    righty=')}]'
    S=ArrayStack()
    for i in expr:
        if i in lefty:
            S.push(i)
        elif i in righty:
            if S.is_empty():
                return False
            # 错配
            if righty.index(i) != lefty.index(S.pop()):
                return False
    return S.is_empty()
print(is_match(str))
```
