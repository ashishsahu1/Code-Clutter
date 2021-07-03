#include <bits/stdc++.h>
using namespace std;

bool isInterleave(string s1, string s2, string s3)
{
    int i = 0, j = 0, k = 0;
    int n1 = s1.length();
    int n2 = s2.length();
    while (i < n1 || j < n2)
    {
        cout<<i<<" "<<j<<" "<<k<<" "<<endl;
        if (s1[i] == s3[k])
        {
            i++;
            k++;
            continue;
        }
        else if (s2[j] == s3[k])
        {
            j++;
            k++;
            continue;
        }
        else
        {
            return false;
        }
    }
    return true;
}

int main()
{
    // code
    string s1 = "aabcc",s2="dbbca",s3="aadbbcbcca";
    bool ans = isInterleave(s1,s2,s3);
    cout<<ans<<endl;
    return 0;
}