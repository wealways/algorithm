import sys
from collections import deque

sys.stdin = open('BOJ2667.txt')

N = int(input())
arr = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]
result = []

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def find(r,c,v):
    cnt = 0
    q=deque()
    q.append((r,c))
    arr[r][c]=v
    while q:
        r,c = q.popleft()
        cnt += 1
        for i in range(4):
            temp_r,temp_c = r+dr[i],c+dc[i]
            if 0<=temp_r<N and 0<=temp_c<N:
                if arr[temp_r][temp_c]==1:
                    arr[temp_r][temp_c]=v
                    q.append((temp_r,temp_c))
    return cnt

t = 2
for r in range(N):
    for c in range(N):
        if arr[r][c]==1:
            result.append(find(r,c,t))
            t+=1

print(len(result))
result = sorted(result)
for r in result:
    print(r)