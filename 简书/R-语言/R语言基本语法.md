##目录
- 帮助
- 查看类型
- 基本运算
- 数据结构
- 数据操作
- 方程计算

####1. 帮助
```
# 获取帮助信息
？topic
help(topic)

# 用法举例
example("topic")

## 搜索帮助系统
help.search("topic")

# 用于函数名记不记来了
apropos("topi")

# 打开网页搜索
RSiteSearch("topic") 
```
####2. 查看类型
- mode(),class(),typeof()区分
```
# 新建一个因子
> gl(2,5)           
[1] 1 1 1 1 1 2 2 2 2 2
Levels: 1 2

# 查看变量的类，显示为因子
> class(gl(2,5))  
[1] "factor"

# 查看数据大类，显示为数值型
> mode(gl(2,5))    
[1] "numeric"

# 查看数据细类，显示为整数型
> typeof(gl(2,5))   
[1] "integer"

# 在展现数据的细节上，mode<class<typeof。
``` 
####3. 基本运算
- 四则运算: 加减乘除, 余数, 整除, 绝对值, 判断正负
```
> a<-10;b<-6

# 加减乘除
> a+b;a-b;a*b;a/b
[1] 16
[1] 4
[1] 60
[1] 1.666667

# 余数,整除
> a%%b;a%/%b
[1] 4
[1] 1

# 绝对值
> abs(-a)
[1] 10

# 判断正负
> sign(-2:3)
[1] -1 -1  0  1  1  1
```
- 数学计算: 幂, 自然常用e的幂, 平方根, 对数
```
> a<-10;b<-5;c<-4

# 幂
> c^b;c^-b;c^(b/10)
[1] 1024
[1] 0.0009765625
[1] 2

# 自然常数e
> exp(1)
[1] 2.718282

# 自然常数e的幂
> exp(3)
[1] 20.08554

# 平方根
> sqrt(c)
[1] 2

# 以2为底的对数
> log2(c)
[1] 2
# 以10为底的对数
> log10(b)
[1] 0.69897

# 自定义底的对数
> log(c,base = 2)
[1] 2
# 自然常数e的对数
> log(a,base=exp(1))
[1] 2.302585

# 指数对数操作
> log(a^b,base=a)
[1] 5
> log(exp(3))
[1] 3
```
- 比较计算: ==, >, <, !=, <=, >=, isTRUE, identical
```
> a<-10;b<-5

# 比较计算
> a==a;a!=b;a>b;a=c
[1] TRUE
[1] TRUE
[1] TRUE
[1] FALSE
[1] FALSE
[1] TRUE

# 判断是否为TRUE
> isTRUE(a)
[1] FALSE
> isTRUE(!a)
[1] FALSE

# 精确比较两个对象
> identical(1, as.integer(1))
[1] FALSE
> identical(NaN, -NaN)
[1] TRUE

> f <- function(x) x
# 双冒号表示使用compiler 中的cmpfun函数
> g <- compiler::cmpfun(f)
> identical(f, g)
[1] TRUE
```
- 逻辑计算： &, |, &&, ||, xor
```
> x<-c(0,1,0,1)
> y<-c(0,0,1,1)

# 只比较第一个元素 &&, ||
> x && y;x || y
[1] FALSE
[1] FALSE

# S4对象的逻辑运算，比较所有元素 &, |
> x & y;x | y
[1] FALSE FALSE FALSE  TRUE
[1] FALSE  TRUE  TRUE  TRUE

# 异或
> xor(x,y)
[1] FALSE  TRUE  TRUE FALSE
> xor(x,!y)
[1]  TRUE FALSE FALSE  TRUE
```
- 约数计算： ceiling,floor,trunc,round,signif
```
# 向上取整
> ceiling(5.4)
[1] 6

# 向下取整
> floor(5.8)
[1] 5

# 取整数
> trunc(3.9)
[1] 3

# 四舍五入
> round(5.8)

# 四舍五入,保留2位小数
> round(5.8833, 2)
[1] 5.88

# 四舍五入,保留前2位整数
> signif(5990000,2)
[1] 6e+06
```
- 数组计算： 最大, 最小, 范围, 求和, 均值, 加权平均, 连乘, 差分, 秩,中位数, 分位数, 任意数，全体数
```
> d<-seq(1,10,2);d
[1] 1 3 5 7 9

# 求最大值，最小值,范围range
> max(d);min(d);range(d)
[1] 9
[1] 1
[1] 1 9

# 求和,均值
> sum(d),mean(d)
[1] 25
[1] 5

# 加权平均
> weighted.mean(d,rep(1,5))
[1] 5
> weighted.mean(d,c(1,1,2,2,2))
[1] 5.75

# 连乘
> prod(1:5)
[1] 120

# 差分
> diff(d)
[1] 2 2 2 2

# 秩
> rank(d)
[1] 1 2 3 4 5

# 中位数
> median(d)
[1] 5

# 分位数
> quantile(d)
0%  25%  50%  75% 100%
1    3    5    7    9

# 任意any，全体all
> e<-seq(-3,3);e
[1] -3 -2 -1  0  1  2  3
> any(e<0);all(e<0)
[1] TRUE
[1] FALSE
```
- 排列组合计算: 阶乘, 组合, 排列
```
# 5!阶乘
> factorial(5)
[1] 120

# 组合, 从5个中选出2个
> choose(5, 2)
[1] 10

# 列出从5个中选出2个的组合所有项
> combn(5,2)
     [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9] [,10]
[1,]    1    1    1    1    2    2    2    3    3     4
[2,]    2    3    4    5    3    4    5    4    5     5

# 计算0:10的组合个数
> for (n in 0:10) print(choose(n, k = 0:n))
[1] 1
[1] 1 1
[1] 1 2 1
[1] 1 3 3 1
[1] 1 4 6 4 1
[1]  1  5 10 10  5  1
[1]  1  6 15 20 15  6  1
[1]  1  7 21 35 35 21  7  1
[1]  1  8 28 56 70 56 28  8  1
[1]   1   9  36  84 126 126  84  36   9   1
[1]   1  10  45 120 210 252 210 120  45  10   1

# 排列，从5个中选出2个
> choose(5, 2)*factorial(2)
[1] 20
```
- 累积计算: 累加, 累乘, 最小累积, 最大累积
```
# 累加
> cumsum(1:5)
[1]  1  3  6 10 15

# 累乘
> cumprod(1:5)
[1]   1   2   6  24 120

> e<-seq(-3,3);e
[1] -3 -2 -1  0  1  2  3

# 最小累积cummin
> cummin(e)
[1] -3 -3 -3 -3 -3 -3 -3
# 最大累积cummax
> cummax(e)
[1] -3 -2 -1  0  1  2  3
```
- 两个数组计算: 交集, 并集, 差集, 数组是否相等, 取唯一, 查匹配元素的索引, 找重复元素索引
```
# 定义两个数组向量
> x <- c(9:20, 1:5, 3:7, 0:8);x
 [1]  9 10 11 12 13 14 15 16 17 18 19 20  1  2  3  4  5
[18]  3  4  5  6  7  0  1  2  3  4  5  6  7  8
> y<- 1:10;y
[1]  1  2  3  4  5  6  7  8  9 10

# 交集
> intersect(x,y)
[1]  9 10  1  2  3  4  5  6  7  8

# 并集
> union(x,y)
 [1]  9 10 11 12 13 14 15 16 17 18 19 20  1  2  3  4  5
[18]  6  7  0  8

# 差集，从x中排除y
> setdiff(x,y)
 [1] 11 12 13 14 15 16 17 18 19 20  0

# 判断是否相等
> setequal(x, y)
[1] FALSE

# 取唯一
> unique(c(x,y))
 [1]  9 10 11 12 13 14 15 16 17 18 19 20  1  2  3  4  5
[18]  6  7  0  8

# 找到x在y中存在的元素的索引
> which(x %in% y)
 [1]  1  2 13 14 15 16 17 18 19 20 21 22 24 25 26 27 28
[18] 29 30 31
> which(is.element(x,y))
 [1]  1  2 13 14 15 16 17 18 19 20 21 22 24 25 26 27 28
[18] 29 30 31

# 找到重复元素的索引
> which(duplicated(x))
 [1] 18 19 20 24 25 26 27 28 29 30
```
- 函数
```
# 基本语法
function_name <- function(arg_1, arg_2, ...) {
   Function body 
}
```
- ***函数名称*** -这是函数的实际名称。 它作为具有此名称的对象存储在R环境中。
- ***参数*** -参数是一个占位符。 当函数被调用时，你传递一个值到参数。 参数是可选的; 也就是说，一个函数可能不包含参数。 参数也可以有默认值。
- ***函数体*** -函数体包含定义函数的功能的语句集合。
- ***返回值*** -函数的返回值是要评估的函数体中的最后一个表达式。
```
# Create a function with arguments.
new.function <- function(a,b,c) {
   result <- a * b + c
   print(result)
}

# Call the function by position of arguments.
new.function(5,3,11)

# Call the function by names of the arguments.
new.function(a = 11, b = 5, c = 3)

[1] 26
[1] 58
```
####4. 数据结构
- 数据对象
```
x <- seq(0,1,by = 0.2)
y <- seq(0,1,by = 0.2)
y[4]
## [1] 0.6

x[3]
## [1] 0.4

1 - x[3]
## [1] 0.6

y[4] > 1 - x[3]
## [1] TRUE
```
- 向量
```
# 向量赋值
x <- c(1,3,5,7,9)
x
## [1] 1 3 5 7 9

v <- paste("x",1:5,sep="")
v
## [1] "x1" "x2" "x3" "x4" "x5"
```
```
# 向量运算
x <- c(1,3,5,7,9)
y <- c(2,4,6,8,10)
x * y
## [1]  2 12 30 56 90

x %*% y
##      [,1]
## [1,]  190
```
```
# 生成有规则的序列
(t <- 1:10)
##  [1]  1  2  3  4  5  6  7  8  9 10

(r <- 5:1)
## [1] 5 4 3 2 1

2 * 1:5
## [1]  2  4  6  8 10

seq(1,10,2)
## [1] 1 3 5 7 9

seq(1,by = 2,length = 10)
##  [1]  1  3  5  7  9 11 13 15 17 19
```
```
# 向量常见函数
x <- c(1,3,5,7,9)
length(x)
## [1] 5

y <- c(2,6,3,7,5)
sort(y)
## [1] 2 3 5 6 7

rev(y)
## [1] 5 7 3 6 2

append(y,10:15,after = 3)
##  [1]  2  6  3 10 11 12 13 14 15  7  5

sum(x)
## [1] 25

max(y)
## [1] 7
```
```
# 向量索引
x <- c(1,3,5,7,9)
x[2]
## [1] 3

x[c(1,3)] <- c(9,11)
x
## [1]  9  3 11  7  9

x[x < 9]
## [1] 3 7

y <- 1:10
y[-(1:5)]
## [1]  6  7  8  9 10
```
- 矩阵
```
# 语法
matrix(data, nrow, ncol, byrow, dimnames)
```
- 数据是成为矩阵的数据元素的输入向量。
- nrow是要创建的行数。
- ncol是要创建的列数。
- byrow是一个逻辑线索。 如果为TRUE，则输入向量元素按行排列。
- dimname是分配给行和列的名称。
```
matrix(1:12,nrow = 4,ncol = 3)
##      [,1] [,2] [,3]
## [1,]    1    5    9
## [2,]    2    6   10
## [3,]    3    7   11
## [4,]    4    8   12

matrix(1:12,nrow = 4,ncol = 3,byrow = T)
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    4    5    6
## [3,]    7    8    9
## [4,]   10   11   12

(A <- matrix(1:12,nrow = 3,ncol = 4))
##      [,1] [,2] [,3] [,4]
## [1,]    1    4    7   10
## [2,]    2    5    8   11
## [3,]    3    6    9   12

t(A)
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    4    5    6
## [3,]    7    8    9
## [4,]   10   11   12

A * A
##      [,1] [,2] [,3] [,4]
## [1,]    1   16   49  100
## [2,]    4   25   64  121
## [3,]    9   36   81  144

A %*% t(A)
##      [,1] [,2] [,3]
## [1,]  166  188  210
## [2,]  188  214  240
## [3,]  210  240  270

diag(A)
## [1] 1 5 9

diag(diag(A))
##      [,1] [,2] [,3]
## [1,]    1    0    0
## [2,]    0    5    0
## [3,]    0    0    9

diag(3)
##      [,1] [,2] [,3]
## [1,]    1    0    0
## [2,]    0    1    0
## [3,]    0    0    1

(B <- matrix(rnorm(16),4,4))
##            [,1]       [,2]      [,3]       [,4]
## [1,] -1.9441703 -1.4811642 1.2187468  1.0028083
## [2,]  0.6886851 -0.3208272 0.3789500  0.9239378
## [3,]  1.7030543 -0.2826748 0.2768131 -1.1049455
## [4,] -1.3975218 -0.6632472 0.8276895  1.4652977

solve(B)
##             [,1]       [,2]       [,3]       [,4]
## [1,] -0.03313522  0.5688924  0.1142514 -0.2498819
## [2,] -2.06669506 -1.8009514  1.2105668  3.4628296
## [3,] -1.77181671 -1.9747337  2.0794344  4.0257930
## [4,]  0.03376588  0.8428525 -0.5176777 -0.2624789

(B.eigen <- eigen(B,symmetric = T))
## $values
## [1]  2.2962328  1.2039567 -0.5355768 -3.4874994
## 
## $vectors
##            [,1]        [,2]        [,3]       [,4]
## [1,]  0.2730185 -0.48668143  0.01842590  0.8296159
## [2,]  0.3168695 -0.06025928  0.93287247 -0.1603481
## [3,] -0.1790906 -0.87148651 -0.07292924 -0.4506874
## [4,] -0.8904949  0.00461278  0.35226518  0.2879353

svd(B)
## $d
## [1] 3.946727 1.590731 1.189326 0.143115
## 
## $u
##             [,1]       [,2]       [,3]       [,4]
## [1,] -0.71015075 -0.3175435 -0.4980918 -0.3830882
## [2,] -0.05382737 -0.5504837  0.7326792 -0.3965496
## [3,]  0.40938383 -0.7653272 -0.3594082  0.3427898
## [4,] -0.57025731 -0.1020202  0.2931066  0.7605833
## 
## $v
##            [,1]        [,2]       [,3]        [,4]
## [1,]  0.7190095 -0.57996589  0.3794131 -0.05206411
## [2,]  0.3373981  0.58523258  0.3446369  0.65183640
## [3,] -0.3153411 -0.56068851 -0.1566321  0.74943632
## [4,] -0.5193726 -0.08228479  0.8442378 -0.10365246

dim(A)
## [1] 3 4

nrow(B)
## [1] 4

det(B)
## [1] 1.068612

A[row(A) < col(A)] = 0
A
##      [,1] [,2] [,3] [,4]
## [1,]    1    0    0    0
## [2,]    2    5    0    0
## [3,]    3    6    9    0

apply(A,1,sum)
## [1]  1  7 18

apply(A,2,mean)
## [1] 2.000000 3.666667 3.000000 0.000000
```
- 数组
***矩阵只能是2维的，数组是多维的。一维数组就是向量，二维数组就是矩阵。***
```
(xx <- array(1:24,c(3,4,2)))
## , , 1
## 
##      [,1] [,2] [,3] [,4]
## [1,]    1    4    7   10
## [2,]    2    5    8   11
## [3,]    3    6    9   12
## 
## , , 2
## 
##      [,1] [,2] [,3] [,4]
## [1,]   13   16   19   22
## [2,]   14   17   20   23
## [3,]   15   18   21   24

xx[2,3,2]
## [1] 20

xx[2,1:3,2]
## [1] 14 17 20

dim(xx)
## [1] 3 4 2
```
- 因子
***因子是用于对数据进行分类并将其存储为级别的数据对象***
```
y <- c("male","female","female","male","female","male","male")
(f <- factor(y))
## [1] male   female female male   female male   male  
## Levels: female male

levels(f)
## [1] "female" "male"
```
```
# gl()生成因子级别，n给出的级数，k给出复制数，labels是所得因子水平的标签向量
v <- gl(3, 4, labels = c("Tampa", "Seattle","Boston"))
print(v)

Tampa   Tampa   Tampa   Tampa   Seattle Seattle Seattle Seattle Boston 
[10] Boston  Boston  Boston 
Levels: Tampa Seattle Boston
```
- 列表
***如果一个数据对象需要包含不同的数据类型，则可以采用列表（List）***
```
x <- c(1,1,2,2,3,3,3)
y <- c("male","female","female","male","female","male","male")
z <- c(80,85,92,76,61,95,83)
(stu <- list(class = x, sex = y, score = z))
## $class
## [1] 1 1 2 2 3 3 3
## 
## $sex
## [1] "male"   "female" "female" "male"   "female" "male"   "male"  
## 
## $score
## [1] 80 85 92 76 61 95 83

stu[[3]]
## [1] 80 85 92 76 61 95 83

stu$sex
## [1] "male"   "female" "female" "male"   "female" "male"   "male"
```
- 数据框
***数据框（data frame）是一种矩阵形式的数据，但各列可以是不同类型的数据，可以看做是矩阵的推广，类似于关系数据库的形式。***
```
(student <- data.frame(class = x, sex = y, score = z))
##   class    sex score
## 1     1   male    80
## 2     1 female    85
## 3     2 female    92
## 4     2   male    76
## 5     3 female    61
## 6     3   male    95
## 7     3   male    83

row.names(student) <- c("zhao","qian","sun","li","zhou","wu","zhen")
student
##      class    sex score
## zhao     1   male    80
## qian     1 female    85
## sun      2 female    92
## li       2   male    76
## zhou     3 female    61
## wu       3   male    95
## zhen     3   male    83

student[,"score"]
## [1] 80 85 92 76 61 95 83

student[,2]
## [1] male   female female male   female male   male  
## Levels: female male

student$score
## [1] 80 85 92 76 61 95 83

student[["class"]]
## [1] 1 1 2 2 3 3 3

student[[3]]
## [1] 80 85 92 76 61 95 83

#数据框绑定attach函数
#score
#Error: object 'score' not found
attach(student)
score
## [1] 80 85 92 76 61 95 83

detach()
#score
#Error: object 'score' not found
```
####5. 数据操作
- ***字符串操作***
- 连接字符串 - paste()函数
```
paste(..., sep = " ", collapse = NULL)
```

- ***...***表示要组合的任意数量的自变量。
- ***sep***表示参数之间的任何分隔符。 它是可选的。
- ***collapse***用于消除两个字符串之间的空格。 但不是一个字符串的两个字内的空间。
```
a <- "Hello"
b <- 'How'
c <- "are you? "

print(paste(a,b,c))
print(paste(a,b,c, sep = "-"))
print(paste(a,b,c, sep = "", collapse = ""))

[1] "Hello How are you? "
[1] "Hello-How-are you? "
[1] "HelloHoware you? "
```
- 格式化数字和字符串 - format()函数
```
#format(x, digits, nsmall, scientific, width, justify = c("left", "right", "centre", "none")) 
```
- ***x***是向量输入。
- ***digits***是显示的总位数。
- ***nsmall***是小数点右边的最小位数。
- 科学设置为TRUE以显示科学记数法。
- ***width***指示通过在开始处填充空白来显示的最小宽度。
- ***justify***是字符串向左，右或中心的显示。
```
# Total number of digits displayed. Last digit rounded off.
result <- format(23.123456789, digits = 9)
print(result)
[1] "23.1234568"

# Display numbers in scientific notation.
result <- format(c(6, 13.14521), scientific = TRUE)
print(result)
[1] "6.000000e+00" "1.314521e+01"

# The minimum number of digits to the right of the decimal point.
result <- format(23.47, nsmall = 5)
print(result)
[1] "23.47000"

# Format treats everything as a string.
result <- format(6)
print(result)
[1] "6"

# Numbers are padded with blank in the beginning for width.
result <- format(13.7, width = 6)
print(result)
[1] "  13.7"

# Left justify strings.
result <- format("Hello", width = 8, justify = "l")
print(result)
[1] "Hello   "

# Justfy string with center.
result <- format("Hello", width = 8, justify = "c")
print(result)
[1] " Hello  "
```
- 计算字符串中的字符数 - nchar()函数
```
# 此函数计算字符串中包含空格的字符数。
result <- nchar("Count the number of characters")
print(result)
[1] 30
```
- 更改case - toupper()和tolower()函数
```
# Changing to Upper case.
result <- toupper("Changing To Upper")
print(result)

# Changing to lower case.
result <- tolower("Changing To Lower")
print(result)

[1] "CHANGING TO UPPER"
[1] "changing to lower"
```
- 提取字符串的一部分 - substring()函数
```
# Extract characters from 5th to 7th position.
result <- substring("Extract", 5, 7)
print(result)
[1] "act"
```
- ***数据帧操作***
数据帧是表或二维阵列状结构，其中每一列包含一个变量的值，并且每一行包含来自每一列的一组值。
以下是数据帧的特性。
  - 列名称应为非空。
  - 行名称应该是唯一的。
  - 存储在数据帧中的数据可以是数字，因子或字符类型。
  - 每个列应包含相同数量的数据项。
- 创建数据帧
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Print the data frame.			
print(emp.data) 

 emp_id    emp_name     salary     start_date
1     1     Rick        623.30     2012-01-01
2     2     Dan         515.20     2013-09-23
3     3     Michelle    611.00     2014-11-15
4     4     Ryan        729.00     2014-05-11
5     5     Gary        843.25     2015-03-27
```
- 获取数据结构
通过使用str()函数可以看到数据帧的结构。
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Get the structure of the data frame.
str(emp.data)

'data.frame':   5 obs. of  4 variables:
 $ emp_id    : int  1 2 3 4 5
 $ emp_name  : chr  "Rick" "Dan" "Michelle" "Ryan" ...
 $ salary    : num  623 515 611 729 843
 $ start_date: Date, format: "2012-01-01" "2013-09-23" "2014-11-15" "2014-05-11" ...
```
- 数据框中的数据摘要
可以通过应用summary()函数获取数据的统计摘要和性质。
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Print the summary.
print(summary(emp.data))  

     emp_id    emp_name             salary        start_date        
 Min.   :1   Length:5           Min.   :515.2   Min.   :2012-01-01  
 1st Qu.:2   Class :character   1st Qu.:611.0   1st Qu.:2013-09-23  
 Median :3   Mode  :character   Median :623.3   Median :2014-05-11  
 Mean   :3                      Mean   :664.4   Mean   :2014-01-14  
 3rd Qu.:4                      3rd Qu.:729.0   3rd Qu.:2014-11-15  
 Max.   :5                      Max.   :843.2   Max.   :2015-03-27 
```
- 从数据帧提取数据
使用列名称从数据框中提取特定列。
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5),
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25),
   
   start_date = as.Date(c("2012-01-01","2013-09-23","2014-11-15","2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)

# Extract Specific columns.
result <- data.frame(emp.data$emp_name,emp.data$salary)
print(result)
  emp.data.emp_name emp.data.salary
1              Rick          623.30
2               Dan          515.20
3          Michelle          611.00
4              Ryan          729.00
5              Gary          843.25

# Extract first two rows.
result <- emp.data[1:2,]
print(result)
  emp_id    emp_name   salary    start_date
1      1     Rick      623.3     2012-01-01
2      2     Dan       515.2     2013-09-23

# Extract 3rd and 5th row with 2nd and 4th column.
result <- emp.data[c(3,5),c(2,4)]
print(result)
  emp_name start_date
3 Michelle 2014-11-15
5     Gary 2015-03-27
```
- 数据帧中加入列和行
```
# Create vector objects.
city <- c("Tampa","Seattle","Hartford","Denver")
state <- c("FL","WA","CT","CO")
zipcode <- c(33602,98104,06161,80294)

# Combine above three vectors into one data frame.
addresses <- cbind(city,state,zipcode)

# Print a header.
cat("# # # # The First data frame
") 

# Print the data frame.
print(addresses)

# # # # The First data frame
     city       state zipcode
[1,] "Tampa"    "FL"  "33602"
[2,] "Seattle"  "WA"  "98104"
[3,] "Hartford" "CT"   "6161" 
[4,] "Denver"   "CO"  "80294"

# Create another data frame with similar columns
new.address <- data.frame(
   city = c("Lowry","Charlotte"),
   state = c("CO","FL"),
   zipcode = c("80230","33949"),
   stringsAsFactors = FALSE
)

# Print a header.
cat("# # # The Second data frame
") 

# Print the data frame.
print(new.address)

# # # The Second data frame
       city       state   zipcode
1      Lowry      CO      80230
2      Charlotte  FL      33949

# Combine rows form both the data frames.
all.addresses <- rbind(addresses,new.address)

# Print a header.
cat("# # # The combined data frame
") 

# Print the result.
print(all.addresses)

# # # The combined data frame
       city      state zipcode
1      Tampa     FL    33602
2      Seattle   WA    98104
3      Hartford  CT     6161
4      Denver    CO    80294
5      Lowry     CO    80230
6     Charlotte  FL    33949
```
- 合并数据帧
在下面的例子中，我们考虑图书馆名称“MASS”中有关Pima Indian Women的糖尿病的数据集。 我们基于血压（“bp”）和体重指数（“bmi”）的值合并两个数据集。 在选择这两列用于合并时，其中这两个变量的值在两个数据集中匹配的记录被组合在一起以形成单个数据帧。
```
library(MASS)
merged.Pima <- merge(x = Pima.te, y = Pima.tr,
   by.x = c("bp", "bmi"),
   by.y = c("bp", "bmi")
)
print(merged.Pima)
nrow(merged.Pima)
```
```
 bp  bmi npreg.x glu.x skin.x ped.x age.x type.x npreg.y glu.y skin.y ped.y
1  60 33.8       1   117     23 0.466    27     No       2   125     20 0.088
2  64 29.7       2    75     24 0.370    33     No       2   100     23 0.368
3  64 31.2       5   189     33 0.583    29    Yes       3   158     13 0.295
4  64 33.2       4   117     27 0.230    24     No       1    96     27 0.289
5  66 38.1       3   115     39 0.150    28     No       1   114     36 0.289
6  68 38.5       2   100     25 0.324    26     No       7   129     49 0.439
7  70 27.4       1   116     28 0.204    21     No       0   124     20 0.254
8  70 33.1       4    91     32 0.446    22     No       9   123     44 0.374
9  70 35.4       9   124     33 0.282    34     No       6   134     23 0.542
10 72 25.6       1   157     21 0.123    24     No       4    99     17 0.294
11 72 37.7       5    95     33 0.370    27     No       6   103     32 0.324
12 74 25.9       9   134     33 0.460    81     No       8   126     38 0.162
13 74 25.9       1    95     21 0.673    36     No       8   126     38 0.162
14 78 27.6       5    88     30 0.258    37     No       6   125     31 0.565
15 78 27.6      10   122     31 0.512    45     No       6   125     31 0.565
16 78 39.4       2   112     50 0.175    24     No       4   112     40 0.236
17 88 34.5       1   117     24 0.403    40    Yes       4   127     11 0.598
   age.y type.y
1     31     No
2     21     No
3     24     No
4     21     No
5     21     No
6     43    Yes
7     36    Yes
8     40     No
9     29    Yes
10    28     No
11    55     No
12    39     No
13    39     No
14    49    Yes
15    49    Yes
16    38     No
17    28     No
[1] 17

```
####6. 方程计算
- 一元一次方程
```
# 定义方程函数
> f1 <- function (x, a, b) a*x+b

# 给a,b常数赋值
> a<-5;b<-10

# 在(-10,10)的区间，精确度为0.0001位，计算方程的根
> result <- uniroot(f1,c(-10,10),a=a,b=b,tol=0.0001)

# 打印方程的根x
> result$root
[1] -2
```
- 以图形展示方程：y = 5*x + 10
```
library(ggplot2)
instaf1 <- function(x,a,b) a*x+b
result <- uniroot(f1,c(-10,10),a=a,b=b,tol=0.0001)
a<-5;b<-10
# 创建数据点
x<-seq(-5,5,by=0.01)
y<-f1(x,a,b)
df<-data.frame(x,y)

# 用ggplot2来画图
g<-ggplot(df,aes(x,y))
g<-g+geom_line(col='red') #红色直线
g<-g+geom_point(aes(result$root,0),col="red",size=3) #点
g<-g+geom_hline(yintercept=0)+geom_vline(xintercept=0) #坐标轴
g<-g+ggtitle(paste("y =",a,"* x +",b))
g
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f04db6bce3a4063a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 一元二次方程
```
一元二次方程：a*x^2+b*x+c=0，设a=1，b=5，c=6，求x？

> f2 <- function (x, a, b, c) a*x^2+b*x+c
> a<-1;b<-5;c<-6
> result <- uniroot(f2,c(0,-2),a=a,b=b,c=c,tol=0.0001)
> result$root
[1] -2
```
```
# 把参数带入方程，用uniroot()函数，我们就解出了方程的一个根，改变计算的区间，我们就可以得到另一个根。

> result <- uniroot(f2,c(-4,-3),a=a,b=b,c=c,tol=0.0001)
> result$root
[1] -3
```
```
#方程的两个根，一个是-2，一个是-3。
#由于uniroot()函数，每次只能计算一个根，而且要求输入的区间端值，必须是正负号相反的。如果我们直接输入一个(-10,0)这个区间，那么uniroot()函数会出现错误。

> result <- uniroot(f2,c(-10,0),a=a,b=b,c=c,tol=0.0001)
Error in uniroot(f2, c(-10, 0), a = a, b = b, c = c, tol = 1e-04) : 
  位于极点边的f()值之正负号不相反
```
- 以图形展示方程：y = x^2 + 5*x + 6
```
library(ggplot2)
f2 <- function(x,a,b,c) a*x^2+b*x+c
a<-1;b<-5;c<-6
x<-seq(-5, 1, by=0.01)
y<-f2(x,a,b,c)
df<-data.frame(x,y)
g<-ggplot(df,aes(x,y))
g<-g+geom_line(col='red')
g<-g+geom_hline(yintercept = 0)+geom_vline(xintercept=0)
g<-g+ggtitle(paste("y =",a,"* X^2 +",b,"* x +",c))
g
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-001b753688fe54e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 一元三次方程

```
# 一元二次方程：a*x^3+b*x^2+c*x+d=0，设a=1，b=5，c=6，d=-11，求x？
> f3 <- function (x, a, b, c,d) a*x^3+b*x^2+c*x+d
> a<-1;b<-5;c<-6;d<--11
> result <- uniroot(f3,c(-5,5),a=a,b=b,c=c,d=d,tol=0.0001)
> result$root
[1] 0.9461458
```
- 以图形展示方程：y = x^3 + 5*x^2 + 6* x - 11
```
library(ggplot2)
f3 <- function(x,a,b,c,d) a*x^3+b*x^2+c*x+d
a<-1;b<-5;c<-6;d<--11
x<-seq(-5, 5, by=0.01)
y<-f3(x,a,b,c,d)
df<-data.frame(x,y)
g<-ggplot(df,aes(x,y))
g<-g+geom_line(col='red')
g<-g+geom_hline(yintercept = 0)+geom_vline(xintercept=0)
g<-g+ggtitle(paste("y =",a,"* x^3 +",b,"* x^2 +",c,"* x ",d))
g
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-abf0f1c3f9ef3384.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 二元一次方程组
![image.png](http://upload-images.jianshu.io/upload_images/6634703-589088c42a91b2de.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# 左矩阵
> lf<-matrix(c(3,5,1,2),nrow=2,byrow=TRUE)

# 右矩阵
> rf<-matrix(c(4,1),nrow=2)

# 计算结果
> result<-solve(lf,rf)
> result
     [,1]
[1,]    3
[2,]   -1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-07b896febed725a9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####6. 参考文献
1. http://www.rpubs.com/jeeplee/DataAnalysis-2 （R语言基本运算）
2. http://blog.fens.me/r-mathematics/ （R语言中的数学计算）
3. https://www.w3cschool.cn/r/r_data_frames.html （W3Cschool, R 语言教程 ）
