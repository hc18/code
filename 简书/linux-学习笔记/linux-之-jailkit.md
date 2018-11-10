>需求：实验室来了批实习生，领导说，让他们用数据，但不能下载数据。然后就有了这篇学习笔记
>- Jailkit
可以建立一些只能使用特定命令的帐户
限制用户活动范围和权限
搭建安全的SSH多用户环境
辅助建立安全的生产环境
######1. 安装布置
```
cd /usr/local/src
wget http://olivier.sessink.nl/jailkit/jailkit-2.19.tar.bz2
tar xf jailkit-2.19.tar.bz2
./configure --prefix=/usr/local/src/jailkit-2.19
make
make install
```
######2. 配置受限环境
- 我们需要建立一个目录来存放所有受限环境的配置。目录不要建在`jailkit-2.19`里面，会报错。
```
mkdir -p /home/jail
```
######2.1  jk_init 设置在受限环境中能运行的命令
```
jk_init -v /home/jail netutils basicshell jk_lsh ssh id scp ftp
```
-  scp是linux系统下基于ssh登陆进行安全的远程文件拷贝命令。所以需要禁止
![image.png](https://upload-images.jianshu.io/upload_images/6634703-08dc95b4ab52ac75.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
chmod 700 scp # 改变用户权限
```
######3 创建受限制的用户
- 具体见[服务器创建账户+建立软连接+更改权限](https://www.jianshu.com/p/73703fbab315)
```
useradd luzhaofeng
passwd luzhaofeng
```
######4 把用户丢进“监狱”
```
jk_jailuser -j /home/jail/ -s /bin/bash luzhaofeng
```
- cat /etc/passwd 查看,发现用户的登录主目录已经在jail里。用的shell 也是特殊shell
```
cat /etc/passwd
yzm:x:549:549::/home/yzm:/bin/bash
luzhaofeng:x:553:553::/home/jail/./home/luzhaofeng:/usr/sbin/jk_chrootsh
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f11c233414641ede.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



