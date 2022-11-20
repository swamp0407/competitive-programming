#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

void change_cin() {
    // 追加２, 以降 cin の入力元が 'input.txt' になる
    std::ifstream in("input.txt");
    std::cin.rdbuf(in.rdbuf());

    // ...
}

int main() {
    change_cin();
    using namespace std;

    unsigned N;
    cin >> N;

    // i 番目の文字列の最初の文字/最後の文字
    vector<pair<unsigned char, unsigned char>> info(N);
    for (auto&& [first, last] : info) {
        string S;
        cin >> S;
        first = S.front() - 'a';
        last = S.back() - 'a';
    }

    // dp[S] の c bit 目 = S が残っていて直前の文字が c のときの勝敗
    vector<unsigned> dp(1UL << N);
    for (unsigned S{1}; S < 1UL << N; ++S)
        for (unsigned c{}; c < N; ++c)
            if (1 & S >> c)
                dp[S] |= (1UL & ~dp[S ^ 1UL << c] >> info[c].second)
                         << info[c].first;

    // dp[2^N - 1] に立っているビットがあれば先手の勝ち
    cout << (dp.back() ? "First" : "Second") << endl;

    return 0;
}
