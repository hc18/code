####1. 创建函数
- 可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。
```
# 方法一
function name {
  commands
}
# 方法二
name() {
  commands
}
```
####2. 函数返回值
- 参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255)
```
# 无返回值
demoFun(){
    echo "这是我的第一个 shell 函数!"
}
demoFun

# return 返回
funReturn(){
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    return $(($aNum+$anotherNum))
}
funRetrun
echo "输入的两个数字之和为 $? !"
```
```
ChengkaideMacBook-Pro:linux chengkai$ bash fun.sh 
这是我的第一个 shell 函数!
输入第一个数字: 
1
输入第二个数字: 
2
输入的两个数字之和为 3 !
```
####3. 向函数传递参数
- 如果传入参数为0或者大于2，则报错。如果是1个参数，自身相加，如果为两个参数，相互相加
```
function addem {
    if [ $# -eq 0 ] || [ $# -gt 2 ]
    then
        echo -1
    elif [ $# -eq 1 ]
    then
        echo $[ $1 + $1 ]
    else
        echo $[ $1 + $2 ]
    fi
}
addem 10
addem 10 15
# 函数和变量必须在同一行
addem 10 15 20
```
```
ChengkaideMacBook-Pro:linux chengkai$ bash test1.sh 
20
25
-1
```
```
function func {
    echo $[ $1 * $2 ]
}
if [ $# -eq 2 ]
then
    value=$(func $1 $2)
    echo "The result is $value"
else
    echo "Usage: func a b"
fi
```
```
ChengkaideMacBook-Pro:linux chengkai$ bash test2.sh 2 3
The result is 6
```
####4. 全局变量和局部变量
- 全局变量在shell 脚本中任何地方都能使用；局部变量在函数内部使用，声明前加一个local 就好
```
function fun {
    a=$[ $b + 5 ]
    c=$[ $a * 2 ]
}

a=4
b=6

fun
if [ $a -gt $b ]
then
    echo "$a is larger than $b"
else
    echo "$a is smaller than $b"
fi


function fun {
    local  a=$[ $b + 5 ]
    c=$[ $a * 2 ]
}

a=4
b=6

fun
if [ $a -gt $b ]
then
    echo "$a is larger than $b"
else
    echo "$a is smaller than $b"
fi
```
```
ChengkaideMacBook-Pro:linux chengkai$ bash test3.sh 
11 is larger than 6
4 is smaller than 6
```
####5. 数组变量和函数
- $@ 变量会单独处理每个参数
```
function addarray {
    local sum=0
    local newarray
    newarray=($(echo "$@"))
    for value in ${newarray[*]}
    do
        sum=$[ $sum + $value ]
    done
    echo $sum
}

myarray=(1 2 3 4 5)
# 这里 arg1=${myarray[*]} 也可以
arg1=$(echo ${myarray[*]})
result=$(addarray $arg1)
echo "The result is $result"
```
```
ChengkaideMacBook-Pro:linux chengkai$ bash test4.sh 
The result is 15
```
```
function arraydblr {
    local origarray
    local newarray
    local elements
    local i
    origarray=($(echo "$@"))
    newarray=($(echo "$@"))
    elements=$[ $# -1 ]
    for (( i = 0; i <= $elements; i++))
    {
        newarray[$i]=$[ ${origarray[$i]} * 2 ]
    }
    echo ${newarray[*]}
}

myarray=(1 2 3 4 5)
arg1=$(echo ${myarray[*]})
result=($(arraydblr $arg1))
echo "The new array is: ${result[*]}"
```
```
ChengkaideMacBook-Pro:linux chengkai$ bash test5.sh
The new array is: 2 4 6 8 10
```
####6. 递归函数
```
function factorial {
    if [ $1 -eq 1 ]
    then
        echo 1
    else
        local temp=$[ $1 - 1 ]
        local result=$(factorial $temp)
        echo $[ $result * $1 ]
    fi
}

read -p "Enter value: " value
result=$(factorial $value)
echo "The factorial of $value is: $result"
```
```
ChengkaideMacBook-Pro:linux chengkai$ bash test6.sh
Enter value: 5
The factorial of 5 is: 120
```
