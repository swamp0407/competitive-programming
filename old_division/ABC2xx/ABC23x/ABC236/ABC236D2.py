import time
N = int(input())


tempN = N

l = []
a = "".join([str(i+1) for i in range(2*N)])


def cul(cur, now):

    for k, v in d.items():
        if v == 1:
            pass
        print(k, v)
    # for i in range(1, n):
    #     tnow = now[::]
    #     tcur = cur[::]
    #     tcur.pop(i)
    #     tcur.pop(0)
    #     tnow.append(cur[0])
    #     tnow.append(cur[i])
    #     tnow = now+cur[0]+cur[i]
    #     cul(tcur, tnow)


start = time.time()
cul(a, "", [])
nax = 0
print(time.time()-start)
