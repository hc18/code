####1. 安装
```
yum install -y environment-modules
```
####2. 查找安装路径
```
rpm -qa|grep environment-modules
rpm -ql environment-modules-3.2.10-3.el6.x86_64
```
![](https://upload-images.jianshu.io/upload_images/6634703-aa5a2d54a5a89dd3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. 环境配置
```
vim ~/.bashrc
```
```
module () 
  { 
      eval `/usr/bin/modulecmd bash $*`
  }

# 告诉系统，多了一个存放modulefiles的路径
export MODULEPATH=$MODULEPATH:/etc/modulefiles
```
####4. 把python 导入module
```
#%Module1.0
module-whatis ""
prepend-path PATH /root/anaconda3/envs/test_py3/bin
prepend-path LD_LIBRARY_PATH /opt/local/miniconda3/envs/test_py3/lib
prepend-path MANPATH /root/anaconda3/envs/test_py3/man
prepend-path INFOPATH /root/anaconda3/envs/test_py3/info
prepend-path INCLUDEPATH /root/anaconda3/envs/test_py3/include
```
