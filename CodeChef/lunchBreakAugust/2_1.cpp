#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int sum = (n*(n+1))/2;
        if(sum%2==0){
            cout<<sum<<endl;
        }else{
            cout<<sum-1<<endl;
        }

    }
    return 0;
}