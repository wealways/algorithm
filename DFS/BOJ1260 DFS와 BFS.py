import sys
from collections import deque
sys.stdin = open('BOJ1260.txt')

def dfs(v):
    print(v,end=' ')
    for n in range(N):
        if not visit[n] and arr[v-1][n]==1:
            visit[n] = 1
            dfs(n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visit[v-1] = 1
    while q:
        temp = q.popleft()
        print(temp,end=' ')
        for idx,a in enumerate(arr[temp-1]):
            if not visit[idx] and a==1:
                q.append(idx+1)
                visit[idx]=1

for _ in range(int(input())):
    N, M, V = map(int, sys.stdin.readline().split())
    arr = [[0]*N for _ in range(N)]
    visit = [0]*N
    for m in range(M):
        r,c = map(int,sys.stdin.readline().split())
        arr[r-1][c-1] = 1
        arr[c-1][r-1] = 1
    visit[V-1]= 1
    dfs(V)
    print()
    visit = [0] * N
    bfs(V)
    print()

N,M,V = map(int,sys.stdin.readline().split())
arr = [[0]*N for _ in range(N)]
visit = [0]*N
for m in range(M):
    r,c = map(int,sys.stdin.readline().split())
    arr[r-1][c-1] = 1
    arr[c-1][r-1] = 1
visit[V-1]= 1
dfs(V)
print()
visit = [0] * N
bfs(V)
print()