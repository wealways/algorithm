import sys
from collections import deque
sys.stdin = open('BOJ1012.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def find(r,c):
    visit.add((r,c))
    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        for i in range(4):
            r_temp,c_temp = r+dx[i],c+dy[i]
            if 0<=r_temp<M and 0<=c_temp<N:
                if (r_temp,c_temp) not in visit and arr[r_temp][c_temp]==1:
                    q.append((r_temp,c_temp))
                    arr[r_temp][c_temp]=0
                    visit.add((r_temp,c_temp))



for _ in range(int(input())):
    M,N,K = map(int,input().split())
    arr = [[0]*N for _ in range(M)]
    for i in range(K):
        r,c = map(int,input().split())
        arr[r][c]=1
    visit=set()

    ans = 0
    for r in range(M):
        for c in range(N):
            if arr[r][c]:
                find(r, c)
                ans+=1
    print(ans)


