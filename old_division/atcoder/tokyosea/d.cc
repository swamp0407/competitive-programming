#include <iostream>
using namespace std;

int n, W;
int weight[100000], value[100000];
int dp[100000][100000 + 10];
int knapsack(int v, int L)
{
    if (v == 1)
    {

        if (weight[v - 1] > L)
        {
            dp[v][L] = 0;
            return 0;
        }
        else
        {
            dp[v][L] = value[v - 1];
            return value[v - 1];
        }
    }
    if (dp[v][L] != -1)
    {
        return dp[v][L];
    }
    if (L < weight[v - 1])
    {
        dp[v][L] = knapsack(v / 2, L);
    }
    else
    {
        dp[v][L] = max(knapsack(v / 2, L),
                       knapsack(v / 2, L - weight[v - 1]) + value[v - 1]);
        return dp[v][L];
    }
    return 0;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> value[i] >> weight[i];

    int q;
    cin >> q;
    int v, L;
    for (int i = 0; i < q; i++)
    {
        cin >> v >> L;
        int a;
        a = knapsack(v, L);
        printf("%d", a);
    }
}
