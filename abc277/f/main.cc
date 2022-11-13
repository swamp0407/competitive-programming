#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int h, w;
int a[1000005];
vector<int> G[2000005];
bool used[2000005];
vector<int> topo;

void dfs(int v) {
    used[v] = true;
    for (auto u : G[v])
        if (!used[u]) dfs(u);
    topo.push_back(v);
}

int main(void) {
    std::ifstream in("input.txt");
    std::cin.rdbuf(in.rdbuf());
    cin >> h >> w;
    for (int y = 1; y <= h; y++)
        for (int x = 1; x <= w; x++) cin >> a[(y - 1) * w + (x - 1)];

    vector<pair<int, int>> vec;
    for (int y = 1; y <= h; y++) {
        int l = 1e9, r = -1e9;
        for (int x = 1; x <= w; x++) {
            int v = a[(y - 1) * w + (x - 1)];
            if (v) l = min(l, v), r = max(r, v);
        }
        if (l <= r) vec.push_back({l, r});
    }
    sort(vec.begin(), vec.end());

    for (int i = 1; i < (int)vec.size(); i++) {
        if (vec[i - 1].second > vec[i].first) {
            cout << "No" << endl;
            return 0;
        }
    }

    for (int y = 1; y <= h; y++) {
        vector<pair<int, int>> vec;
        for (int x = 1; x <= w; x++)
            if (a[(y - 1) * w + (x - 1)])
                vec.push_back({a[(y - 1) * w + (x - 1)], x});
        sort(vec.begin(), vec.end());

        for (int i = 1; i < (int)vec.size(); i++) {
            if (vec[i - 1].first != vec[i].first) {
                int v = w + vec[i - 1].first;
                for (int j = i - 1; j >= 0; j--) {
                    if (vec[j].first != vec[i - 1].first) break;
                    G[vec[j].second].push_back(v);
                }
                for (int j = i; j < (int)vec.size(); j++) {
                    if (vec[j].first != vec[i].first) break;
                    G[v].push_back(vec[j].second);
                }
            }
        }
    }

    int n = w + h * w;
    for (int i = 1; i <= n; i++)
        if (!used[i]) dfs(i);
    reverse(topo.begin(), topo.end());

    for (int i = 1; i <= n; i++) used[i] = false;
    for (auto v : topo) {
        used[v] = true;
        for (auto u : G[v]) {
            if (used[u]) {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;

    return 0;
}
