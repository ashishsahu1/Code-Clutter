#include <iostream>
#include <limits.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int a, b, c, d, e;
        cin >> a >> b >> c >> d >> e;
    
        if((a+b<=d && c<=e) || (a+c<=d && b<=e) || (b+c<=d && a<=e)){
            cout<<"Yes"<<endl;
        }else{
            cout<<"No"<<endl;
        }
    }
}