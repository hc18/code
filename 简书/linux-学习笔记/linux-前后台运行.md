####1. nohup
- 如果直接在终端启动一个程序，那么终端关闭的时候，程序也会被终止，所以要使用nohup让程序后台执行
- 代码
```
nohup java -jar xxx.jar > xxx.log 2>&1 &
```
 >注：
其中 0、1、2分别代表如下含义：
0 – stdin (standard input)
1 – stdout (standard output)
2 – stderr (standard error)
nohup ./startWebLogic.sh >out.log 2>&1 &
nohup+最后面的& 是让命令在后台执行
out.log 是将信息输出到out.log日志中
2>&1 是将标准错误信息转变成标准输出，这样就可以将错误信息输出到out.log 日志里面来。
####2. 进程前后台切换
```
command &   //将进程放在后台执行
ctrl-z      //暂停当前进程 并放入后台
jobs -l       //查看当前后台任务
bg  %num        //将任务转为后台执行, 这里的num 看进程 ID号
fg   %num      //将任务调回前台
kill  %num    //杀掉任务
```
####3. 参考文献
1. https://www.jianshu.com/p/85d2f4da4755
