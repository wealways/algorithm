import sys
from collections import deque
sys.stdin = open('BOJ7569.txt')

C,R,H = map(int,sys.stdin.readline().split())

arr = []
for _ in range(H):
    temp = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
    arr.append(temp)

dr=[0,0,1,-1,0,0]
dc=[1,-1,0,0,0,0]
dh=[0,0,0,0,1,-1]

q = deque()
temp = 0
for h in range(H):
    for r in range(R):
        for c in range(C):
            if arr[h][r][c]==1:
                q.append((r,c,h,0))
            if arr[h][r][c]==0:
                temp+=1

if temp==0:
    print(0)
else:
    while q:
        r,c,h,day = q.popleft()
        for i in range(6):
            temp_r,temp_c,temp_h = r+dr[i], c+dc[i], h+dh[i]
            if 0<= temp_r<R and 0<=temp_c<C and 0<=temp_h<H:
                if arr[temp_h][temp_r][temp_c]==0:
                    arr[temp_h][temp_r][temp_c]= 1
                    q.append((temp_r,temp_c,temp_h,day+1))

    flag = 0
    for h in range(H):
        if flag==0:
            for r in range(R):
                if arr[h][r].count(0):
                    print(-1)
                    flag = 1
                    break
    if flag==0:
        print(day)
