####1. Linux软件安装目录惯例
- Linux 的软件安装目录是也是有讲究的，理解这一点，在对系统管理是有益的

- /usr：系统级的目录，可以理解为C:/Windows/，/usr/lib理解为C:/Windows/System32.

- /usr/local：用户级的程序目录，可以理解为C:/Progrem Files/。用户自己编译的软件默认会安装到这个目录下。


- /opt：用户级的程序目录，可以理解为D:/Software，opt有可选的意思，这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接rm -rf掉即可。在硬盘容量不够时，也可将/opt单独挂载到其他磁盘上使用。

####2. 源码放哪里？

- /usr/src：系统级的源码目录。

- /usr/local/src：用户级的源码目录。

####3. yum 安装软件路径查询
```
yum install environment-modules
rpm -qa|grep environment-modules
rpm -ql environment-modules-3.2.10-3.el6.x86_64
```
![](https://upload-images.jianshu.io/upload_images/6634703-aa5a2d54a5a89dd3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. 参考文献
1. http://blog.csdn.net/aqxin/article/details/48324377
