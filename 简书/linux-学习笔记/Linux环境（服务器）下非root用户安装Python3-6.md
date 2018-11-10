> 管服务器的学长用perl, python只有2.7版的，各种包都没有，然后我就研究了一下，自己装个python3.6
####1. 安装python
python版本库：[https://www.python.org/ftp/python/](https://www.python.org/ftp/python/)
```
wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4rc1.tgz
tar -xzf Python-3.6.4rc1.tgz
cd Python-3.6.4rc1
mkdir -p /home/zck/zhuchengkai/software/Python-3.6.4rc1
# 编译安装
./configure --prefix="/home/zck/zhuchengkai/software/Python-3.6.4rc1"
make
make install
```
####2 添加环境变量
```
vim ~/.bash_profile
# python 环境变量
export PATH="$PATH:/home/zck/zhuchengkai/software/Python-3.6.4rc1/";
# pip3 环境变量
export PATH="$PATH:/home/zck/zhuchengkai/software/Python-3.6.4rc1/bin/";
```
- 这里有一个坑，当你运行python的时候还是2.7版本的，因为python3的执行脚本名字也叫python(和python2.7一样)，所以执行脚本需要改名字
```
cp python python3
```
![](http://upload-images.jianshu.io/upload_images/6634703-81c9e8147f76c2cc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3 安装其他包
```
pip3 install pandas
pip3 install numpy
pip3 install scipy
pip3 install sklearn
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-307d6d97f6aa61fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######祝君好运～
