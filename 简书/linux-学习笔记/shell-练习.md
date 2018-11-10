> 建议读者先看一下grep,find,awk,sed的用法，再看这篇文章。
####1. 创建目录
```
DIR="路径"
# 一般用[[]]，比[] 功能多
if [ ! -d $Dir ];then
  mkdir -p $DIR
fi
```
####2. 软件安装
- 一键式软件安装，以后便于软件管理
```
# apache install 
apache=httpd-2.2.27.tar.bz2
apache_dir=httpd-2.2.27
apache_url=http://mirrors.cnnic.cn/apache/httpd/
apache_prefix=/usr/local/apache2/

wget -c $apache_url/$apache &&tar -jxvf $apache $$cd $apache_dir ;./configure --prefix=$apache_prefix
if [$? -eq 0];then
  make &&make install
  echo -e "\033[32mThe $apache_dir Server install successfully!\033[0m"
else
  echo  -e "\033[32mThe $apache_dir Server install failed!\033[0m"
  exit
fi
```
####3. 找到文件并打包
- 合并merge 文件
```
test
├── merge1.sh
└── test2
    ├── merge2.sh
    └── test3
        ├── merge3.sh
        └── test4
```
```
for i in `find ./test/ -name "merge*"`
do
 tar -czf merge.tgz $i
done
```
####4. 把 broadcast:10.222.127.255 提取出来变成 10-222-127-255
```
ChengkaideMacBook-Pro:test chengkai$ cat test9
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	inet6 fe80::108e:9978:9183:3678%en0 prefixlen 64 secured scopeid 0x4 
	inet 10.222.107.136 netmask 0xffffc000 broadcast:10.222.127.255
	inet6 fe80::2893:5cff:fe99:39a%awdl0 prefixlen 64 scopeid 0xb 
	inet6 fe80::b062:5cf4:3d21:831d%utun0 prefixlen 64 scopeid 0xd 
	inet6 fe80::aede:48ff:fe00:1122%en5 prefixlen 64 scopeid 0xc 
ChengkaideMacBook-Pro:test chengkai$ cat test9|grep "broadcast"
	inet 10.222.107.136 netmask 0xffffc000 broadcast:10.222.127.255
ChengkaideMacBook-Pro:test chengkai$ cat test9|grep "broadcast"|awk '{print $5}'
broadcast:10.222.127.255
ChengkaideMacBook-Pro:test chengkai$ cat test9|grep "broadcast"|awk '{print $5}'|awk -F: '{print $2}'
10.222.127.255
ChengkaideMacBook-Pro:test chengkai$ cat test9|grep "broadcast"|awk '{print $5}'|awk -F: '{print $2}'|awk -F. '{print $1"-"$2"-"$3"-"$4}'
10-222-127-255
ChengkaideMacBook-Pro:test chengkai$ 
```

####5. 提取出“/boot”分区的磁盘使用率，并判断是否超过95%
```
[chengkaizhu@Server-Sugon opt]$ df | grep '/boot'
/dev/sda1           487652       41830      420222  10% /boot
[chengkaizhu@Server-Sugon opt]$ df | grep '/boot' | awk '{print $5}'
10%
[chengkaizhu@Server-Sugon opt]$ df | grep '/boot' | awk '{print $5}' | awk -F% '{print $1}'
10
[chengkaizhu@Server-Sugon opt]$ [[ `df | grep '/boot' | awk '{print $5}' | awk -F% '{print $1}'` -le 95 ]]&&echo "safe"
safe
```
####6. 统计当前登录到系统中的用户数量，并判断是否超过三个
```
[[ `who | wc -l` -ge 3 ]] && echo "warning"
```
######7. 每隔五分钟监测一次mysqld服务进程的运行状态，若发现mysqld进程已终止，则在“/var/log/messages”文件中追加写入日志信息（包括当时时间），并重启mysqld服务；否则不进行任何操作
```
Process=`ps -ef | grep "mysqld_safe" | grep -v "grep" | wc -l`
if [  $Process != 0 ] ; then
echo "Mysql Process is running"  >> /dev/null
else
echo "`date +"%Y-%m-%d %H:%M:%S"` ERROR: Mysql Process is Not running" >> /var/log/messages
/etc/init.d/mysqld start >> /dev/null
fi

*/5 * * * * /bin/bash /root/1.sh
```
######8. 对于使用“/bin/bash”作为登录shell的系统用户，检查他们在“/opt”目录中拥有的子目录或文件数量，如果超过100个，则列出具体数值及对应的用户账号
```
#!/bin/bash
User=`grep "/bin/bash" /etc/passwd | awk -F ':' '{print $1}'`
Number=`find /opt -user $User | grep -v ^/opt$  | wc -l`
if [  $Number -gt 100 ] ; then
echo $User:$Number
fi
```
######9. 计算“/etc”目录中所有“*.conf”形式的配置文件所占用的总空间大小
```
#!/bin/bash
FileSize=$(ls -l $(find /etc -type f -name  *.conf ) | awk '{print $5}')
total=0
for i in $FileSize
do
total=$(expr $total + $i)
done
echo "total size of conf file is $total"
```
######10. 由用户从键盘输入一个字符，并判断该字符是否为字母、数字或者其他字符，并输出相应的提示信息。
```
#!/bin/bash
read -p "Please input a character: " Cha
m=`echo $Cha | sed s/[a-zA-Z]//g`
n=`echo $Cha | sed s/[0-9]//g`
s=`echo $Cha | sed s/[a-zA-Z0-9]//g`
if [ -z $m  ] ; then
echo "字母"
elif [ -z $n ] ; then
echo "数字"
elif [ -z $s ] ; then
echo "数字字母"
else
echo "your input is 特殊字符"
fi
```
######11. 循环提示用户输入字符串，并将每次输入的内容保存到临时文件“/tmp/input.txt”中，当用户输入“END”字符串时退出循环体，并统计出input.txt文件中的行数、单词数、字节数等信息，统计完后删除临时文件
```
#!/bin/bash
while true
do
read -p "Please input a string: " Str
echo $Str >> /tmp/test.txt
if [ $Str == "end" ];then
break
fi
done
wc /tmp/test.txt && rm -rf /tmp/test.txt
```
######12.  在脚本中定义一个help函数，当用户输入的脚本参数不是“start”或“stop”时，加载该函数并给出关于命令用法的帮助信息，否则给出对应的提示信息
```
#!/bin/bash
help() {
echo "Usage: "$0" start|stop"
}
case "$1" in
start)
echo "starting..."
;;
stop)
echo "stoping..."
;;
*)
help
esac
```
####################################高级版#########################################
######13. 
1、写一个脚本
   (1) 接受一个以上文件路径作为参数；
   (2) 显示每个文件拥有的行数；
   (3) 总结说明本次共为几个文件统计了其行数；
```
#!/bin/bash
#
[ $# -eq 0 ] && echo "At least one path!" && exit 1
for i in $*; do
        echo "$i has $(wc -l $i | awk '{print $1}') lines."
done
echo
echo $#
```
######14.
写一脚本，分别统计/etc/rc.d/rc.sysinit、/etc/rc.d/init.d/functions和/etc/fstab文件中以#号开头的行数之和，以及总的空白行数；
```
declare -i lines_sum1=0
declare -i lines_sum2=0
lines_sum1=$(($(grep "^#" /etc/passwd | wc -l)+$(grep "^#" /etc/ttys | wc -l)+$(grep "^#" /etc/syslog.conf | wc -l)))
lines_sum2=$(($(grep "^$" /etc/passwd | wc -l)+$(grep "^$" /etc/ttys | wc -l)+$(grep "^$" /etc/syslog.conf | wc -l)))
echo "以#号开头的行数之和为：$lines_sum1"
echo "以$号开头的行数之和为：$lines_sum2"
```
######15. 写一个脚本，显示当前系统上所有默认shell为bash的用户的用户名、UID以及此类所有用户的UID之和；
```
#!/bin/bash
declare -i id_sum=0
 
grep "bash$" /etc/passwd | awk -F: '{printf "Username: %-10s UID: %d\\n",$1,$3}'
 
for i in $(grep "bash$" /etc/passwd | awk -F: '{print $3}');do
    id_sum+=$i
done 
echo "默认shell为bash的用户的UID之和为：$id_sum"
```
######16.
写一个脚本，完成以下功能
   (1) 假设某目录(/etc/rc.d/rc3.d/)下分别有K开头的文件和S开头的文件若干；
   (2) 显示所有以K开头的文件的文件名，并且给其附加一个stop字符串；
   (3) 显示所有以S开头的文件的文件名，并且给其附加一个start字符串；
   (4) 分别统计S开头和K开头的文件各有多少；
```
#!/bin/bash
#
declare -i k=0
declare -i s=0
for i in $(ls /etc/rc.d/rc3.d|grep "^K"); do
        echo "$i—-Stop"
        let k++
done
for i in $(ls /etc/rc.d/rc3.d|grep "^S"); do
        echo "$i—-Start"
        let s++
done
echo -e  "K file:$k\\nS file:$s"
```
######17. 写一个脚本，完成以下功能
   (1) 脚本能接受用户名作为参数；
   (2) 计算此些用户的ID之和；
此脚步需要与用户交互：
```
#!/bin/bash
#
declare -i sum=0
read -p "请输入用户,输入完毕请按q键：" user
until [ $user == q ]; do
        if id $user &>/dev/null; then
                let sum+=$(id -u $user)
                echo "现在用户的UID之和是: $sum"
        else
                echo "你输入的用户不存在,请重新输入！退出请按q键。"
        fi
        read -p "请输入用户,输入完毕请按q键：" user
done
echo "所有的用户UID和是: $sum"
```
```
#!/bin/bash
declare -i sum
if [ $# -lt 1 ];then
    echo "At least one username"
    exit 1
else
    for name in $*
    do
        if id $name &> /dev/null;then
            let sum+=$(grep "^\\" /etc/passwd | cut -d: -f3)
        fi
    done
    echo "id sum is $sum"
fi
```
######18. 写一个脚本
   (1) 传递一些目录给此脚本；
   (2) 逐个显示每个目录的所有一级文件或子目录的内容类型；
   (3) 统计一共有多少个目录；且一共显示了多少个文件的内容类型；
```
#!/bin/bash
#
declare -i d=0
declare -i s=0
declare -a file
file=( $* )
echo ${file[*]}
for ((i=0;i> ./type.txt
                elif [ -c $a ]; then
                        echo "$a type is char."
                        echo "c" >> ./type.txt
                elif [ -d $a ]; then
                        echo "$a type is directory."
                        echo "d" >> ./type.txt
                        let d++
                elif [ -S $a ]; then
                        echo "$a type is socket."
                        echo "S" >> ./type.txt
                elif [ -L $a ]; then
                        echo "$a type is ln."
                        echo "L" >> ./type.txt
                elif [ -p $a ]; then
                        echo "$a type is p."
                        echo "p" >> ./type.txt
                elif [ -f $a ]; then
                        echo "$a type is file."
                        echo "f" >> ./type.txt
                fi
        done
done
echo "have $d directory."
echo "All Type :$(grep -o "[bcdSLpf]" ./type.txt | sort -u | wc -l)"
\\mv  ./type.txt /tmp
```
######19. 打印九九乘法表。
```
#!/bin/bash
#
for ((i=1;i<=9;i++)); do
        for ((j=1;j<=i;j++)); do
                echo -e -n "$j*$i=$((i*j))\\t"
        done
        echo
done
```
######20. 
写一个脚本，接受一个路径参数：
(1) 如果为普通文件，则说明其可被正常访问；
(2) 如果是目录文件，则说明可对其使用cd命令；
(3) 如果为符号链接文件，则说明是个访问路径；
(4) 其它为无法判断；
```
if [ $# -lt 1 ];then
  echo "please input a url"
fi
if [ -L $1 ];then
  echo "this is a access url"
elif [ -d $1 ];then
  echo "can use cd common"
elif [ -f $1 ];then
  echo "normal access"
else
 echo "unknow"
fi
```

######21.
写一个脚本，显示用户选定要查看的信息；
   cpu) display cpu info
   mem) display memory info
   disk) display disk info
   quit) quit
非此四项选择，则提示错误，并要求用户重新选择，只到其给出正确的选择为止；
```
#!/bin/bash
#
while true; do
read -p "Input you argu(cpu/mem/disk/quit):" argu
case $argu in
        cpu)
                lscpu;;
        mem)
                cat /proc/meminfo;;
        disk)
                fdisk -l s[hd][a-z];;
        quit)
                exit 1;;
        *)
                echo "error"
                continue;;
esac
done
```
######22.
写一个shell脚本来看看你最喜欢敲的命令是哪个？然后列出你最喜欢敲的命令top10。
```
cat ~/.bash_history | awk '{print $1}' | sort |uniq -c | sort -rn |head -n 10 |sed "$i"'p' -n | awk '{print $2}'

cat  .bash_history |sort -n |uniq -c |sort -rn |head -10
```
######23. find 
```
#查找/data目录以.log结尾,文件大于10k的文件,同时cp到/tmp目录;

find /data/ -name "*.log" –type f -size +10k -exec cp {} /tmp/ /;

#查找/data目录以.txt结尾,文件大于10k的文件,权限为644并删除该文件;

find /data/ -name "*.log" –type f -size +10k -m perm 644 -exec rm –rf {} /;

#查找/data目录以.log结尾,30天以前的文件,大小大于10M并移动到/tmp目录;

find /data/ -name "*.log" –type f -mtime +30 –size +10M -exec mv {} /tmp/ /;
```
######24.awk
```
$ awk '$1>2 && $2=="Are" {print $1,$2,$3}' log.txt    #命令
#输出
3 Are you

# 去掉注释，去掉重复的标题，去掉空行
awk '!/#/ {print}' aaa | awk '!/TOTAL_GQ0_VARIANTS/ {print $6}'|awk '{if($0!="")print}'

# 统计A_G的转换率，处理压缩文件
for i in $files
do
	A_G=$(gzip -dc $i|awk '!/#/ {print $4,$5}'|awk '$1=="A" && $2=="G" {print}'|wc -l)
	echo ""A_G:" $A_G" 
done
```
```
# 找到压缩的vcf 文件
files=$(find ./ -name "*HC.vcf.gz")

for i in $files
do
# 数变异数
zcat $i|awk '!/#/ {print}'|wc -l
done
```
####参考文献
1. http://blog.51cto.com/tengxiansheng/1708428
2. http://blog.51cto.com/szk5043/1892069
3. http://blog.51cto.com/afterdawn/1916633










