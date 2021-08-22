#include<bits/stdc++.h>
using namespace std;

int main(){

    int q;
    cin>>q;
    while(q--){
        int n;
        cin>>n;
        string s,t;
        cin>>s;
        cin>>t;
        int c_s=0,c_t=0;
        for(int i=0;i<n;i++){
            if(s[i]=='1'){
                c_s++;
            }
            if(t[i]=='1'){
                c_t++;
            }
        }
        cout<<min(c_s,min(c_t,n/2))<<endl;
    }
    return 0;
}