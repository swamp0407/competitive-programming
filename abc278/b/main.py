###### 2022年 11月19日 土曜日 21時00分25秒 JST ######
h, m = map(int, input().split())


def next(h, m):
    if m == 59:
        if h == 23:
            return 0, 0
        else:
            return h+1, 0
    return h, m+1


def check(h, m):
    h10 = h // 10
    h1 = h % 10
    m10 = m // 10
    m1 = m % 10

    if h1 >= 6:
        return False

    if h10 == 2 and m10 >= 4:
        return False
    return True


while True:

    if check(h, m):
        print(h, m)
        break

    h, m = next(h, m)
