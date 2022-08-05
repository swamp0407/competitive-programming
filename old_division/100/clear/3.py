# 16:06
s = input()
num = 0
ans = 0
for i in range(len(s)):
    if s[i] == "A"or s[i] == "G" or s[i] == "C"or s[i] == "T":
        for j in range(i, -1, -1):
            if s[j] == "A"or s[j] == "C"or s[j] == "G"or s[j] == "T":
                num += 1
            else:
                break
        for k in range(i+1, len(s)):
            if s[k] == "A"or s[k] == "C"or s[k] == "G"or s[k] == "T":
                num += 1
            else:
                break
        if num > ans:
            ans = num
        num = 0
print(ans)
