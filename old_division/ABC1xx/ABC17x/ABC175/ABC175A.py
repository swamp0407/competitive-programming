n = input()
if n == "RRR":
    print(3)
elif n == "RRS" or n == "SRR":
    print(2)
elif n == "RSS" or n == "RSR" or n == "SSR" or n == "SRS":
    print(1)
else:
    print(0)  # SSS
