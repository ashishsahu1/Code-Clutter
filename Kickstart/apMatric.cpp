#include<bits/stdc++.h>
using namespace std;

//counting horizontals
int countHor(vector<vector<int>> inp){
    int c=0;
    for(int i=0;i<3;i++){
        if(inp[i][0]-inp[i][1] == inp[i][1]-inp[i][2]){
            c++;
        }
    }
    return c;
}

//counting diagonal
int countDig(vector<vector<int>> inp){
    int c=0;
    if(inp[0][0]-inp[1][1] == inp[1][1]-inp[2][2]){
        c++;
    }
    if(inp[0][2]-inp[1][1] == inp[1][1]-inp[2][0]){
        c++;
    }
    return c;
}

//counting verticals
int countVer(vector<vector<int>> inp){
    int c=0;
    for(int i=0;i<3;i++){
        if(inp[0][i]-inp[1][i] == inp[1][i]-inp[2][i]){
            c++;
        }
    }
    return c;
}

int main(){
    int t;
    cin>>t;
    vector<vector<int>> inp(3,vector<int>(3));
    int k=1;
    while(k<=t){
        int maxC=0;
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(i==1 && j==1){
                    continue;
                }
                cin>>inp[i][j];
            }            
        }
        int g=0;
        while(true){
            inp[1][1]=g;
            int sum = countHor(inp)+countDig(inp)+countVer(inp);
            if(sum<maxC){
                cout<<"Case #"<<k<<": "<<maxC<<endl;
                break;
            }
            maxC = sum;

            g++;
        }
        k++;
    }
}