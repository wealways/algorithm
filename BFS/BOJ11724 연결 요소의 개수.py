import sys
from collections import deque
sys.stdin = open('BOJ11724.txt')


for _ in range(int(input())):
    N,M = map(int,sys.stdin.readline().split())
    graph={i:[] for i in range(1,N+1)}
    for m in range(M):
        temp = list(map(int,sys.stdin.readline().split()))
        graph[temp[0]].append(temp[1])
        graph[temp[1]].append(temp[0])

    visit = [1]+[0]*N
    cnt = 0
    for g in graph.keys():
        if not visit[g]:
            cnt += 1
            q = deque()
            q.append(g)
            visit[g]=1
            while q:
                temp = q.popleft()
                for i in graph[temp]:
                    if not visit[i]:
                        q.append(i)
                        visit[i]=1
    print(cnt)