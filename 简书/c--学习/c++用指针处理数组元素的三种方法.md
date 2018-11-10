> 设有一个int 型数组a, 有10个元素，用三种方法输出各元素
```
#include<iostream>
using namespace std;

int main(){
    int a[10]={1,2,3,4,5,6,7,8,9,0};
    for (int i=0;i<10;i++) //下标法
        cout<<a[i]<<" ";
    cout<<endl;
    for (int i=0;i<10;i++) //数组名和指针运算法
        cout<<* (a+i)<<" ";
    cout<<endl;
    for (int *p=a;p<a+10;p++) //指针变量
        cout<<*p<<" ";
    cout<<endl;
    return 0;
}
``` 
```
1 2 3 4 5 6 7 8 9 0 
1 2 3 4 5 6 7 8 9 0 
1 2 3 4 5 6 7 8 9 0 
Program ended with exit code: 0
```
