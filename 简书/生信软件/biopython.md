####1. 软件安装
```
conda create -n bioinformatics biopython=1.65 python=3.4
source activate bioinformatics
conda install scipy matplotlib ipython-notebook binstar pip
conda install pandas cython numba scikit-learn seaborn
conda install pygraphviz
conda install pysam simuPOP pyvcf dendropy rpy2
```
- 安装docker
```
 https://www.docker.com/. 
```
```
docker build -t bio
       https://raw.githubusercontent.com/tiagoantao/bioinf-
       python/master/docker/3/Dockerfile
```
- docker 教程: https://docs.docker.com/docker-for-mac/#kubernetes
####2. Python and the Surrounding Software Ecology
```
# 下载index
wget -nd ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/historical_data/former_toplevel/sequence.index -O sequence.index
```
