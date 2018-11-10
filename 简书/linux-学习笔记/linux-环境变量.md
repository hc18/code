####1. Linux环境变量分类
一、按照生命周期来分，Linux环境变量可以分为两类：
1、永久的：需要用户修改相关的配置文件，变量永久生效。
2、临时的：用户利用export命令，在当前终端下声明环境变量，关闭Shell终端失效。

二、按照作用域来分，Linux环境变量可以分为：
1、系统环境变量：系统环境变量对该系统中所有用户都有效。
2、用户环境变量：顾名思义，这种类型的环境变量只对特定的用户有效。
####2. 临时环境变量
- 只在当前shell 有效，关闭后无效
```
# $PATH 查看当前命令和程序目录
ChengkaideMacBook-Pro:~ chengkai$ $PATH
-bash: /Users/chengkai/miniconda3/bin:/Users/chengkai/Desktop/ENTER/bin:/usr/local/homebrew/bin:

# 加入临时环境变量, "." 代表加入当前目录
PATH=$PATH:.
$PATH
-bash: /Users/chengkai/miniconda3/bin:/Users/chengkai/Desktop/ENTER/bin:/usr/local/homebrew/bin:.:

PATH=$PATH:/home/christine/Scripts
-bash: /Users/chengkai/miniconda3/bin:/Users/chengkai/Desktop/ENTER/bin:/usr/local/homebrew/bin:.:/home/christine/Scripts:
```
####3. 永久环境变量
```
/etc/profile #系统环境变量
$HOME/.bash_profile # 用户环境变量
$HOME/.bashrc # 用户环境变量
$HOME/.bash_login # 用户环境变量
$HOME/.profile # 用户环境变量
```
####3.1 系统环境变量
- `/etc/profile`对所有用户有效
```
# added by Anaconda3 installer
export PATH="/root/anaconda3/bin:$PATH"
```
####3.2 用户环境变量
- shell 会按照`$HOME/.bash_profile, $HOME/.bash_login, $HOME/.profile ` 顺序查找，**只运行第一个被找到的文件，余下的则忽略**
- `.bash_profile` 启动文件会先去检查HOME目录中是不是还有一个叫`.bashrc` 的启动文件。如果有的话，会先执行启动文件里面的命令。
```
[chengkaizhu@Server-Sugon population]$ cat /home/chengkaizhu/.bash_profile 
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs
PATH=$PATH:$HOME/bin
export PATH
```
```
[chengkaizhu@Server-Sugon population]$ cat /home/chengkaizhu/.bashrc
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific aliases and functions

export PATH=/root/anaconda3/bin:$PATH

module () 
  { 
      eval `/usr/bin/modulecmd bash $*`
  }

export MODULEPATH=$MODULEPATH:/etc/modulefiles

```
####4 总结
- 如果你是服务器管理员，公共大型软件可以加在`/etc/profile`,如 python，R， java等
- 个性化的软件和包，可以装在`.bashrc`
