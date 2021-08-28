#include <bits/stdc++.h>
using namespace std;

int calc(int n){
    if (n == 1 || n == 2)
    {
        return 1;
    }
    if (n == 3)
    {
        return 3;
    }
    if (n == 4 || n == 5)
    {
        return 4;
    }
    return (calc(n - calc(n - 1))) + (calc(n - calc(n - 2))) + (calc(n - calc(n - 3)));
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        
        cout<<calc(n)<<endl;
    }
    return 0;
}