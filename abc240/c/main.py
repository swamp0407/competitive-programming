n, x = map(int, input().split())

ok = {}
ok[0] = 1
for i in range(n):
    a, b = map(int, input().split())
    tok = {}
    for o in ok.keys():
        tok[o+a] = 1
        tok[o+b] = 1
    ok = tok

# print(ok.keys())
if x in ok.keys():
    print("Yes")
else:
    print("No")
