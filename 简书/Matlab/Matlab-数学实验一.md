####1. 画散点图
```
x=[1 2 4 7 9 12 13 15 17];
f=[1.5 3.9 6.6 11.7 15.6 18.8 19.6 20.6 21.1];
plot(x,f,'+'),
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-b2e9b1869431f313.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####2. 用前五个点拟合一条过原点的直线 y=kx
```
x1=[1 2 4 7 9 ];
f1=[1.5 3.9 6.6 11.7 15.6 ];
x2=x1';
f2=f1';
x3=x2\f2;
k=x1'\f1'; % 先转置，然后取x1的逆与f1相乘
xx1=0:0.1:9;
y1=k*xx1;
y10=k*9;
plot(x1,f1,'+',xx1,y1),
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-9ed47b49b2c51442.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3 拟合二次函数
![image.png](https://upload-images.jianshu.io/upload_images/6634703-f313180959d3cdae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
x2=[9 12 13 15 17];
f2=[15.6 18.8 19.6 20.6 21.1];
u=f2-k*9;
r1=x2.^2-81;
r2=x2-9;
R=[r1' r2'];
a=R\u';
a1=a(1);a2=a(2);
xx2=9:0.1:17;
y2=a1*(xx2.^2-81)+a2*(xx2-9)+k*9;
y20=k*9;
dy20=2*a1*9+a2;
plot(x2,f2,'+',xx2,y2),
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-ef3c47053565feb5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####4.
![image.png](https://upload-images.jianshu.io/upload_images/6634703-45656ea6c59d47dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dd66c74eef8a78a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
x2=[9 12 13 15 17];
f2=[15.6 18.8 19.6 20.6 21.1];
u=f2-k*x2;
v=(x2/9).^2-2*x2/9+1;
a3=v'\u';
a1=a3/81;
a2=k-2*a3/9;
xx2=9:0.1:17;
y2=a1*xx2.^2+a2*xx2+a3;
y20=a1*81+a2*9+a3;
dy20=2*a1*9+a2;
plot(x2,f2,'+',xx2,y2),
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-fc7a582c71bd7fa7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####5. 数值积分
![image.png](https://upload-images.jianshu.io/upload_images/6634703-333c15a3325e17b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5ae695b32858bd61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-bb01984fbda3a3f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
clear all;
a=0.8;b=0.5;p=0.4;m=0;z=0;
n=100000;
for i=1:n
   x=2*rand(1,2)-1; % [-0.884776377804476,0.833380170934443]
   y=0;
   if x(1)^2+x(2)^2<=1
      y=exp(-0.5/(1-p*p)*(x(1)^2/a^2+x(2)^2/b^2-2*p*x(1)*x(2)/a/b));
      z=z+y;
      m=m+1;
   end
end
P=4*z/2/pi/a/b/sqrt(1-p*p)/n,m  % P ≈ 0.6998
```
