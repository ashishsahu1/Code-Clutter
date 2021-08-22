#include<iostream>
using namespace std;

int calDiv(int n){
    if(n<1600){
        return 3;
    }
    if(n<2000){
        return 2;
    }
    return 1;
}

int main(){

    int t;
    cin>>t;
    while(t){
        int n;
        cin>>n;
        cout<<calDiv(n)<<endl;
        t--;
    }
    return 0;
}