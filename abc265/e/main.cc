/**
 *    author:  USERNAME
 *    create-mm-dd hh:mm:ss
 **/

#include <bits/stdc++.h>
using namespace std;

// clang-format off
/* accelration */
// 高速バイナリ生成
#pragma GCC target("avx")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
// cin cout の結びつけ解除, stdioと同期しない(入出力非同期化)
// cとstdの入出力を混在させるとバグるので注意
struct Fast {Fast() {std::cin.tie(0); ios::sync_with_stdio(false);}} fast;

/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using pii = pair<int, int>;

/* define short */
#define pb push_back
#define mp make_pair
#define all(obj) (obj).begin(), (obj).end()
#define YESNO(bool) if(bool){cout<<"YES"<<endl;}else{cout<<"NO"<<endl;}
#define yesno(bool) if(bool){cout<<"yes"<<endl;}else{cout<<"no"<<endl;}
#define YesNo(bool) if(bool){cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}

/* REP macro */
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define rep1(i, n) reps(i, 1, n + 1)
#define rreps(i, a, n) for (ll i = (n-1); i >= (ll)(a); i--)
#define rrep(i,n) rreps(i,0,n)
#define rrep1(i,n) rreps(i,1,n+1)

/* debug */
// 標準エラー出力を含む提出はrejectされる場合もあるので注意
#define debug(x) cerr << "\033[33m(line:" << __LINE__ << ") " << #x << ": " << x << "\033[m" << endl;

/* func */
inline int in_int() {int x; cin >> x; return x;}
inline ll in_ll() {ll x; cin >> x; return x;}
inline string in_str() {string x; cin >> x; return x;}
// search_length: 走査するベクトル長の上限(先頭から何要素目までを検索対象とするか、1始まりで)
template <typename T> inline bool vector_finder(std::vector<T> vec, T element, unsigned int search_length) {
    auto itr = std::find(vec.begin(), vec.end(), element);
    size_t index = std::distance( vec.begin(), itr );
    if (index == vec.size() || index >= search_length) {return false;} else {return true;}
}
template <typename T> inline void print(const vector<T>& v, string s = " ")
    {rep(i, v.size()) cout << v[i] << (i != (ll)v.size() - 1 ? s : "\n");}
template <typename T, typename S> inline void print(const pair<T, S>& p)
    {cout << p.first << " " << p.second << endl;}
template <typename T> inline void print(const T& x) {cout << x << "\n";}
template <typename T, typename S> inline void print(const vector<pair<T, S>>& v)
    {for (auto&& p : v) print(p);}
// 第一引数と第二引数を比較し、第一引数(a)をより大きい/小さい値に上書き
template <typename T> inline bool chmin(T& a, const T& b) {bool compare = a > b; if (a > b) a = b; return compare;}
template <typename T> inline bool chmax(T& a, const T& b) {bool compare = a < b; if (a < b) a = b; return compare;}
// gcd lcm
// C++17からは標準実装
// template <typename T> T gcd(T a, T b) {if (b == 0)return a; else return gcd(b, a % b);}
// template <typename T> inline T lcm(T a, T b) {return (a * b) / gcd(a, b);}
// clang-format on

int main() {
    // code
    int n = in_int();
    int m = in_int();
    ll a, b, cc, d, e, f;
    cin >> a >> b >> cc >> d >> e >> f;
    ll x, y;
    typedef std::pair<ll, ll> pair;
    ll mod = 998244353;
    std::map<pair, ll> block;
    rep(i, m) {
        cin >> x >> y;
        block[mp(x, y)] = 1;
    }
    typedef vector<tuple<ll, ll, ll>> qu;
    qu q;
    q.push_back(make_tuple(0, 0, 1));
    ll dx[4] = {a, cc, e};  // x軸方向への変位
    ll dy[4] = {b, d, f};
    rep(i, n) {
        std::map<pair, ll> next_dict = {};

        for (qu::const_iterator i = q.begin(); i != q.end(); ++i) {
            ll x = get<0>(*i);
            ll y = get<1>(*i);
            ll c = get<2>(*i);
            // cout << "syc" << x << " " << y << " " << c << endl;
            for (ll j = 0; j < 3; j++) {
                ll nx = x + dx[j];
                ll ny = y + dy[j];
                if (block.count(mp(nx, ny))) {
                    continue;
                }
                if (next_dict.count(mp(nx, ny))) {
                    next_dict[mp(nx, ny)] = (next_dict[mp(nx, ny)] + c) % mod;
                } else {
                    next_dict[mp(nx, ny)] = c;
                }
            }
        }
        q.clear();
        for (auto&& p : next_dict) {
            // cout << p.first.first;
            q.push_back(make_tuple(p.first.first, p.first.second, p.second));
        }
        for (qu::const_iterator i = q.begin(); i != q.end(); ++i) {
            ll x = get<0>(*i);
            ll y = get<1>(*i);
            ll c = get<2>(*i);
            // cout << "next" << x << " " << y << " " << c << endl;
        };
    }
    ll ans = 0;

    for (auto&& p : q) {
        ans = (ans + get<2>(p)) % mod;
    }
    cout << ans << endl;
    return 0;
}