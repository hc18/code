# 转录组入门一（mac版）

1. 安装bioconda: 

- 去官网下载和自己电脑系统一样的版本

    [https://conda.io/miniconda.html](https://conda.io/miniconda.html)


![image.png](http://upload-images.jianshu.io/upload_images/6634703-f1bb635abad99648.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


- 下载完后，双击解压，然后cd 到文件目录，开始安装。

```javascipt
# 安装
bash Miniconda3-latest-MacOSX-x86_64.sh
```

之后会要求看一个license，和安装环境路径，输入yes 就好。
- 激活

```javascipt
source .bash_profile
# 查看是否安装成功
conda
```

![image.png](http://upload-images.jianshu.io/upload_images/6634703-2ee7013f9423c6cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

出现上图代表安装成功

- bioconda 是conda 上一个分发生物信息的频道，所以需要创建一些channels.

```javascript
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
```

- 安装完channels后 需要更新miniconda

```javascript
conda update conda
```

2. 安装配置软件：

-sratoolkit

教程上用的Linux方法，mac会报错，建议使用以下方法。

方法一（别人可以，我的不行）：

```javascript
conda install -c bioconda sra-tools=2.8.1
```

方法二（亲测可行）： 
```javascript  
ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
brew install wget
brew tap homebrew/science
brew install sratoolkit
```

- 余下的安装很简单没报错

```javascipt
conda install fastqc
conda install hisat2
conda install samtools
conda install -c bioconda htseq
conda install r
conda install rstudio
```
## 参考文献
1. http://www.biotrainee.com/thread-1796-1-1.html
2. http://www.biotrainee.com/thread-1800-1-1.html
