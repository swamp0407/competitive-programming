###### 2022年 8月27日 土曜日 21時00分19秒 JST ######

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())


def f1(x, y):
    if ax != cx:
        ans = (ay-cy)/(ax-cx) * (x-cx) + cy - y
    else:
        return x
    return ans


def f2(x, y):
    ax, ay = bx, by
    cx, cy = dx, dy
    if ax != cx:
        ans = (ay-cy)/(ax-cx) * (x-cx) + cy - y
    else:
        return x

    return ans


if f1(bx, by) * f1(dx, dy) >= 0:
    print("No")
    exit()

if f2(ax, ay) * f2(cx, cy) >= 0:
    print("No")
    exit()

print("Yes")
