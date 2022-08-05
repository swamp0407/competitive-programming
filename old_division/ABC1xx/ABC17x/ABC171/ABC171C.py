n = int(input())


def cal(n):
    c = ord("a")
    l = ""
    b = n
    while b > 26:
        a = (b-1) % 26
        b = (b-a)//26
        l = l+chr(c+a)
    l = l+chr(c+b-1)
    print(l[::-1])


cal(n)
