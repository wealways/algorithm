import sys
from collections import deque
sys.stdin = open('BOJ7576.txt')
C,R = map(int,sys.stdin.readline().split())

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(R)]

good = deque()
for r in range(R):
    for c in range(C):
        if arr[r][c]==1:
            good.append((r,c,0))

dr = [0,0,1,-1]
dc = [1,-1,0,0]

while good:
    r,c,day = good.popleft()
    for i in range(4):
        temp_r,temp_c = r + dr[i],c + dc[i]
        if 0<=temp_r<R and 0<=temp_c<C and arr[temp_r][temp_c]==0:
            good.append((temp_r,temp_c,day+1))
            arr[temp_r][temp_c] = 1

flag = 0
for r in range(R):
    if arr[r].count(0)>0:
        flag=1
        break
if flag==0:
    print(day)
else:
    print(-1)