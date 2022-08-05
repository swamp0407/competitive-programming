n = int(input())

flist = [0]*(10**4+10)


def cal(i, j, k):
    return i ** 2+j ** 2 + k ** 2+i*j+j*k+k*i


for i in range(1, 101):
    for j in range(i, 101):
        for k in range(j, 101):
            s = cal(i, j, k)
            if s >= 10**4+5:
                break
            if i == j and j == k:
                flist[s] += 1
            elif i == j:
                flist[s] += 3
            elif j == k:
                flist[s] += 3
            else:
                flist[s] += 6
for i in range(1, n+1):
    print(flist[i])
