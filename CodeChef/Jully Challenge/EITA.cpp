#include <bits/stdc++.h>
using namespace std;

int main()
{
    // code
    int t;
    cin>>t;
    while(t){
        int d,x,y,z;
        cin>>d>>x>>y>>z;
        int tS1 = 7*x;
        int tS2 = (d*y)+((7-d)*z);
        cout<<max(tS1,tS2)<<endl;
        t--;
    }
    return 0;
}