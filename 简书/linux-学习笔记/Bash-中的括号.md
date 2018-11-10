####1. []
- 一开始发明[], 来替换test. 为了更美观
####2. [[]]
- 觉得上面[]功能有限，就开发了[[]]。
```
ChengkaideMacBook-Pro:~ chengkai$ help "["
[: [ arg... ]
    This is a synonym for the "test" builtin, but the last
    argument must be a literal `]', to match the opening `['.
[[ ... ]]: [[ expression ]]
    Returns a status of 0 or 1 depending on the evaluation of the conditional
    expression EXPRESSION.  Expressions are composed of the same primaries used
    by the `test' builtin, and may be combined using the following operators
    
    	( EXPRESSION )	Returns the value of EXPRESSION
    	! EXPRESSION	True if EXPRESSION is false; else false
    	EXPR1 && EXPR2	True if both EXPR1 and EXPR2 are true; else false
    	EXPR1 || EXPR2	True if either EXPR1 or EXPR2 is true; else false
    
    When the `==' and `!=' operators are used, the string to the right of the
    operator is used as a pattern and pattern matching is performed.  The
    && and || operators do not evaluate EXPR2 if EXPR1 is sufficient to
    determine the expression's value.
```
####3. (())
- [],[[]]，比较字符串还凑合用，比较数字大小很憋屈，所以开发(()),其实就是在(())里面搞算数运算。
####4. $(())
- 也是计算，但是不会像命令一样有返回值，而是会像变量一样把运算结果替换出来。
```
例如：b=1;echo $((++b))
这时b等于2，显示的也是2，b=1; echo $((b++))这时b等于2，显示的是1.
```
####5. 其他
```
( COMMAND [; ...] )
把一堆命令包起来，放在一个子 shell（subshell）里面运行。你在子 shell 里面切目录、改变
量，全都不会影响到当前这一层。你做一些 shell 之外的改变（例如全盘格式化）的话还是会影
响到的。这玩意前面加个 foo() 的话，可以把一坨命令定义为一个在子 shell 里面运行的函数。
$( COMMAND [; ...] )
和上面那个差不多，但是会把命令的输出替换成字符串。这玩意会把输出末尾的所有换行符都吃
掉，所以你想完全保留输出的话需要动动脑筋。旧社会里有人喜欢用 ` COMMAND `，这破东西
要嵌套起来那叫一个烦。要是有人在你的项目里面那么写，我建议你带个榔头。
{ COMMAND; [... COMMAND; ] }
一个不把命令放在 subshell 里面的包裹。这样你可以重定向一堆命令的输入或者输出，但是仍
然可以修改变量。这玩意前面加个 foo() 的话，可以把一坨命令定义为一个在同级 shell 里面运
行的函数。
```
####6.另一个版本
```
2.1 () 在子shell中运行
    (a=1);echo $a，结果是空，因为a=1不是在当前shell中运行的(a=1);(echo $a)也是空的。
    小技巧：(cd $path, do something) 可以让不切换当前目录而在其它目录干点别的事儿~
    () 还有个功能是数组的赋值：比如a=(1 3 5)，那么${a[0]}=1;${a[1]}=3;${a[2]}=5，需要注意的是，下标是从0开始的。
    
2.2 (()) 表达式计算
    a=1;((a++));echo $a，这时a就是2了。
    
2.3 <() 和 >() 进程代入，可以把命令的执行结果当成文件一样读入
    比如comm前一般需要sort，那就可以这样comm <(sort 1.lst) <(sort 2.lst)
    或者是paste <(cut -t2 file1) <(cut -t1 file1)，和管道差不多，但是支持多个输入。

2.4 $() $(cmd) 执行cmd的结果，
    比如cmd是echo ls，那么就是执行ls，比如file $(which bash)，which bash的结果是/bin/bash，
    所以file $(which bash)等于file /bin/bash。如果你$(ls)，而且你的当前目录下只有a b两个文件，
    那么就是执行a b，然后系统会提示，命令没找到。$() 基本和 `` 等价。
    
2.5 $(()) 表达式扩展，
    和(())很相似，但是这个是有点不同，$(())不能直接$((b++))，例如：b=1;echo $((++b))
    这时b等于2，显示的也是2，b=1; echo $((b++))这时b等于2，显示的是1.
    
2.6 [] 和 [[]]，[] 就是 test，[]和[[]]都是条件表达式，不过[[]]有比[]高的容错性，
    如果a为空，那么[ $a -eq 0 ]会报错，但是[[ $a -eq 0 ]]不会，所以一般都会使用[[]]或者是
    [ "$a" -eq 0 ]，[[]]支持的功能也比 [] 多，比如[[ aaa =~ a{3} ]]，[] 还有一种用途，
    如果你的当前目录下有a1-a9九个文件，你可以用a[1-9]来替代这九个文件。
    有点需要注意，你不能用a[1-20]来代替a1- a20，必须要a[1-9] a1[0-9] a20。
    但是需要注意的是 [[]] 数字进制转换的坑~
    
2.7 $[] 是 $(()) 的过去形式，现在已经不建议使用。

2.8 {n..m} {1..30} 就是1-30，或者是/{,s}bin/表示/bin/和/sbin/，ab{c,d,e}表示abc、abd、abe，
    小技巧：文件备份：cp a.sh{,.bak}
    而 { cmd1; cmd2; } 的作用是定义一个命令组，一般用在单行的条件表达式中：
    [[ 1 -eq 2 ]] && echo True || { echo False; echo "Program will exit！"; }
    其实 shell 函数的语法也是它的变体：
    a(){ i=$1; echo $((i++)); echo $((++i)); } && a 1

2.9 ${} 变量的Parameter Expansion，
    用法很多，最基本的 ${var}1，防止变量扩展冲突，具体可以查看man bash。
```
####8 总结
技巧小结：
```
 字符串比较用双中括号[[ ]]；算数比较用单中括号[ ]——左右留空格
 算数运算用双小括号(( )) ；shell命令及输出用小括号( )——左右不留空格
 快速替换用花括号{ }——左右留空格
 反单引号起着命令替换的作用` `
```
####7 参考文献
1. https://www.zhihu.com/question/266787434
2. https://blog.csdn.net/lvdan1/article/details/78698071
