n = int(input())

S = [input() for _ in range(5)]
for i in range(1, n+1):
    if (S[0][4*i-3:4*i] == "###"and
        S[1][4*i-3:4*i] == "#.#"and
        S[2][4*i-3:4*i] == "#.#"and
        S[3][4*i-3:4*i] == "#.#"and
            S[4][4*i-3:4*i] == "###"):
        print(0, end="")
    elif (S[0][4*i-3:4*i] == ".#."and
          S[1][4*i-3:4*i] == "##."and
          S[2][4*i-3:4*i] == ".#."and
          S[3][4*i-3:4*i] == ".#."and
          S[4][4*i-3:4*i] == "###"):
        print(1, end="")
    elif (S[0][4*i-3:4*i] == "###"and
          S[1][4*i-3:4*i] == "..#"and
          S[2][4*i-3:4*i] == "###"and
          S[3][4*i-3:4*i] == "#.."and
          S[4][4*i-3:4*i] == "###"):
        print(2, end="")

    elif (S[0][4*i-3:4*i] == "###"and
          S[1][4*i-3:4*i] == "..#"and
          S[2][4*i-3:4*i] == "###"and
          S[3][4*i-3:4*i] == "..#"and
          S[4][4*i-3:4*i] == "###"):
        print(3, end="")
    elif (S[0][4*i-3:4*i] == "#.#"and
          S[1][4*i-3:4*i] == "#.#"and
          S[2][4*i-3:4*i] == "###"and
          S[3][4*i-3:4*i] == "..#"and
          S[4][4*i-3:4*i] == "..#"):
        print(4, end="")
    elif (S[0][4*i-3:4*i] == "###"and
          S[1][4*i-3:4*i] == "#.."and
          S[2][4*i-3:4*i] == "###"and
          S[3][4*i-3:4*i] == "..#"and
          S[4][4*i-3:4*i] == "###"):
        print(5, end="")
    elif (S[0][4*i-3:4*i] == "###"and
          S[1][4*i-3:4*i] == "#.."and
          S[2][4*i-3:4*i] == "###"and
          S[3][4*i-3:4*i] == "#.#"and
          S[4][4*i-3:4*i] == "###"):
        print(6, end="")
    elif (S[0][4*i-3:4*i] == "###"and
          S[1][4*i-3:4*i] == "..#"and
          S[2][4*i-3:4*i] == "..#"and
          S[3][4*i-3:4*i] == "..#"and
          S[4][4*i-3:4*i] == "..#"):
        print(7, end="")
    elif (S[0][4*i-3:4*i] == "###"and
          S[1][4*i-3:4*i] == "#.#"and
          S[2][4*i-3:4*i] == "###"and
          S[3][4*i-3:4*i] == "#.#"and
          S[4][4*i-3:4*i] == "###"):
        print(8, end="")
    elif (S[0][4*i-3:4*i] == "###"and
          S[1][4*i-3:4*i] == "#.#"and
          S[2][4*i-3:4*i] == "###"and
          S[3][4*i-3:4*i] == "..#"and
          S[4][4*i-3:4*i] == "###"):
        print(9, end="")
    else:
        print("????????????")
