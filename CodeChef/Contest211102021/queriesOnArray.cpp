#include<bits/stdc++.h>
using namespace std;

int count(vector<int> arr,int l,int r,int x){
    int c=0;
    for(int i=l-1;i<r;i++){
        if(arr[i]>=x)
            c+=1;
    }
    return c;
}

int main(){

    int n,q;
    cin>>n>>q;
    vector<int> arr(n,0);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }   
    while(q--){
        int l,r,x;
        cin>>l>>r>>x;
        int ans = count(arr,l,r,x);
        cout<<ans<<endl;
    }
    return 0;
}