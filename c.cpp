#include<iostream>
#include<algorithm>
using namespace std;


int solve(){
    int n,k,i=0,j=0;
    int arr[1000000000];
    cin>>n>>k;
    for(i;i<n;i++){
        cin>>arr[i];
    }
    int a,b;
    n = sizeof(arr) / sizeof(arr[0]);
    for(j;j<k;j++){

        cin>>a>>b;
        if(count(arr, arr + n, a)==0){
            cout<<"no"<<endl;
            return 0;
        }
        if(count(arr, arr + n, b)==0){
            cout<<"no"<<endl;
            return 0;
        }
        int pos_a,pos_b;
        for(i=0;i<n;i++){
            if(arr[i]==a){
                pos_a=i;
                break;
            }
        }
        for(i=0;i<n;i++){
            if(arr[i]==b){
                pos_b=i;
            }
        }
        if(pos_b>pos_a){
            cout<<"YES"<<endl;
        }
        else    
            cout<<"no"<<endl;
        return 0;
    }
}


int main(){
    int t;
    cin>>t;
    while(t--){
        int g=solve();
    }
    return 0;
}