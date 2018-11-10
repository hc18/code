####1. 插值与拟合，热导系数
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e2540d3607da5f26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
% The first method
T=[68,87,106,140];
P=[9.7981,13.324,9.0078,13.355,9.7918,14.277,9.6563,12.463];
K=[0.0848,0.0897,0.0762,0.0807,0.0696,0.0753,0.0611,0.0651];
T0=99; P0=10.3;
x(1)=interp1(P(1:2),K(1:2),P0);
x(2)=interp1(P(3:4),K(3:4),P0);
x(3)=interp1(P(5:6),K(5:6),P0);
x(4)=interp1(P(7:8),K(7:8),P0);
% 画草图
%plot(T,x,'r+',T,x)
xlabel('T'), ylabel('K'), 
```
![image.png](https://upload-images.jianshu.io/upload_images/6634703-182bc63b36554064.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
