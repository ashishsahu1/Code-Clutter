#include<bits/stdc++.h>
using namespace std;

int main(){

    int t;
    cin>>t;
    while(t--){
        int a,b,n;
        cin>>n>>a>>b;
        // cout<<n<<a<<b<<endl;
        string s;
        // getline(cin,s);
        cin>>s;
        // cout<<s<<endl;
        int sum=0;
        for(int i=0;i<n;i++){
            // cout<<sum<<endl;
            if(s[i] == '0'){
                sum+=a;
            }else{
                sum+=b;
            }
        }

        cout<<sum<<endl;

    }   
    return 0;
}