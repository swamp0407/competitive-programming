###### 2022年 12月17日 土曜日 21時00分29秒 JST ######
n = int(input())
S = list(input())


is_replace = 1


ans = []
for s in S:
    if s == '"':
        is_replace = 1-is_replace

    if s == ',' and is_replace:
        ans.append(".")
    else:
        ans.append(s)

print("".join(ans))
