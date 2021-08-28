#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin>>n;
        int currSm=0,currLn=0,mxSm = INT_MIN,mxLn = INT_MIN;
        for(int i=1;i<=n;i++){
            cout << currSm << " " << mxSm << " " << currLn << " " << mxLn << endl;
            if(i%2==0){
                if((currSm%2==0)){
                    currSm+=i;
                }
            }else{
                if(currSm%2!=0){
                    currSm+=i;
                }
            }
            if(currSm>mxSm){
                mxSm = currSm;
                mxLn = currLn;
            }
        }
        cout<<mxLn<<endl;
    }
    return 0;
}