#include<bits/stdc++.h>
using namespace std;

int main(){

    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int currSm,mxLen = INT_MIN,currLen,mxSm = INT_MIN;
        for(int i=1;i<=n;i++){
            for(int j=i;j<=n;j++){
                currLen=0;
                currSm =0 ;
                for(int k=i;k<=j;k++){
                    currSm+=k;
                    currLen++;
                    // cout<<currSm<<" "<<mxSm<<" "<<currLen<<" "<<mxLen<<endl;
                }
                if(currSm%2==0){
                    if (currSm > mxSm)
                    {
                        mxSm = currSm;
                        mxLen = currLen;
                    }
                }

            }
        }
        cout<<mxLen<<endl;
    }
    return 0;
}