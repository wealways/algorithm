import sys
sys.stdin = open('BOJ1697.txt')
from collections import deque

N,K = map(int,sys.stdin.readline().split())
Max = 100000
visit=[0]*(Max+1)
if N >=K:
    print(N-K)
else:
    q=deque()
    q.append(N)
    while q:
        time = q.popleft()
        if time==K:
            print(visit[time])
            break
        for t in (time-1,time+1,time*2):
            if 0<=t<=Max and not visit[t]:
                visit[t] = visit[time]+1
                q.append(t)
