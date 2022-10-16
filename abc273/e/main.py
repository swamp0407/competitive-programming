###### 2022年 10月15日 土曜日 21時00分20秒 JST ######
import sys

input = sys.stdin.readline
q = int(input())


ans = []

for i in range(q):
    query = input()
    if query[0] != "D":
        type_, x = query.split()
        x = int(x)
