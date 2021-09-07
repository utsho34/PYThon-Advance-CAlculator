#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int a,b,c,d,n,g,m,tc;
    cin>>tc;
    while(tc--){
        cin>>a>>b>>c;
    if(a>b){
        g=a-b;
    }
    else{
        g=b-a;
    }
    n=(g*2);
    m = std::max({a,b,c});
    d=c+g;
    if(n<m){
        cout<<"-1"<<endl;
    }
    else if(d>n){
        cout<<c-g<<endl;
    }
    else{
        cout<<d<<endl;
    }

    }
    return 0;

    }

