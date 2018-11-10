####移动构造
1. C++ 11 标准中提供了一种新的构造方法--移动构造
2. C++11 之前，如果要将源对象的状态转移到目标对象只能通过复制。在某些情况下，我们有没有必要复制对象----只需要移动他们
3. 移动语义：源对象资源的控制权全部交给目标对象
![image.png](https://upload-images.jianshu.io/upload_images/6634703-5168dde8f970e1f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. 什么时候用移动构造？
- 临时对象即将消亡，但里面的数据还是要用的，所以用移动构造
![image.png](https://upload-images.jianshu.io/upload_images/6634703-6c9245d6ed3dbd73.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-e75170de06d528ab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 移动构造，效率更高一些，把快要释放的资源转移
![image.png](https://upload-images.jianshu.io/upload_images/6634703-05cf458f03b1094a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-96f1089f5c45a829.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####另一个有趣的例子
```
#include <iostream>
using namespace std;

class A {
public:
    int x;
    A(int x) : x(x)
    {
        cout << "Constructor" << endl;
    }
    A(A& a) : x(a.x)
    {
        cout << "Copy Constructor" << endl;
    }
    A& operator=(A& a)
    {
        x = a.x;
        cout << "Copy Assignment operator" << endl;
        return *this;
    }
    A(A&& a) : x(a.x)
    {
        cout << "Move Constructor" << endl;
    }
    A& operator=(A&& a)
    {
        x = a.x;
        cout << "Move Assignment operator" << endl;
        return *this;
    }
};

A GetA()
{
    return A(1);
}

A&& MoveA()
{
    return A(1);
}

int main()
{
    cout << "-------------------------1-------------------------" << endl;
    A a(1);  // 调用构造函数
    cout << "-------------------------2-------------------------" << endl;
    A b = a; // 创建新对象b，使用a初始化b，因此调用拷贝构造函数。
    cout << "-------------------------3-------------------------" << endl;
    A c(a); // 创建新对象c，使用a初始化c，因此调用拷贝构造函数。
    cout << "-------------------------4-------------------------" << endl;
    b = a; // 使用a的值更新对象b，因为不需要创建新对象，所以调用拷贝赋值运算符。
    cout << "-------------------------5-------------------------" << endl;
    A d = A(1); //创建新对象d，使用临时对象A(1)初始化d，由于临时对象是一个右值，所以调用移动构造函数。
    cout << "-------------------------6-------------------------" << endl;
    A e = std::move(a); //创建新对象e，使用a的值初始化e，但调用std::move(a)将左值a转化为右值，所以调用移动构造函数。
    cout << "-------------------------7-------------------------" << endl;
    A f = GetA(); // 创建新对象f，使用GetA()函数返回的临时对象初始化f，由于临时对象是右值，所以调用移动构造函数。值得注意的是，这里调用了两次移动构造函数。第一次是GetA()返回前，A(1)移动构造了一个临时对象。第二次是临时对象移动构造f。
    cout << "-------------------------8-------------------------" << endl;
    A&& g = MoveA(); // 没有创建新对象，也不更新任何对象，只是将MoveA()的返回值绑定到右值引用g。因此不调用构造函数，也不调用赋值运算符。
    cout << "-------------------------9-------------------------" << endl;
    d = A(1); // 使用临时对象A(1)更新d，因为不需要创建新对象，所以调用移动赋值运算符。
    

}
```
```
-------------------------1-------------------------
Constructor
-------------------------2-------------------------
Copy Constructor
-------------------------3-------------------------
Copy Constructor
-------------------------4-------------------------
Copy Assignment operator
-------------------------5-------------------------
Constructor
-------------------------6-------------------------
Move Constructor
-------------------------7-------------------------
Constructor
-------------------------8-------------------------
Constructor
-------------------------9-------------------------
Constructor
Move Assignment operator
Program ended with exit code: 0
```
####参考文献
1. https://www.jianshu.com/p/f5d48a7f5a52
