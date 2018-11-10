####理论相关
- User：
```
管理员
    UID：0，GID：0
系统用户
    UID：1-499  GID：1-499（Centos6）
    UID：1-999  GID：1-999(Centos7)
普通用户
    UID:500-60000  GID:500-6000(Centos6)
    UID:1000-60000 GID:1000-60000(Centos7)
```
- group:
```
分类一：
    系统组
    普通用户组
分类二：
    基本组
    附加组
分类三：
    私有组
    公有组
注：组的UID、GID跟用户的分配类似
```
- File Mode：
```
Linux系统安全上下文：
    当一个用户发起一个进程时，此进程将继承用户的属主、属组的权限，再以进程继承的权限来控制文件的访问权限。
Linux权限标识：
    r: Readable 读
    W: writable 写
    x: executable 执行
rwx标识对文件及目录的意义：
    对文件：
        r : 可以读取文件中的内容
        w : 可以修改及删除文件中的内容
        x : 可以将其发起为一个进程
    对目录：
        r : 可以查看目录中的文件，可以使用ls命令， 但不能使用 -l选项
        w : 可以创建、删除目录，但不能修改文件中的内容
        x : 可以使用cd命令进入目录
文件及目录权限详细表示方面
    文件：-rwxrwxrwx
        从左边第二位开始，每三位代表一个权限类别：
            u : owner
            g : owner group
            o : other
            a : 代表以上三项
    目录：drwxrwxrwx
            u、g、o同文件权限位
    
Linux内核对文件权限的表示方法：
    rwx: 4 2 1
```
####1、用户信息文件：/etc/passwd
![image.png](https://upload-images.jianshu.io/upload_images/6634703-775f4f27054b07dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>  1：用户名，用户登录系统时使用的用户名
2：密码位
3：UID，用户标识号
4：GID，缺省组标识号
5：用户注释信息:Comment,可以完善用户的基本信息
6：用户家目录: 系统登录用户后的工作目录
7：用户使用的shell，默认为bash
######1.1 想知道系统有多少个用户，可以直接使用wc -l /etc/passwd
>[root@node1 zhuchengkai]# wc -l /etc/passwd
73 /etc/passwd
######1.2 密码文件 /etc/shadow
>[root@node1 zhuchengkai]# cat /etc/shadow
root:$6$1bdnZ6nO$ULp8lVBx/SglaucS91CiOax6OYGrDqY43gAkNFxZ8PopST7tV.wVUEyDku/dyMl5BWNlSD2yoQgCZGcehaSjL0:17542:0:99999:7:::

|root|$6$1bdnZ6nO$ULp8lVBx/SglaucS91CiOax6OYGrDqY43gAkNFxZ8PopST7tV.wVUEyDku/dyMl5BWNlSD2yoQgCZGcehaSjL0|17542|0|99999|7||
|---|---|---|---|---|---|---|
用户名|密码|上一次修改密码的时间|密码最小使用期限|最长使用期限|警告时间|帐户过期时间|保留字段|
- 如果把/etc/shadow文件中的相应的加密密码删除，那么用户不需要密码就可以登陆系统了
