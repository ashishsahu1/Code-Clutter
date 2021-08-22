#include<bits/stdc++.h>
using namespace std;

int equalDif(vector<int> &arr,int n){
    if(n<=2){
        return 0;
    }
    int mx = INT_MIN;
    for(int i=0;i<n;i++){
        mx = max(mx,arr[i]);
    }
    vector<int> count(mx+1,0);
    for(int i=0;i<n;i++){
        count[arr[i]]++;
    }
    int mxElement;
    int currMX = INT_MIN;
    for(int i=0;i<=mx;i++){
        // cout<<currMX<<" ";
        if(count[i]>currMX){
            mxElement = i;
            currMX = count[i];
        }
    }
    // cout<<endl;
    // cout<<mxElement<<endl;
    int c=0;
    for(int i=0;i<n;i++){
        if(arr[i]==mxElement){
            c++;
        }
    }
    // cout<<c<<endl;

    return n-c;
}

int main(){
    int t;
    cin>>t;
    while(t){
        int n;
        cin>>n;
        vector<int> arr(n,0);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        cout<<equalDif(arr,n)<<endl;
        t--;
    }
}