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
        vector<int> arr(n, 0);

        int mx = 0;
        map<int, int> mp;

        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            mp[arr[i]]++;
            mx = max(mx, mp[arr[i]]);
        }

        if (n <= 2)
        {
            cout << 0 << endl;
            continue;
        }
        if (mx == 1)
        {
            cout << n - 2 << endl;
            continue;
        }
        cout << n - mx << endl;
    }
    return 0;
}