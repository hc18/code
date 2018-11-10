>- 软件安装规范化
>- 不同版本任意切换
```
module load gcc/6.1.1
which gcc
/usr/local/gcc/6.1.1/linux-x86_64/bin/gcc
module switch gcc gcc/6.3.1
which gcc
/usr/local/gcc/6.3.1/linux-x86_64/bin/gcc
```
####参考文献
1. https://enigmahuang.github.io/2017/02/22/Environment-Modules-Usage/
####1 gatk
```
mkdir /usr/share/Modules/modulefiles/gatk
cd /usr/share/Modules/modulefiles/gatk
#%Module1.0
module-whatis "gatk4"
conflict gatk
prepend-path PATH /opt/gatk-4.0.6.0/
```
####2 gcc
```
wget https://ftp.gnu.org/gnu/gcc/gcc-8.2.0/gcc-8.2.0.tar.gz

tar -xvf gcc-8.2.0.tar.gz
cd gcc-8.2.0
./contrib/download_prerequisites
mkdir build
cd build
../configure -enable-checking=release -enable-languages=c,c++ -disable-multilib
sudo make -j
sudo make install
```
> 1.首先解压，然后进入该文件
2.执行 ./contrib/download_prerequisites  ，不要问为什么，其实它是为了下载一些需要依赖的库，以及做好配置工作
3.创建一个文件用来存放编译的文件，进入该文件
>4.执行 ../configure -enable-checking=release -enable-languages=c,c++ -disable-multilib
>5.sudo make(make -j4，这样是多核的系统使用，我使用的是虚拟机，所以使用make选项)
>6.上面步骤完成后看看有没有错误，没有错误就 sudo make install
- 如果仍然报错，是因为make 运行的是老版本，把新版本指定到老版本就好
```
# 把老得改名字，把新的建立软连接
sudo mv /usr/bin/gcc /usr/bin/gcc4.4.7
sudo mv /usr/bin/g++ /usr/bin/g++4.4.7
sudo mv /usr/bin/c++ /usr/bin/c++4.4.7
sudo ln -s /usr/local/bin/gcc /usr/bin/gcc
sudo ln -s /usr/local/bin/g++ /usr/bin/g++
sudo ln -s /usr/local/bin/c++ /usr/bin/c++
```
####3. bedtools
```
https://github.com/arq5x/bedtools2
make
```
- make 报错:undefined reference to `gzopen64'
- 原因是zlib 版本太老，下载新版本，重新指定路径
```
sudo ln -sf /usr/local/lib/libz.so.1.2.11 /usr/lib64/libz.so
# 修改前
[chengkaizhu@Server-Sugon /]$ ls -lhrt /usr/lib64/libz.so
lrwxrwxrwx. 1 root root 25 Jun 25 10:07 /usr/lib64/libz.so -> ../../lib64/libz.so.1.2.3
# 修改后
[chengkaizhu@Server-Sugon /]$ ls -lhrt /usr/lib64/libz.so
lrwxrwxrwx. 1 root root 29 Oct 29 21:52 /usr/lib64/libz.so -> /usr/local/lib/libz.so.1.2.11
```
详见
1：http://blog.sciencenet.cn/blog-656335-842862.html
2. http://xqxia.blog.sohu.com/260954395.html
- 继续报错：“/usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.21' not found ”
```
[chengkaizhu@Server-Sugon bedtools2]$ sudo cp /usr/local/lib64/libstdc++.so.6.0.25 /usr/lib64
[chengkaizhu@Server-Sugon bedtools2]$ ls -lhrt /usr/lib64/libstdc++.so.6
lrwxrwxrwx. 1 root root 19 Oct 27 19:38 /usr/lib64/libstdc++.so.6 -> libstdc++.so.6.0.13
# 删除连接
[chengkaizhu@Server-Sugon bedtools2]$ sudo rm -rf /usr/lib64/libstdc++.so.6
# 创建新的软连接
[chengkaizhu@Server-Sugon bedtools2]$ sudo ln -s /usr/lib64/libstdc++.so.6.0.25 /usr/lib64/libstdc++.so.6
[chengkaizhu@Server-Sugon bedtools2]$ ls -lhrt /usr/lib64/libstdc++.so.6
lrwxrwxrwx. 1 root root 30 Oct 29 22:21 /usr/lib64/libstdc++.so.6 -> /usr/lib64/libstdc++.so.6.0.25
# 查看
[chengkaizhu@Server-Sugon bedtools2]$ strings /usr/lib64/libstdc++.so.6 | grep GLIBC
```
详见：
1. https://itbilu.com/linux/management/NymXRUieg.html
####4. qualimap
```
wget https://bitbucket.org/kokonech/qualimap/downloads/qualimap_v2.2.1.zip
unzip qualimap_v2.2.1.zip


#%Module1.0
module-whatis ""
conflict qualimap
prepend-path PATH /home/chengkaizhu/zhuchengkai/software/qualimap_v2.2.1/
```
####5. vcftools
```
git clone https://github.com/vcftools/vcftools.git
cd vcftools
./autogen.sh
./configure
make
make install
```
