>以前学过一次，现在忘了,这里做个笔记，就当备忘录了
- 完整的github原理, git命令介绍见：
1. https://www.bilibili.com/video/av10475153/?p=7 （bilibili）
2. https://www.jianshu.com/p/7edb6b838a2e

####如何上传，下载文件
1. 在github 上新建一个仓库，复制该仓库的ssh
2. cd 到你想创建文件夹的目录
```
# 克隆该仓库到本地
git clone git@github.com:wenmobo/LearnGit.git
```
3. 上传代码
```
//文件添加到仓库（.代表提交所有文件）
git add .
//把文件提交到仓库
git commit -m "First Commit"
//上传到github
git push
```
- git commit -m 'first commit' ，这个命令什么意思呢？ commit 是提交的意思，-m 代表是提交信息，执行了以上命令代表我们已经正式进行了第一次提交。
