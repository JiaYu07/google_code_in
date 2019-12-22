#include<iostream>
#include <ctime>
using namespace std;
int main(){
    int a[1000][5]={},x;
     clock_t  st=clock();
    for(int j=0;j<1000;j++)
        for(int i=0;i<1000;i++)
            x=i+j;
    cout<<"column-major : "<<(float)(clock()-st)/ CLOCKS_PER_SEC<<endl;  

     st=clock();
    for(int i=0;i<1000;i++)
        for(int j=0;j<1000;j++)
            x=i+j;
    cout<<"row-major : "<<(float)(clock()-st)/ CLOCKS_PER_SEC<<endl; 

 
  
    return 0;
}