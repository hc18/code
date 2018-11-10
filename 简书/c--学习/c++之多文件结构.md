- 一个c++程序，一般都由三个部分来构成的：类的定义，类的成员的实现和主函数。
- 一个项目（至少）由三个文件组成：定义类文件（*.h 或者 *.hpp）,类实现文件（*.cpp 文件），类使用文件（主函数文件 *.cpp）
> 本篇实现，如何将一个文件编变成一个项目
####1. Point.cpp
```//5_5.cpp
#include <iostream>
using namespace std;
class Point //Point类定义
{
public: //外部接口
    Point(int x=0, int y=0) :x(x), y(y){ //构造函数
    count++;
    }
    Point(Point &p){        //复制构造函数
        x=p.x;
        y=p.y;
        count++;
    }
    ~Point(){  count--; }    //析构函数，程序运行完，释放内存
    int GetX() {return x;}
    int GetY() {return y;}
    static void showCount() { //静态函数成员
        cout<<" Object count="<<count<<endl;
    }
   
private:    //私有数据成员
    int x,y;
    static int count;  //静态数据成员，用于记录点的个数
};
int Point::count=0;    // 静态数据成员定义和初始化，使用类名限定

int main()             //主函数实现
{
    Point a(4,5);   //定义对象a，其构造函数会使count 加1
    cout<<"Point A,"<<a.GetX()<<","<<a.GetY();
    a.showCount();   //输出对象号，对象名引用，等价于Point::showCount()
    Point b(a); //定义对象b，其构造函数会使count 加1
    cout<<"Point B,"<<b.GetX()<<","<<b.GetY();
    Point::showCount();  //输出对象个数
    
    return 0;
}
```
```
Point A,4,5 Object count=1
Point B,4,5 Object count=2
Program ended with exit code: 0
```
####2. 拆分
1. ponit.h
```
//文件1，类的定义，point.h
class Point{
public:
    Point(int x=0, int y=0) :x(x), y(y){}
    Point(const Point &p);
    ~Point(){  count--; }    //析构函数，程序运行完，释放内存
    int GetX() {return x;}
    int GetY() {return y;}
    static void showCount();
private:    //私有数据成员
    int x,y;
    static int count;  //静态数据成员，用于记录点的个数
};
```
2. point.cpp
```
//文件二，类的实现
#include "point.h"
#include <iostream>
using namespace std;

int Point::count=0;

Point::Point(const Point &p):x(p.x),y(p.y){ //复制构造函数体
    count++;
}
void Point::showCount(){
    cout<<" Object count="<<count<<endl;
}
```
3. main.cpp
```
//文件三，主函数
#include "point.h"
#include <iostream>
using namespace std;

int main(){
    Point a(4,5);   //定义对象a，其构造函数会使count 加1
    cout<<"Point A,"<<a.GetX()<<","<<a.GetY();
    a.showCount();   //输出对象号，对象名引用，等价于Point::showCount()
    Point b(a); //定义对象b，其构造函数会使count 加1
    cout<<"Point B,"<<b.GetX()<<","<<b.GetY();
    Point::showCount();  //输出对象个数
    return 0;
}
```
```
Point A,4,5 Object count=0
Point B,4,5 Object count=1
Program ended with exit code: 0
```
