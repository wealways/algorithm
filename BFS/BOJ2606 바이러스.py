import sys
from collections import deque
sys.stdin = open('BOJ2606.txt')

N = int(input())
network = {i:set() for i in range(1,N+1)}

for _ in range(int(input())):
    temp = list(map(int,sys.stdin.readline().split()))
    network[temp[0]].add(temp[1])
    network[temp[1]].add(temp[0])

visit= []
q = deque()
q.append(1)
visit.append(1)
while q:
    temp = q.popleft()
    for t in network[temp]:
        if t not in visit:
            visit.append(t)
            q.append(t)
print(len(visit)-1)