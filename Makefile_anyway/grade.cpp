#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

 int main(){
     int data[102]={0,0,0,0,0,0,0,5,18,0,0,0,0,0,0,0,0,0,54,43,23,0,0,0,0,0,0,0,0,0};
     


    ofstream outfile;
    //outfile.open("/home/crystal/桌面/coding/makefile anyway/data.txt",  ios::out);
    outfile.open("data.txt",  ios::out);
    if(!outfile.is_open())cout<<"open file fail"<<endl;

    for(int i=0;i<101;++i){
        outfile<<data[i];
        if(i!=100)outfile<<" ";//最後一個不用輸出空格
    }outfile<<endl;
    outfile.close();   

   return 0;

}