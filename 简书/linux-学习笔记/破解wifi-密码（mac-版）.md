####序章
今天学了破解wifi密码，屁颠屁颠跑去新爸爸测试，搞了我两小时都没破出来， 不过地下一楼的家香记到是花了29秒破解了（速度快慢取决与你的字典）。
![image.png](http://upload-images.jianshu.io/upload_images/6634703-d222691c83f469f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

CPU八核满仓跑，确实烧电脑
![image.png](http://upload-images.jianshu.io/upload_images/6634703-6d61ee1ab697396d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
做了虚心事的我，拍照都不敢正面拍了，认识这家店的小伙伴多去吃吃哈，卤鸡腿很鲜美。回来的路上，一脚踩空，脚踝扭了，提醒我不要再干这事啦～～！
![image.png](http://upload-images.jianshu.io/upload_images/6634703-ba16101f93ec843a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
***最后我想说写这篇教程，仅仅用于技能学习交流，如发生任何违法事件，均与本人无关***
***
####1. 安装Xcode和MacPorts
- Xcode 可以在App Store 里面下
- MacPorts 去官网下https://www.macports.org/install.php
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9ee51014d780ed7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. 安装 aircrack-ng
```
sudo port -v selfupdate
sudo port install aircrack-ng
```
- 查看是否安装成功
![image.png](http://upload-images.jianshu.io/upload_images/6634703-b50c9e3770d7f8ba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. 获取所有无线网络
- 建立一个连接
```
sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport
```
- 查看所有无线网络
```
airport -s
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-be81b433e905fce6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4. 开始抓包与监听
- 需要输入密码
- 监听的时候会自动断网
- 抓包抓的是，在你监听的时候，有人连接此Wi-Fi，你可以找一个朋友在你监听的时候重新输入密码连接一下网络，这样会快一些，不然你等别人连接Wi-Fi可能需要一些时间
- 按control+c 结束进程，cap包文件自动保存在/tmp 文件夹下面（/tmp 文件夹，电脑重启自动删除）
```
sudo airport en0 sniff 1
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-5ac17dfa44930fe5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5. 收集字典
- 我用的是下面这位大神的字典，你可以多试试几个txt 文件
```
https://github.com/rootphantomer/Blasting_dictionary
```
####6. 查看cap文件中数据
- 在Finder 下查找／tmp 文件
![image.png](http://upload-images.jianshu.io/upload_images/6634703-3dc8bf85fa36026b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 找到cap 文件，把他拖到桌面
- 在桌面建立文件夹wifiCrack
- 把你的字典.txt 文件也拖进来
![image.png](http://upload-images.jianshu.io/upload_images/6634703-bec7813d88e8b2dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
cd Desktop/wifiCrack/家香记/
aircrack-ng -w 超级字典.txt airportSniffV9NQma.cap
```
![image.png](http://upload-images.jianshu.io/upload_images/6634703-9621d2ec3ab247a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- control +f  寻找“1 handshake”,如果找到，进入步骤#7，如果没找到（即都是0）回到步骤#4
####7. 开始破解
- 在“Index number of target nertwork ？”后面输入你找到的index, 我是8，然后按回车
- 有些密码很复杂，可能需要等很久，有些很简单，比如全是阿拉伯数字的，这个字典破不了就换个字典玩玩，实在不行就暴力破解
![image.png](http://upload-images.jianshu.io/upload_images/6634703-137b37428d6bbbb4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 恭喜你，完美破解！
![image.png](http://upload-images.jianshu.io/upload_images/6634703-1bee06547d038205.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####8. 参考文献
1. https://github.com/rootphantomer/Blasting_dictionary (字典)
2. http://cdn2.jianshu.io/p/f49b6691a6b7 （aircrack-ng破解wifi）
3. http://www.jianshu.com/p/67c0277fd5bc （Mac破解Wifi密码教程）
4. http://www.jianshu.com/p/d3922131319d （三分钟教你破解WIFI无线密码）

