####1. 下载
```
wget https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh
bash Anaconda3-5.1.0-Linux-x86_64.sh
```
- 添加到环境变量
```
vi /etc/profile
export PATH=/root/anaconda3/bin:$PATH 
source /etc/profile
```
####2.  增加一些生物信息通道
```
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/  # 我用华科的镜像，清华的貌似失效了
conda config --set show_channel_urls yes 
conda update conda  # 更新conda 通道
```
####3. 装一个qiime2
```
conda update conda
conda install wget

wget https://data.qiime2.org/distro/core/qiime2-2018.4-py35-linux-conda.yml
conda env create -n qiime2-2018.4 --file qiime2-2018.4-py35-linux-conda.yml
# OPTIONAL CLEANUP
rm qiime2-2018.4-py35-linux-conda.yml
```
- 激活
```
source activate qiime2-2018.4
qiime --help # 查看帮助
```
####4 查找一个软件,并安装
```
anaconda search -t conda fastq-screen
anaconda show bioconda/fastq-screen
conda install --channel https://conda.anaconda.org/bioconda fastq-screen
conda install --channel https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/ rseqc
```
![](https://upload-images.jianshu.io/upload_images/6634703-4ee1c95a9e345fcf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5 python3 和2 环境配置
- 创建环境
```
# 基于 python3.6 创建一个名为test_py3 的环境
conda create --name test_py3 python=3.6 

# 基于 python2.7 创建一个名为test_py2 的环境
conda create --name test_py2 python=2.7

# 激活 test 环境
activate test_py2  # windows
source activate test_py2 # linux/mac

# 切换到python3
activate test_py3

# 退出环境
source deactivate
```
- conda 的包管理功能是对 pip 的一种补充，如果当前已经激活了某个Python环境，那么就可以在当前环境开始安装第三方包。如果conda 找不到，再用pip 下载也可
```
# 安装 matplotlib 
conda install matplotlib
# 查看已安装的包
conda list 
# 包更新
conda update matplotlib
# 删除包
conda remove matplotlib
```
