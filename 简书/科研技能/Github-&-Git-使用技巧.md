![image.png](https://upload-images.jianshu.io/upload_images/6634703-2bd76b7ec478d7b8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####1. 目的
- 借助github 托管项目代码
####2. 基本概念
1. 仓库 - Repository
- 仓库即你的项目，你想在GitHub上开源一个项目，那就必须要新建一个Repository。如果你开源的项目有多个，那么你就有多个Repositories。
2. 收藏 - Star
- 收藏项目，方便下次查看。如果你的项目被收藏的次数越多，那么你的项目也就越受广大开发者的欢迎咯。
3. 复制克隆项目 - Fork
- 如果你开源了一个项目，别人想在你这个项目的基础之上做些改进，然后应用到自己的项目中，这时他就可以Fork你的项目，然后他的GitHub主页上就多了一个项目，只不过这个项目是基于你的项目为基础（相当于别人拿到了一个副本）。Fork之后，他就可以随心所欲地去改进，但是丝毫不会影响原有项目的代码与结构。
4. 发起请求 - Pull Request
- 如果别人在你的项目基础之上做了一些改进，并且觉得改得很不错，应该要把这些改进让更多的人受益。于是，他就想把自己的改进合并进原有项目之中，这时他就可以发起一个Pull Request。而原有项目创建人也就是你，可以收到这个请求，这个时候你可能会仔细review他的代码，并且测试后觉得OK，就可以接受他的Pull Request，之后他做的改进就可以融入到原有项目之中了。
5. 关注 - Watch
- 类似于微博中的关注，如果你Watch了某个项目，那么以后只要这个项目有任何更新，你都会第一时间收到关于这个项目的通知提醒。
6. 事务卡片 - Issue
- 你开源了一个项目，别人发现你的项目中有bug，或者哪些地方做的不够好，他就可以给你提一个Issue（即问题）。你如果看到了这些Issue，就可以逐个去Fix修复，修复OK之后就可以一个一个地Close掉。
7. GitHub 主页
- 个人信息：头像、个人简介、关注我的人，我关注的人，我关注的Git库，我的开源项目，我贡献的开源项目信息 等等。
![图片来源知乎](https://upload-images.jianshu.io/upload_images/6634703-81473f9b196f75c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. 注册github
- [注册教程](https://jingyan.baidu.com/article/455a9950abe0ada167277864.html)
1. 需要邮箱验证，可能需要翻墙
2. 私有仓库只能自己或者指定的朋友才有权限操作（需要收费）
####4. 创建仓库
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f7214592cd71349b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 仓库主页
![image.png](https://upload-images.jianshu.io/upload_images/6634703-985a2b2f2fa988ab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5 仓库管理
1. 创建文件
![image.png](https://upload-images.jianshu.io/upload_images/6634703-2914a15345216d57.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 填写记录信息
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9c4ec6ab29cf80d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 6 其他一些功能
- 发起issue (比较简单略) 
- fork （比较简单略）
####7 安装 git
- 目的
> 通过git 管理 github 托管项目代码
- [官网下载](https://git-scm.com/downloads)
- 下载合适自己电脑的版本，注意下面两步，其他傻瓜式点next
![](https://upload-images.jianshu.io/upload_images/6634703-650a92a7353434d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1fbe082559c2ee6a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####8 Git 基本工作流程
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f297d71f649d8b30.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####9 Git 初始化操作及仓库管理 (本地操作)
1. 基本信息设置
```
# 设置用户名
git config --global usr.name 'zhangsan'
# 设置账户邮箱
git config --global user.email 'zhangsan@qq.com'
```
- 新建一个文件夹作为你的Git Workspace，然后右键打开Git Bash命令行界面：
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e63011bb48356916.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 初始化一个新的Git 仓库
```
mkdir test1
cd test1
git init
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6b50ec750690913c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 向仓库中添加文件
```
touch hello.py # 创建一个文件
git status # 查看文件状态
git add hello.py # 添加文件到缓存
git commit -m ' add hello.py' # 将文件从暂存区提交到仓库
```
3. 修改文件
- 修改之后要重新提交
4. 删除文件
- 三步
```
rm -rf hello.py
git rm hello.py
git commit -m 'hello.py'
```
####10 git管理远程仓
- 将本地仓库同步到git 远程仓库中   （git push）
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1ea2c63d21344554.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. Git clone: 先将远程仓库复制到本地
![image.png](https://upload-images.jianshu.io/upload_images/6634703-86ef3e5065a9b93f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
git clone https://github.com/zckoo007/PlaneWars.git
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a1feda0068d3f088.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 修改代码，然后再上传
```
git add PlaneWars
git status
git commit -m 'add PlaneWars'
git push 
```
- 报了个错
![image.png](https://upload-images.jianshu.io/upload_images/6634703-aeddc8f85cedb5d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 原因是缺少推送的目的地
```
git remote add origin
git push
```
