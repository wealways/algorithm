import sys
sys.stdin = open('BOJ11403.txt')

N = int(input())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def find(v):
    for i in range(N):
        if not visit[i] and arr[v][i]:
            visit[i]=1
            find(i)


for r in range(N):
    visit = [0] * N
    find(r)
    for c in range(N):
        if visit[c]==1:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()