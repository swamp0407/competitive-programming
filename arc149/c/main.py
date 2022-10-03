###### 2022年 10月 2日 日曜日 21時00分08秒 JST ######
n =int(input())

def prime(N):
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes
# print(prime(n**2*2))
p = prime(n**2*2)


graph = [[0]*n for _ in range(n)]
print(graph)


def process0(n):
    global graph
    s = [3,5,4,6,2,1]

    for i in range(n):
        for j in range(n):
            graph[i][j] = i*n+j//6*6 + s[(i+j)%6]


def process1(n):
    global graph
    s = [5,4,6,2,1,3]

    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                graph[i][j] = n**2
            else:
                graph[i][j] = (i*n+j)//6*6 + s[(i+j)%6]

def process2(n):
    global graph

def process3(n):
    global graph

def process4(n):
    global graph

def process5(n):
    global graph


if n**2 % 6 == 0:
    process0(n)
elif (n**2) % 6 == 1:
    process1(n)



def print_graph(graph):
    for g in graph:
        print(*g)

print_graph(graph)
