n, k = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
score = [0 for _ in range(n)]
loopn = [0 for _ in range(n)]
done = {i: True for i in range(n)}
cycles = []
nux = -1000000000000000
cycles_score = []
for start in range(n):
    if done[start]:
        done[start] = False
        cycle = [start]
        score = C[start]
        nex = P[start]-1
        while nex != start:
            done[nex] = False
            cycle.append(nex)
            score += C[nex]
            nex = P[nex]-1
        cycles.append(cycle)
        cycles_score.append(score)

for score, cycle in zip(cycles_score, cycles):
    l = len(cycle)
    acum = [0 for _ in range(2*l+1)]
    for i in range(2*l):
        acum[i+1] = acum[i]+C[cycle[i % l]]
    if score < 0:
        for r in range(l+1):
            for i in range(l):
                if r == 0:
                    continue
                if r <= k:
                    nux = max(nux, acum[i+r]-acum[i])
    else:
        for r in range(l+1):
            q = (k-r)//l
            for i in range(l):
                if r == 0 and q == 0:
                    continue
                if q <= 0 and r > k:
                    continue
                nux = max(nux, score*q+acum[i+r]-acum[i])


print(nux)

"""n, k = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

score = [0 for _ in range(n)]
loopn = [0 for _ in range(n)]
done = {i: True for i in range(n)}
for start in range(n):
    if done[start]:
        nex = -1
        j = 0
        tuuka = []
        nax = -float("inf")
        while nex != start:
            if nex == -1:
                nex = P[start]-1
            else:
                nex = P[nex]-1
            tuuka.append(nex)
            score[start] += C[nex]
            nax = max(nax, score[start])
            j += 1
        loopn[start] = j
        for i in tuuka:
            done[i] = False
            loopn[i] = j
            score[i] = score[start]
            nokori = k-(k//loopn[start])*loopn[start]

    if score[start] < 0:
        score[start] = 0
    else:
        score[start] = (k//loopn[start])*score[start]
        nokori = k-(k//loopn[start])*loopn[start]
        i = 0
        nnnnn = (k//loopn[start])
        nscore = 0
        nax = 0
        while i < nokori:
            nex = P[nex]-1
            nscore += C[nex]
            if nscore < 0:
                break
            nax = max(nax, nscore)
            i += 1
        if nax > 0:
            score[start] += nax


ans = max(score)
if ans <= 0:
    ans = max(C)
print(ans)
"""
