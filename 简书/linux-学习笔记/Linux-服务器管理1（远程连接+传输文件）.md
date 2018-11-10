####1. SSH远程连接Linux服务器
```
# 先ping一下看看能不能连上
ping 127.0.0.1
# 正式连接
ssh student@127.0.0.1 -p 22
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-cfd17b3b5bbfcf60.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 表示ssh连接
2. 表示连接服务器的用户名
3. 表示远程主机的host IP(这里是本机)
4. 表示远程主机端口(默认22)
- 连接后一般会要求输入密码。
####2. Mac 上传文件到Linux服务器
![image.png](http://upload-images.jianshu.io/upload_images/6634703-e0e4945f04aaa967.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 在shell 中打开“新建远程连接”
2. 选择安全文件传输
3. 添加远程主机IP
4. 输入连接服务器的用户名
5. 点击连接
- 连接成功上传文件
```
put 本地文件路径 远程主机路径
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-21fb38509ead670d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 上传文件成功
####3. 下载文件
```
get 远程主机路径 本地文件路径
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9c826025bdb105ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


