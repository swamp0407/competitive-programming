import bisect


def sum_of_intervals(intervals):
    sintervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    first = [x[0] for x in sintervals]
    index = 0
    ans = 0
    print(sintervals)
    print(first)
    while index != len(first):
        end = sintervals[index][1]
        end2 = end + d-1
        print("index", index)
        print(end2
        index=bisect.bisect_right(first, end2)
        ans += 1
    return ans


n, d=map(int, input().split())
intervals=[]

for i in range(n):
    l, r=map(int, input().split())
    intervals.append([l, r])
a=sum_of_intervals(intervals)
print(a)
