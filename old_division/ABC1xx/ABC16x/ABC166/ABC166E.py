import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    n = int(lines[0])
    dict = {}
    mod = 10**6
    for i in range(n):
        a, b = map(int, lines[i+1].split())
        bmod = b % mod
        if a == 0:
            while not dict.get(bmod) == b:
                dict[bmod] = b
                bmod = bmod+1
        else:
            while 1:
                if dict.get(bmod) == None:
                    print("not found")
                    break
                if dict.get(bmod) == b:
                    print("found")
                    break
                bmod = bmod+1


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
