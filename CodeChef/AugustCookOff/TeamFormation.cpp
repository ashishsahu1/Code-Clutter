#include<bits/stdc++.h>
using namespace std;

int calTeam(string s,string t,int n){
    int onlyP=0,onlyE=0,both=0,non=0;
    // cout<<s.length()<<endl;
    if(stoi(s)==0 || stoi(t)==0){
        return 0;
    }
    for(int i=0;i<s.length();i++){
        // cout<<s[i]<<" "<<t[i]<<endl;
        if(s[i]=='1' && t[i]=='1'){
            both++;
        }
        else if (s[i] == '1' && t[i] == '0'){
            onlyP++;
        }
        else if (s[i] == '0' && t[i] == '1')
        {
            onlyE++;
        }
        else if (s[i] == '0' && t[i] == '0')
        {
            non++;
        }
    }
    // cout<<onlyP<<" "<<onlyE<<" "<<both<<" "<<non<<endl;
    int tot = ((onlyE+onlyP)/2)+((both+non)/2);
    // cout<<tot<<endl;
    return tot;
}

int main(){

    int q;
    cin>>q;
    while(q--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        // cout<<s.length()<<endl;
        string t;
        cin>>t;
        // cout<<t.length()<<endl;

        cout<<calTeam(s,t,n)<<endl;
    }
    return 0;
}