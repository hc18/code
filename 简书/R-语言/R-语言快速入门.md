####A. 基础知识
######1. 获得帮助  
```
#方法一,获取帮助信息
?mean
#方法二，获取帮助信息
help.search("mean")
# 方法三，搜索帮助系统
help.search("mean")
# 方法三，用于函数名记不记来了
apropos("mea")
# 方法四，打开网页搜索
RSiteSearch("mean")
```
######2. 简单会话
- R语言的标准赋值运算符是<-。（尽量少用=，有些情况下会失灵。）
```
> x <-c(1,2,4)
> x
[1] 1 2 4
> q<-c(x,x,8)
> q
[1] 1 2 4 1 2 4 8
# R下标是从1开始的，python 从0开始
> q[2]
[1] 2
> mean(q)
[1] 3.142857
> sd(q)
[1] 2.478479
```
######3. 函数入门
```
# 创建一个计算计数个数的函数
> oddcount<-function(x){
+   k<-0
+   for(n in x){
+     if(n%%2 ==1) k<-k+1
+   }
+   return(k)
+ }
> 
> oddcount(c(1,2,3,-1,5))
[1] 4
```
