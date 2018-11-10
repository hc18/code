NO.|目录
|:---:|:---:|
1|shell优点
2| 基本格式
3| 输出程序 echo
4| shell 变量
5| 引号
6| 循环
7| 循环控制
8| 条件判断
9| 算数运算
10| 逻辑运算符
11| 函数
12| 字符窜操作
13| 数组
14| 重定向
15| 其他命令

####1. shell优点
1. 语法和结构通常比较简单
2. 学习和使用通常比较简单
3. 通常不需要编译
4. 适合处理文件和目录之类的对象
####2. 基本格式
- 建立一个“test.sh”文件，在文件内输入以下代码
```
#!/usr/bin/env bash
echo "hello world"
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-4b77ae02fdc5f6a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. 输出程序 echo
```
#!/usr/bin/env bash
echo "hello world"
echo hello world

text="hello world"
echo $text

echo -e "hello \nworld"  #输出并且换行

echo "hello world" > a.txt  #重定向到文件

echo `date`  #输出当前系统时间
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-1cc9009ef370a2a2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


####4. shell 变量
>1、只能使用数字，字母和下划线，且不能以数字开头
2、变量名区分大小写
3、“=”前后不能有空格
- 在“test.sh”文件内，继续输入
```
#!/usr/bin/env bash
echo "hello world"
myText="hello world"
muNum=100
echo $myText
echo $muNum

echo myText
echo muNum
```
- 当想要访问变量的时候，需要使用$，否则输出的将是纯文本内容，如下图所示。
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5cdc9137bd1301c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 本地变量
  - 只对当前shell进程有效的，对当前进程的子进程和其它shell进程无效。
![image.png](http://upload-images.jianshu.io/upload_images/6634703-afb7e6c127512f36.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 环境变量(export)
  - 自定义的环境变量对当前shell进程及其子shell进程有效，对其它的shell进程无效
![image.png](http://upload-images.jianshu.io/upload_images/6634703-8ec1b2905a861b60.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 局部变量
  - 1. 在函数调用时，函数执行结束，变量就会消失
  - 2. 对shell脚本中某代码片段有效
  - 3. 定义 local Value_name = Value
- 位置变量
  - $0: 脚本名称 
  - $1：脚本的第一个参数 
  - $2：脚本的第二个参数

![image.png](http://upload-images.jianshu.io/upload_images/6634703-adce4bdaed3028af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 特殊变量

$?|接收上一条命令的返回状态码返回状态码在0-255之间
|:---:|:---:|
$$|获取当前shell的进程号（PID）(可以实现脚本自杀)(或者使用exit命令直接退出也可以使用exit [num]) 
$! |Shell最后运行的后台Process的PID 
$- |使用Set命令设定的Flag一览 
$* |所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 
$@ |所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。 
$# |添加到Shell的参数个数 
$0 |Shell本身的文件名 
$1～$n |添加到Shell的各参数值。$1是第1参数、$2是第2参数…。 
```
#!/usr/bin/env bash
printf "The complete list is %s\n" "$$"
printf "The complete list is %s\n" "$!"
printf "The complete list is %s\n" "$?"
printf "The complete list is %s\n" "$*"
printf "The complete list is %s\n" "$@"
printf "The complete list is %s\n" "$#"
printf "The complete list is %s\n" "$0"
printf "The complete list is %s\n" "$1"
printf "The complete list is %s\n" "$2"
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-a773a5a809b3fb70.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


####5. 引号
- ''单引号不解析变量
- ""双引号会解析变量
- ``反引号是执行并引用一个命令的执行结果，类似于$(...)

![image.png](http://upload-images.jianshu.io/upload_images/6634703-f4dd4cffba4d5be7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####6. 循环
- for 循环
```
#!/usr/bin/env bash
# 方法一
for ((i=0;i<10;i++))
do
printf $i
done
echo

# 方法二
for i in 0 1 2 3 4 5 6 7 8 9
do
printf $i
done
echo

# 方法三
for i in {0..9}
do
printf $i
done
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-270473497c2a8f1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- while 循环
```
#!/usr/bin/env bash
COUNTER=0
while [ $COUNTER -lt 5 ]
do
    COUNTER=`expr $COUNTER + 1`
    echo $COUNTER
done

echo '请输入。。。'
echo 'ctrl + c 即可停止该程序'
while read NUM
do
    echo "Yeah! great NUM the $NUM"
done
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-42e06ad09c80580d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####7. 循环控制
```
break  #跳出所有循环
break n  #跳出第n层f循环
continue  #跳出当前循环
```
####8. 条件判断
参数|解释
|:---:|:---:|
-gt|大于
-lt|小于
-ge|大于等于
-le|小于等于
-eq|等于
-ne|不等于

```
#!/usr/bin/env bash
a=10
b=20
if [ $a -eq $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -ne $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -gt $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -lt $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -ge $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -le $b ]
then
   echo "true"
else
   echo "false"
fi
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-35b52f4d0638c782.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

例如[ $num1 -gt $num2 ]或者test $num1 -gt $num2
```
#!/usr/bin/env bash
num1=4
num2=5
str1=Alice
str2=Bob
if [ $num1 -gt $num2 ]
then
echo $num1 large than $num2
else
echo $num1 lower than $num2
fi

if [ -z $str1 ]
then
echo str1 is empty
else
echo str is not empty
fi
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-55d0d81afe6b5035.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- if 判断
```
#!/usr/bin/env bash
a=10
b=20
if [ $a == $b ]
then
   echo "true"
fi


if [ $a == $b ]
then
   echo "true"
else
   echo "false"
fi


if [ $a == $b ]
then
   echo "a is equal to b"
elif [ $a -gt $b ]
then
   echo "a is greater than b"
elif [ $a -lt $b ]
then
   echo "a is less than b"
else
   echo "None of the condition met"
fi
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d10ee0e389fdf6ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- case 判断

a\|b|a或者b
|:---:|:---:|
*|匹配任意长度的任意字符
?|匹配任意单个字符
[a-z]|指定范围内的任意单个字符
```
#!/usr/bin/env bash

num=10
case $num in
    1)
        echo 1
            ;;
    2)
        echo 2
            ;;
    10)
        echo 10
            ;;
    *)
        echo somethin else
        ;;
esac
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-7ac24073eef5b928.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####9. 算数运算
- 加减乘除
```
#!/usr/bin/env bash
echo "Hello World !"
a=3
b=5
val=`expr $a + $b`
echo "Total value : $val"

val=`expr $a - $b`
echo "Total value : $val"

val=`expr $a \* $b`
echo "Total value : $val"

val=`expr $a / $b`
echo "Total value : $val"
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-1ac1ffa971e30557.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 进行四则运算的时候运算符号前后一定要有空格，乘法的时候需要进行转义。

其他运算符|	含义
|:---:|:---:|
%	|求余
==	|相等
=	|赋值
!=	|不相等
!	|非
-o	|或
-a	|与
```
#!/usr/bin/env bash
a=3
b=5
val=`expr $a / $b`
echo "Total value : $val"

val=`expr $a % $b`
echo "Total value : $val"

if [ $a == $b ]
then
   echo "a is equal to b"
fi
if [ $a != $b ]
then
   echo "a is not equal to b"
fi
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-730985360c8e74ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####10. 逻辑运算符

-a |与
|:---:|:---:|
-o |或
！ |非
```
#!/usr/bin/env bash

num1=10
num2=20
num3=15
if [ $num1 -lt $num3 -a $num2 -gt $num3 ]
then
        echo $num3 is between 10 and 20
else
        echo something else
fi
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9858df0dfdf47dcf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- if [ 条件A ] && [条件B ]
- if((A&&B))
- if [[ A&&B ]]
```
#!/usr/bin/env bash

num1=10
num2=20
num3=15
if [[ $num1 -lt $num3 && $num2 -gt $num3 ]]
then
        echo $num3 is between 10 and 20
else
        echo something else
fi
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d8ce1d0b6cbee5c3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####11. 函数
```
#!/usr/bin/env bash
# 定义一个没有返回值的函数，然后调用该函数
sysout(){
    echo "hello world"
}

sysout

# 定一个有返回值的函数，调用该函数，输出结果
test(){

    aNum=3
    anotherNum=5
    return $(($aNum+$anotherNum))
}
test
result=$?
echo $result
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b4b1868e4b26779f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
#!/usr/bin/env bash
# 定义了一个需要传递参数的函数
test(){
    echo $1  #接收第一个参数
    echo $2  #接收第二个参数
    echo $3  #接收第三个参数
    echo $#  #接收到参数的个数
    echo $*  #接收到的所有参数
}
test aa bb cc
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-3f4a341af0f3785b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- read
  - read命令接收标准输入（键盘）的输入，或者其他文件描述符的输入。得到输入后，read命令将数据放入一个标准变量中。
```
#!/usr/bin/env bash
read -p "Enter your name:" VAR_NAME
echo "hello $VAR_NAME, welcome to my program"
read -t 10 -p "enter your name:" VAR_NAME
echo "hello $VAR_NAME, welcome to my program"
read  -s  -p "Enter your password: " pass
echo "hello $VAR_NAME, your password is $pass"
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-425e87d8625cca57.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- declare
  - 申明变量的类型
```
declare [-aixr] variable
-i: 把变量定义为整数
-a: 把变量定义为数组
-x: 把变量变成环境变量
-r: 可读变量
```
```
ChengkaideMacBook-Pro:~ chengkai$ sum=100+300+50
ChengkaideMacBook-Pro:~ chengkai$ echo $sum
100+300+50           # 文字类型的变量属性无法相加
ChengkaideMacBook-Pro:~ chengkai$ declare -i sum=100+300+50 # -i把变量定义为整数数字
ChengkaideMacBook-Pro:~ chengkai$ echo $sum
450
```
####12. 字符窜操作
```
str1="Hello"
str2="World"

echo ${#str1} # 输出字符窜长度
echo ${str1:0:3} # 截取字符窜
echo $str1" "$str2 # 字符窜拼接
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9f6d4b1b1da2f52b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####13. 数组
```
#!/usr/bin/env bash
array=(1 2 3 4 5)  #定义数组
array2=(aa bb cc dd ee)  #定义数组
value=${array[3]}  #找到某一个下标的数，然后赋值
echo $value  #打印
value2=${array2[3]}  #找到某一个下标的数，然后赋值
echo $value2  #打印
length=${#array[*]}  #获取数组长度
echo $length
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-0910f165c92d9381.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####14. 重定向
命令	|说明
|:---:|:---:|
command > file|	将输出重定向到 file。
command < file|	将输入重定向到 file。
command >> file|	将输出以追加的方式重定向到 file。
n > file	|将文件描述符为 n 的文件重定向到 file。
n >> file	|将文件描述符为 n 的文件以追加的方式重定向到 file。
n >& m	|将输出文件 m 和 n 合并。
n <& m	|将输入文件 m 和 n 合并。
<< tag	|将开始标记 tag 和结束标记 tag 之间的内容作为输入。
/dev/null| 禁止输出
- 注意：0 是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。
```
$echo result > file  #将结果写入文件，结果不会在控制台展示，而是在文件中，覆盖写
$echo result >> file  #将结果写入文件，结果不会在控制台展示，而是在文件中，追加写
echo input < file  #获取输入流
$ command > file 2>&1 # 将 stdout 和 stderr 合并后重定向到 file，
$ command < file1 >file2 # command 命令将 stdin 重定向到 file1，将 stdout 重定向到 file2。
```
####15. 其他命令
- date
  - 格式化输出 +%Y-%m-%d
  - 格式%s表示自1970-01-01 00:00:00以来的秒数
```
#!/usr/bin/env bash
echo `date +%Y-%m-%d-%H:%M:%S`
echo `date +%s`
```
- 后台运行脚本
```
bash test.sh &
```
- 不挂断的运行命令
```
nohup test.sh & 
```
####参考文献
1. http://www.jianshu.com/p/71cb62f08768
2. http://blog.csdn.net/u011204847/article/details/51184883

