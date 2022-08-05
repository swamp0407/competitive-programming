import math
a, b, h, m = map(int, input().split())

x = (a*math.cos(2*math.pi*(60*h+m)/720) -
     b*math.cos(2*math.pi*m/60))**2
y = (a*math.sin(2*math.pi*(60*h+m)/720)-b*math.sin(2*math.pi*m/60.0))**2
print((x+y)**0.5)
