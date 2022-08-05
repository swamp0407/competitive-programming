
def check(list1, list2, l, n):
    list3 = [[0, 0]]*m
    diffx = list2[l][0]-list1[0][0]
    diffy = list2[l][1]-list1[0][1]

    for i in range(m):
        list3[i][0] = list1[i][0]+diffx
        list3[i][1] = list1[i][1]+diffy

    return list_check2(list3, list2)


def list_check2(list1, list2):
    return set(list1).issubset(list2)


m = int(input())
list1 = []
list2 = []
for i in range(m):
    aa, bb = map(int, input().split())
    list1.append([aa, bb])
n = int(input())
for i in range(n):
    aa, bb = map(int, input().split())
    list2.append([aa, bb])
list1.sort()
list2.sort()
for l in range(m):
    if check(list1, list2, l, n):
        print(list2[l][0]-list1[0][0], list2[l][1]-list1[0][1])
