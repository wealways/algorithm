import sys
sys.stdin = open('BOJ10828.txt')
input=sys.stdin.readline

for _ in range(int(input())):
    arr = []
    v = -1
    for _ in range(int(input())):
        user = list(input().split())
        if user[0]=='push':
            arr.append(int(user[1]))
            v += 1
        elif user[0]=='top':
            if v>=0:
                print(arr[v])
            else:
                print(-1)
        elif user[0]=='pop':
            if v>= 0:
                print(arr[v])
                v -= 1
                arr = arr[:-1]
            else:
                print(-1)
        elif user[0]=='size':
            print(v+1)
        else:
            if v>=0:
                print(0)
            else:
                print(1)
