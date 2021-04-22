import sys
from itertools import combinations

sys.stdin = open('BOJ15686.txt')

N,M= map(int,sys.stdin.readline().split())
road = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]


chicken = []
home = []
minv = 999999999999999999999

for r in range(N):
    for c in range(N):
        if road[r][c]==2:
            chicken.append((r,c))
        elif road[r][c]==1:
            home.append((r,c))

for ch in combinations(chicken,M):
    sumv = 0
    for h in home:
        sumv += min([abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in ch])
        if minv <= sumv :break
    if sumv < minv :
        minv = sumv


print(minv)
# print(home)