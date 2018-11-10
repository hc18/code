####1. 数学思路
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e657b59a030cabbc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 详细推导见
https://my.oschina.net/keyven/blog/526010
####2. 代码实现
- 整个程序分为两个文件，Point 类的头文件Point.h 和程序主函数所在文件main.cpp
1. point.h
```
//文件1，类的定义，point.h
#ifndef _POINT_H
#define _POINT_H

class Point{
public:
    Point(float x=0, float y=0) :x(x), y(y) {}
    float GetX() const {return x;}
    float GetY() const {return y;}
private:
    float x,y;
};
#endif
```
2. main.cpp
```
//主函数，main.cpp
#include "point.h"
#include <iostream>
#include <cmath>
using namespace std;

//直线线性拟合，points 为各点，nPoint 为点数
float lineFit(const Point points[], int nPoint) //友元函数体
{
    float avgX=0,avgY=0;    //定义变量
    float lxx=0,lyy=0,lxy=0;
    for(int i=0;i<nPoint;i++)   //计算X、Y的平均值
    {
        avgX+=points[i].GetX()/nPoint;
        avgY+=points[i].GetY()/nPoint;
    }
    for(int i=0;i<nPoint;i++)   //计算Lxx、Lyy和Lxy
    {
        lxx+=(points[i].GetX()-avgX)*(points[i].GetX()-avgX);
        lyy+=(points[i].GetY()-avgY)*(points[i].GetY()-avgX);
        lxy+=(points[i].GetX()-avgX)*(points[i].GetY()-avgY);
    }
    cout<<"This line can be fitted by y=ax+b."<<endl;
    cout<<"a="<<lxy/lxx;  //输出回归系数a
    cout<<" b="<<avgY-lxy*avgX/lxx<<endl;   //输出回归系数b
    return float(lxy/sqrt(lxx*lyy)); //返回相关系数r
}

int main()
{
    Point p[10]={Point(6,10),Point(14,20),Point(26,30),
        Point(33,40),Point(46,50),Point(54,60),Point(67,70),
        Point(75,80),Point(84,90),Point(100,100)};  //初始化数据点
    float r=lineFit(p,10);    //进行线性回归计算
    cout<<"Line coefficient r="<<r<<endl; //输出相关系数
    return 0;
}
```
```
This line can be fitted by y=ax+b.
a=0.97223 b=5.90237
Line coefficient r=0.998193
Program ended with exit code: 0
```
