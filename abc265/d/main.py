###### 2022年 8月21日 日曜日 21時00分20秒 JST ######
n, p, q, r = map(int, input().split())

A = list(map(int, input().split()))
s_pqr = p+q+r
candidates = []
s_now = 0
right = 0
for left, a in enumerate(A):

    while right < n and s_now < s_pqr:
        s_now += A[right]
        right += 1

    if s_now == s_pqr:
        candidates.append((left, right))

    # print(left, right, candidates)
    s_now -= A[left]


for x, y in candidates:
    p_ok = 0
    q_ok = 0
    r_ok = 0
    s_sum = 0
    for i in range(x, y):
        s_sum += A[i]
        # print(x, y, i, s_sum)
        if not p_ok:
            if s_sum < p:
                continue
            elif s_sum == p:
                p_ok = 1
            else:
                break
        elif not q_ok:
            if s_sum < p+q:
                continue
            if s_sum == p+q:
                q_ok = 1
            else:
                break
        elif p_ok and q_ok:
            print("Yes")
            exit()


print("No")
