import sys
from collections import deque
sys.stdin = open('BOJ10866.txt')

arr = deque()
v = 0
for _ in range(int(input())):
    user = list(sys.stdin.readline().split())

    if user[0]=='push_front':
        arr.appendleft(int(user[1]))
        v+=1
    elif user[0]=='push_back':
        arr.append(int(user[1]))
        v +=1
    elif user[0]=='pop_front':
        if v==0: print(-1)
        else:
            print(arr.popleft())
            v -=1
    elif user[0]=='pop_back':
        if v==0 : print(-1)
        else:
            print(arr.pop())
            v -= 1
    elif user[0]=='size':
        print(v)
    elif user[0]=='empty':
        if v==0 : print(1)
        else: print(0)
    elif user[0]=='front':
        if v==0: print(-1)
        else: print(arr[0])
    else:
        if v==0: print(-1)
        else: print(arr[-1])
