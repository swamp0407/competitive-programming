a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if t*v-t*w >= abs(b-a):
    print("YES")
else:
    print("NO")
