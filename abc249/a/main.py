a, b, c, d, e, f, x = map(int, input().split())

aa = x//(a+c)

ansA = aa * a*b + min((x-aa*(a+c)), a)*b


bb = x//(d+f)

ansB = bb * d*e + min((x-bb*(d+f), d))*e


if ansA > ansB:
    print("Takahashi")
elif ansA == ansB:
    print("Draw")
else:
    print("Aoki")
