>在Linux上下载软件有三种方式：
1 在软件仓库里下载如（apt-get）
2 软件仓库里没有，去官网下载文件（编译好的可执行文件），本地安装
3 官网也没有，就去下载源码，先编译成可执行文件，后安装
####1. 一些基本概念
- package：包。这是软件的二进制安装包。类似Windows中软件的安装程序（大多以.exe结尾）。
- dependency：依赖。一个软件包可能需要其他的软件包作为运行的基础。这是依赖关系。
- repository：仓库。软件的仓库，就是存放软件的服务器，我们从这些服务器上下载软件。
- 开放源码：就是程序码，写给人类看的程序语言，但机器并不认识，所以无法执行；
- 编译器：将程序码转译成为机器看的懂得语言，就类似翻译者的角色；
- 可执行文件：经过编译器变成二进制程序后，机器看的懂所以可以执行的文件。
####2. 软件仓库安装
- apt-get update：软件包缓存的更新
```
sudo apt-get update
```
- apt-cache search：搜索软件包
```
sudo apt-cache search
```
- apt-get install：安装软件包
```
# xxx是对应软件包名
sudo apt-get install xxx
```
- apt-get upgrade：升级所有已安装的软件包
```
sudo apt-get upgrade
```
####3. 本地软件包安装
- 下载与解压文件
```
wget  '地址'
tar -xzvf  '文件'
```
- ubuntu 只支持deb安装包，alien 可以把rpm 转成deb
```
# alien默认没有安装，所以首先要安装它。
sudo apt-get install alien
# 将rpm转换为deb，完成后会生成一个同名的xxxx.deb。
sudo alien xxxx.rpm
```
- 安装
```
sudo dpkg -i *.deb
```
- 卸载
```
sudo dpkg -r 包名
```
####4. 编译安装
- 假如实在找不到deb安装包，那么只能：获取软件的源代码，然后自行编译了

```
# 去官网下载源代码并解压
wget '地址'
tar -xzvf '文件'
```
- 配置编译选项, 比如指定软件的安装路径 `.configure --prefix=/安装/路径`,(通过 `./configure --help` 可以查看其它安装选项）
```
./configure --prefix=$HOME/usr 
```
- `make` 表示将源代码编译生成二进制文件. 如果在 make 过程中出现 error, 需要记下错误, 上网搜索别人的解决方案(提醒一下: error 并不只出现在最后一行);
- `make test` 是对上一步的 make 生成的二进制文件进行检查, 测试在你的环境下能否正确执行这些二进制文件;
- `sudo make install` 表示把之前生成的二进制文件复制到 --prefix 指定的安装路径中. 因为要向系统写入文件, 所以需要 sudo 获取 root 权限.
```
make && make test && sudo make install
```
