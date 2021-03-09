import sys
sys.stdin = open('BOJ1260.txt')

def dfs(v,s):
    print(s,end=' ')
    for n in range(N):
        if not visit[n] and arr[s-1][n]==1:
            visit[n] = 1
            dfs(v+1,n+1)



for _ in range(int(input())):
    N,M,V = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    visit = [0]*N
    for m in range(M):
        r,c = map(int,input().split())
        arr[r-1][c-1] = 1
        arr[c-1][r-1] = 1
    visit[V-1]= 1
    dfs(0,V)
    print()
