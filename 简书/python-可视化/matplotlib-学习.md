1. 基本语法
```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50) # 生成-1到1,50个点
y = x**2

plt.figure() # 创建一个窗口
plt.plot(x,y) # 在窗口上画一副图，x是横坐标，y是纵坐标
plt.show() # 输入show,运行时才能看到图
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-33acfb99c29eafb2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 加一条线
```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50) # 生成-1到1,50个点
y1 = x**2
y2 = 2*x+1

plt.figure() # 创建一个窗口
plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--') # 加一条颜色为红色，宽度为1的虚线
plt.plot(x,y1) # 在窗口上画一副图，x是横坐标，y是纵坐标
plt.show() # 输入show,运行时才能看到图
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-a95d63065825ec20.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 坐标轴设置
```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50) # 生成-1到1,50个点
y1 = x**2
y2 = 2*x+1

plt.figure() # 创建一个窗口
plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--') # 加一条颜色为红色，宽度为1的虚线
plt.plot(x,y1) # 在窗口上画一副图，x是横坐标，y是纵坐标
plt.xlim((-1,2)) # 设置x轴坐标的范围是-1，2
plt.ylim((-2,3)) # 设置y轴坐标的范围是-2，3
plt.xlabel('I am x') # 设置x轴标签
plt.ylabel('I am y') # 设置y轴标签
new_ticks = np.linspace(-1,2,5) # -1,2 生成5个点
plt.xticks(new_ticks) # 把x 轴的小标换了
plt.yticks([-2,-1,0,1,1.5,2,3],
           ["A","B","C","D","hello","world","!"]) # 把y标签换成你想换的小标


plt.show() # 输入show,运行时才能看到图
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-1c9bc11cc381178d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 移动坐标轴
```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50) # 生成-1到1,50个点
y1 = x**2
y2 = 2*x+1

plt.figure() # 创建一个窗口
plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--') # 加一条颜色为红色，宽度为1的虚线
plt.plot(x,y1) # 在窗口上画一副图，x是横坐标，y是纵坐标
plt.xlim((-1,2)) # 设置x轴坐标的范围是-1，2
plt.ylim((-2,3)) # 设置y轴坐标的范围是-2，3
plt.xlabel('I am x') # 设置x轴标签
plt.ylabel('I am y') # 设置y轴标签
new_ticks = np.linspace(-1,2,5) # -1,2 生成5个点
plt.xticks(new_ticks) # 把x 轴的小标换了
plt.yticks([-2,-1,0,1,1.5,2,3],
           ["A","B","C","D","hello","world","!"]) # 把y标签换成你想换的小标

ax=plt.gca() # 一个图的四个边
ax.spines['right'].set_color('none') # 右边设为0
ax.spines['top'].set_color('none') # 上边设为0
ax.xaxis.set_ticks_position('bottom') # 下边设为x轴
ax.yaxis.set_ticks_position('left') # 左边设为y轴
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))  # 把原点移动到0，0点
plt.show() # 输入show,运行时才能看到图
```
![](https://upload-images.jianshu.io/upload_images/6634703-9a60ebd03062ed37.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. legend 图例
```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50) # 生成-1到1,50个点
y1 = x**2
y2 = 2*x+1

plt.figure() # 创建一个窗口

plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--',label='down') # 加一条颜色为红色，宽度为1的虚线
plt.plot(x,y1,label='up') # 在窗口上画一副图，x是横坐标，y是纵坐标
plt.legend(loc='best') # 让电脑自己找最好的位置
plt.xlim((-1,2)) # 设置x轴坐标的范围是-1，2
plt.ylim((-2,3)) # 设置y轴坐标的范围是-2，3
plt.xlabel('I am x') # 设置x轴标签
plt.ylabel('I am y') # 设置y轴标签
new_ticks = np.linspace(-1,2,5) # -1,2 生成5个点
plt.xticks(new_ticks) # 把x 轴的小标换了
plt.yticks([-2,-1,0,1,1.5,2,3],
           ["A","B","C","D","hello","world","!"]) # 把y标签换成你想换的小标

plt.show() # 输入show,运行时才能看到图
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d6c611852bf4df15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
5. Annotation 标注
```
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=2*x+1
plt.figure(num=1,figsize=(8,5),)
plt.plot(x,y,)

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x0=1
y0=x0*2+1
plt.scatter(x0,y0,s=50,color='b') # 用散点的形式加入,大小为50，颜色为blue
plt.plot([x0,x0],[y0,0],'k--',lw=2.5) #画一条垂直的虚线，大小为2.5,颜色为black

# 注释一
plt.annotate("2x+1=%s"% y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',\
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

# 注释二
plt.text(-3.0,3,"This is the annotation.",fontdict={'size':16,'color':'r'})

```
![](https://upload-images.jianshu.io/upload_images/6634703-754dbfcf8a2c95f3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

6. 散点图
```
import matplotlib.pyplot as plt
import numpy as np

n=1024
X=np.random.normal(0,1,n) # 生成平均数是0，方差是1的1024个数
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X) #设置点的颜色
plt.scatter(X,Y,s=75,c=T,alpha=0.5) # alpha 透明度50%

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(()) # 隐藏坐标
plt.yticks(())
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-fdc33b65382a2a7b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
7. 柱状图
```
import matplotlib.pyplot as plt
import numpy as np

n=12
X = np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white') # 朝上的Y
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white') # 朝下的Y

for x,y in zip(X,Y1): # zip X，Y分别传入x,y
    #ha,ve,横向和纵向的对其方式
    plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')
for x,y in zip(X,Y2): # zip X，Y分别传入x,y
    #ha,ve,横向和纵向的对其方式
    plt.text(x,-y-0.05,'%.2f'%y,ha='center',va='top')
plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6574788c1d269693.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
8.等高线
```
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1-x/2 +x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y) # 网格的输入值
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot) # y的一个值对应一个颜色
C=plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5) # 8 是等高线的密度
plt.clabel(C,inline=True,fontsize=10)
plt.xticks(())
plt.yticks(())
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-614d23e336b920cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
9. image
```
import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.92) #压缩成90%

plt.xticks(())
plt.yticks(())
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-b376e3938b593fd1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
10.subplot
```
import matplotlib.pyplot as plt

# example 1:
###############################
plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num)
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(222)
plt.plot([0, 1], [0, 2])

plt.subplot(223)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])

plt.tight_layout()
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ffa6fc6c71d29ed8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# method 1: subplot2grid
##########################
plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
ax5 = plt.subplot2grid((3, 3), (2, 1))
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-d9ae789ca49a9135.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
# method 2: gridspec
#########################
plt.figure()
gs = gridspec.GridSpec(3, 3)
# use index from 0
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-7a72f041250fa24f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 3: easy to define structure
####################################
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])

plt.tight_layout()
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-39d28a051e9a9ba6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
11. 图中图
```
import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# below are all percentage
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')


# different method to add axes
####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-157a30b0be6c10b8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
