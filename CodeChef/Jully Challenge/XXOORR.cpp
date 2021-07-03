#include <bits/stdc++.h>
using namespace std;

int main()
{
    // code
    int t;
    cin >> t;
    while (t)
    {
        int n, k;
        cin >> n >> k;
        int ans = 0;
        vector<int> a(n, 0);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        vector<int> frame(32, 0);
        //binary conversion
        int l;
        for (int i = 0; i < n; i++)
        {
            l = 0;
            int x = a[i];
            while (x)
            {
                frame[l] += (x % 2);
                x = x / 2;
                l++;
            }
        }

        for (int i = 0; i < 33; i++)
        {
            cout<<ans<<" ";
            if(frame[i]%k==0){
                ans = ans+(frame[i]/k);
            }else{
                ans = ans+1+(frame[i]/k);
            }
        }
        cout<<ans<<endl;
        t--;
    }
    return 0;
}