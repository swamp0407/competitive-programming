#include <iostream>
#include <vector>
using ll = long long;
using namespace std;
int main(){
    int n;
    cin>>n;
    ll L,w;
    cin>>L>>w;
    ll r = 0;
    vector<ll> a(n+1,L);
    for(int i=0;i<n;i++)cin>>a[i];
    ll ans = 0L;
    for(auto x:a)
    {
        if (x > r)
            ans += (x - r + w- 1) / w;
        r = x + w;
    }
    cout<<ans<<endl;
}