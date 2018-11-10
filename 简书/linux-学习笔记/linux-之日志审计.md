> root 权限泛滥，导致文件莫名丢失，给服务器造成一定的安全隐患，所以有了这篇服务器日志审计
######1. 安装sudo命令，syslog服务
```
# 查看是否安装 sudo 和syslog
[root@node1 zck]# rpm -aq|egrep "sudo|syslog"
sudo-1.8.6p3-15.el6.x86_64
rsyslog-5.8.10-8.el6.x86_64
```
- 没装的执行下面这条命令
```
yum install sudo syslog -y
```
######2. 配置/etc/sudoers
- 增加配置“Defaults       logfile = /var/log/sudo.log” 到 /etc/sudoers中 （意义：把sudo的命令操作打到log 里面去）
```
[root@node1 zck]# echo "Defaults   logfile=/var/log/sudo.log">>/etc/sudoers
[root@node1 zck]# tail -1 /etc/sudoers # 检查
Defaults   logfile=/var/log/sudo.log
[root@node1 zck]# visudo -c # 检查语法
/etc/sudoers: parsed OK
/etc/sudoers.d/ctdb: parsed OK
```
######3. 配置系统日志/etc/syslog.conf
- 增加配置local2.debug 到/etc/syslog.conf 中。
```
echo "local2.debug   /var/log/sudo.log">>/etc/rsyslog.conf    # 记录debug
```
######4. 重启syslog 内核日志记录器
```
[root@node1 zck]# /etc/init.d/rsyslog restart            # 重启
Shutting down system logger:                               [  OK  ]
Starting system logger:                                    [  OK  ]
[root@node1 zck]# ll /var/log/sudo.log                   # 自动生成一个log
-rw------- 1 root root 0 Apr 30 22:49 /var/log/sudo.log
```
######5. 测试sudo 日志审计配置结果
```
[root@node1 zck]# su zck 
[zck@node1 ~]$ sudo useradd aaa
[sudo] password for zck: 
zck is not in the sudoers file.  This incident will be reported.

[zck@node1 ~]$ cat /var/log/sudo.log       # log里面已经有记录了
Apr 30 23:03:13 : zck : user NOT in sudoers ; TTY=pts/0 ; PWD=/home/zck ;
    USER=root ; COMMAND=/usr/sbin/useradd aaa

```
